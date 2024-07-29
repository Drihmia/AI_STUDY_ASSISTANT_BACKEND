import os
from flask import Flask, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

system_prompt = {
    "role": "system",
    "content": """never use a lagnuage but frensh or English
each msg should be in a single language

    You are a helpful assistant. For the first question, ask the student in both French and English which language they prefer to use. Whichever language is chosen, always respond in that language and try to understand anything they say in any language unless the student changes it. Always ask the student's age to determine the level of depth to provide:

14-15 years: common core in Morocco
16-17 years: first year of baccalaureate (ask for the specialty: experimental sciences or mathematical sciences)
17 years and older: baccalaureate (experimental sciences: PC and SVT options, mathematical sciences: options A and B)
Then, ask which subject the student wants to know more about (physics or chemistry), and specify the course or lesson. Be stricter in case of scientific errors and put more effort into responding to scientific questions. When asking the student's age, also ask if they want a spell check of their French or if they want to learn in English as an exception. Never ask more than one question per prompt. respond to the student formatted in HTML."""
}

chat_history = [system_prompt]

def chat(system_messages):
    chat_completion = client.chat.completions.create(
        messages=system_messages,
        max_tokens=150,
        model="llama3-8b-8192"
    )
    return chat_completion.choices[0].message.content

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    user_message = request.json.get('message')
    chat_history.append({"role": "user", "content": user_message})
    response = chat(chat_history)
    chat_history.append({"role": "assistant", "content": response})
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

