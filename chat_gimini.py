import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from datetime import timedelta
from os import getenv
from flask_compress import Compress
import requests
from flask_cors import CORS
from database import Database

load_dotenv()

app = Flask(__name__)

# Initialize the Compress extension
Compress(app)

# Set the Compress configuration
app.config['COMPRESS_MIN_SIZE'] = 500
app.config['COMPRESS_LEVEL'] = 9
app.config['COMPRESS_ALGORITHM'] = 'gzip'  # Force gzip
app.config['COMPRESS_MIMETYPES'] = [ 'application/json' ]

# Set the secret key for the session
app.secret_key = getenv('SECRET_KEY')

# Set the session lifetime to 365 days
app.permanent_session_lifetime = timedelta(days=365)

# Set the session cookie settings
app.config.update(
    SESSION_COOKIE_DOMAIN='.drihmia.me',
    SESSION_COOKIE_NAME='session',
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_SECURE=True,
)

CORS(app)

# Load Gemini API key from environment variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Initialize the database
db = Database(os.environ.get("MONGO_URI"))

# Define the endpoint for Gemini's chat completion API
GEMINI_CHAT_API_URL = "https://api.gemini-ai.com/v1/chat/completions"

# Initial system prompt
system_prompt = {
    "role": "system",
    "content": """never use a language but French or English
    each msg should be in a single language

    You are a helpful assistant. For the first question, ask the student in both French and English which language they prefer to use. Whichever language is chosen, always respond in that language and try to understand anything they say in any language unless the student changes it. Always ask the student's age to determine the level of depth to provide:

    14-15 years: common core in Morocco
    16-17 years: first year of baccalaureate (ask for the specialty: experimental sciences or mathematical sciences)
    17 years and older: baccalaureate (experimental sciences: PC and SVT options, mathematical sciences: options A and B)
    Then, ask which subject the student wants to know more about (physics or chemistry), and specify the course or lesson. Be stricter in case of scientific errors and put more effort into responding to scientific questions. When asking the student's age, also ask if they want a spell check of their French or if they want to learn in English as an exception. Never ask more than one question per prompt. Respond to the student formatted in HTML."""
}

def chat(system_messages):
    """Send a chat request to the Gemini API and return the assistant's response."""
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "messages": system_messages,
        "max_tokens": 150,
        "model": "gemini-large"
    }

    response = requests.post(GEMINI_CHAT_API_URL, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses

    return response.json()["choices"][0]["message"]["content"]

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    user_message = request.json.get('message')
    user_id = request.args.get("user_id")
    if not user_message:
        return jsonify({"error": "Message field is required."}), 400
    if not user_id:
        return jsonify({"error": "user_id field is required."}), 400

    # Get chat history from the database
    chat_history = db.get_history(user_id)
    if not chat_history:
        chat_history = [system_prompt]

    # Append user message to chat history
    chat_history.append({"role": "user", "content": user_message})

    try:
        # Get the assistant's response
        response_content = chat(chat_history)
        
        # Append assistant's response to the local chat history
        chat_history.append({"role": "assistant", "content": response_content})

        # Save the last two messages (user and assistant) to the database
        db.add_messages(user_id, chat_history[-2:])

        return jsonify({"response": response_content})
    except requests.exceptions.RequestException as e:
        print(f"Failed to send chat request to Gemini: {e}")
        return jsonify({"error": "Failed to process the request.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
