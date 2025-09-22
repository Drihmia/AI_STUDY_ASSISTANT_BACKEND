import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from datetime import timedelta
from os import getenv
from flask_compress import Compress
import requests
from flask_cors import CORS

load_dotenv()

# Load Gemini API key from environment variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

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
