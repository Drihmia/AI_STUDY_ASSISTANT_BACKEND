import os
import sys
import json
from flask import Flask, request, jsonify, make_response
from groq import Groq
from dotenv import load_dotenv
import threading
import time
import signal

load_dotenv()

app = Flask(__name__)
api_key = os.environ.get("GROQ_API_KEY")

print("Groq api key:", api_key)
client = Groq(api_key=api_key)

system_prompt = {
    "role": "system",
    "content": """never use a language but French or English
each msg should be in a single language

You are a helpful assistant. For the first question, ask the student in both French and English which language they prefer to use. Whichever language is chosen, always respond in that language and try to understand anything they say in any language unless the student changes it. Always ask the student's age to determine the level of depth to provide:

14-15 years: common core in Morocco
16-17 years: first year of baccalaureate (ask for the specialty: experimental sciences or mathematical sciences)
17 years and older: baccalaureate (experimental sciences: PC and SVT options, mathematical sciences: options A and B)
Then, ask which subject the student wants to know more about (physics or chemistry), and specify the course or lesson. Be stricter in case of scientific errors and put more effort into responding to scientific questions. When asking the student's age, also ask if they want a spell check of their French or if they want to learn in English as an exception. Never ask more than one question per prompt. respond to the student formatted in HTML."""
}

# Dictionary to store chat histories for each user (identified by cookies)
user_chat_histories = {}

# Path to the directory where chat histories are saved
history_dir = 'chat_histories/'

# Function to load chat histories for a specific user
def load_chat_history(user_id):
    user_history_file = os.path.join(history_dir, f"history_{user_id}.json")
    if os.path.exists(user_history_file):
        with open(user_history_file, 'r') as json_file:
            return json.load(json_file)
    else:
        return [system_prompt]  # Return initial prompt if no history exists

# Function to save chat histories to a user-specific file
def save_chat_history(user_id):
    user_history_file = os.path.join(history_dir, f"history_{user_id}.json")
    with open(user_history_file, 'w') as json_file:
        json.dump(user_chat_histories[user_id], json_file, indent=4)
    print(f"Chat history for user {user_id} saved successfully.")

# Register signal handler for graceful shutdown (e.g., when you press Ctrl+C)
def handle_signal(signal, frame):
    print("\nSaving chat histories before shutdown...")
    for user_id in user_chat_histories:
        save_chat_history(user_id)
    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handle_signal)

# Load the chat histories on server startup
if not os.path.exists(history_dir):
    os.makedirs(history_dir)

# Function to handle the chat
def chat(system_messages):
    chat_completion = client.chat.completions.create(
        messages=system_messages,
        max_tokens=300,
        model="llama3-8b-8192"
    )
    return chat_completion.choices[0].message.content


@app.route('/chat', methods=['POST'])
def chat_endpoint():
    # Get the user message from the request
    user_message = request.json.get('message')

    # Get the user ID from the cookie
    user_id = request.cookies.get('user_id')

    print("user_id:", user_id)

    if not user_id:
        # If no user ID, generate a new one (this is only for new users)
        user_id = str(len(user_chat_histories) + 1)  # simple user ID generation

    # Ensure there's a history for the user by loading their specific history file
    if user_id not in user_chat_histories:
        user_chat_histories[user_id] = load_chat_history(user_id)

    # Append the user's message to their chat history
    user_chat_histories[user_id].append({"role": "user", "content": user_message})

    # Get the response from the AI
    response = chat(user_chat_histories[user_id])

    # Append the assistant's response to the chat history
    user_chat_histories[user_id].append({"role": "assistant", "content": f"---- {response}"})

    # Trigger saving chat history to file in the background before responding
    threading.Thread(target=save_chat_history, args=(user_id,), daemon=True).start()

    # Set the user ID in the response cookie
    resp = make_response(jsonify({"response": response}))
    resp.set_cookie('user_id', user_id)  # Set user ID in the cookie for subsequent visits
    return resp

if __name__ == '__main__':
    app.run(port=5001, debug=True)

