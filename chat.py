import os
import sys
import json
from flask import Flask, request, jsonify, make_response
from dotenv import load_dotenv
import signal
from uuid import uuid4
import google.generativeai as genai
from system_prompt import system_prompt_parts
from tools.utils import (load_chat_history,
                         save_chat_history,
                         handle_signal,
                         load_chat_history_startup
                         )
from tools.gemini_chat import chat_gemini

load_dotenv()

app = Flask(__name__)

# Path to the directory where chat histories are saved
history_dir = 'chat_histories/'

# Dictionary to store chat histories for each user (identified by cookies)
user_chat_histories = load_chat_history_startup({}, history_dir)

# Load the chat histories on server startup
load_chat_history_startup(user_chat_histories, history_dir)

@app.route('/api/chat', methods=['post'])
def chat_endpoint():
    """
    Chat endpoint
    """

    # get the user id from the cookie
    user_id = request.cookies.get('user_id')
    usr_id_exist = 1

    if not user_id:
        # if no user id, generate a new one (this is only for new users)
        user_id = str(len(user_chat_histories)) + '_' + str(uuid4())
        usr_id_exist = 0

    # ensure there's a history for the user by loading their specific history file
    if user_id not in user_chat_histories.keys():
        print("user_id:", user_id, "not in user_chat_histories")
        print("user_ids in history are:", user_chat_histories.keys())
        user_chat_histories[user_id] = []

    # get the user message from the request
    user_message = request.json.get('message')

    if not user_message:
        return jsonify({"response": '', "history": user_chat_histories[user_id]})

    # append the user's message to the chat history
    user_chat_histories[user_id].append({"role": "user", "parts": (user_message)})

    # get the response from the ai
    response: str = chat_gemini(user_chat_histories[user_id])
    print("-+"*100)
    print("response:", response)
    print("-+"*100)

    # append the model's response to the chat history
    user_chat_histories[user_id].append({"role": "model", "parts": (response)})
    save_chat_history(user_chat_histories, user_id, history_dir)


    # print("-+"*100)
    # print("user_chat_histories:", user_chat_histories)
    # print("-+"*100)

    # set the user id in the response cookie
    resp = make_response(jsonify({"response": response}))

    if not usr_id_exist:
        resp.set_cookie('user_id', user_id)  # set user id in the cookie for subsequent visits
    return resp


@app.route('/api/history', methods=['GET'])
def load_history():
    # Get the user ID from the cookie
    user_id = request.cookies.get('user_id')
    # print("user_chat_histories:", user_chat_histories.keys())

    try:
        # Return the user's chat history
        resp = make_response(jsonify({"history": user_chat_histories[user_id]}))
    except:
        resp = make_response(jsonify({"history": []}))

    return resp


if __name__ == '__main__':

    # Register the signal handler for SIGINT (Ctrl+C)
    # signal.signal(signal.SIGINT, handle_signal)
    # Register the signal handler for SIGINT (Ctrl+D)
    # signal.signal(signal.SIGTERM, handle_signal)
    app.run(port=5001, debug=True)

