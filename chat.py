import os
import sys
import json
from flask import Flask, request, jsonify, make_response, session
from dotenv import load_dotenv
import signal
from uuid import uuid4
import google.generativeai as genai
from re import sub
from system_prompt import system_prompt_parts
from tools.utils import (load_chat_history,
                         save_chat_history,
                         handle_signal,
                         load_chat_history_startup
                         )
from tools.gemini_chat import chat_gemini

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Path to the directory where chat histories are saved
history_dir = 'chat_histories/'

# Dictionary to store chat histories for each user (identified by cookies)
user_chat_histories = load_chat_history_startup({}, history_dir)

# Load the chat histories on server startup
load_chat_history_startup(user_chat_histories, history_dir)

@app.route('/api/chat', methods=['POST'])
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
        # print("user_id:", user_id, "not in user_chat_histories from /api/chat")
        # print("user_ids in history are:", user_chat_histories.keys())
        user_chat_histories[user_id] = []

    user_message = ""
    if request.is_json:
        # get the user message from the request
        user_message = request.json.get('message', "").strip()
    answers = session.get('answers')
    # print("answers:", answers)

    if answers:
        formatted_answers = [k + ': ' + v for k, v in answers.items()]
        user_message = f"My answers to your testing form are:<br>&emsp;➔ {"<br>&emsp;➔ ".join(formatted_answers)}<br>"
    session['answers'] = None

    if not user_message:
        return jsonify({ "response": '' })

    # append the user's message to the chat history
    user_chat_histories[user_id].append({"role": "user", "parts": (user_message)})

    # get the response from the ai
    response: str = chat_gemini(user_chat_histories[user_id])
    # print("-+"*100)
    # print("response:", response)
    # print("-+"*100random_string)
    random_string = ""
    if '<form ' in response:
        pattern = r'(<form\s+[^>]*id=")[^"]*(")'
        random_string = '-' + str(uuid4())
        replacement = rf'\1{random_string}\2'

        res = response
        try:
            response = sub(pattern, replacement, response)
        except Exception as e:
            print("ERROR while replacing the form id")
            print("Exception:", e)
            response = (response + "\n\n" +
                        "Sorry, there was an error with this form. \
                        Please communicate with us using this code: "
                        + random_string)
            random_string = ""  # reset the random string if there's an error

        if res != response:
            session['form_id'] = random_string

    # append the model's response to the chat history
    user_chat_histories[user_id].append({"role": "model", "parts": (response)})
    save_chat_history(user_chat_histories[user_id], user_id, history_dir)


    # print("-+"*100)
    # print("user_chat_histories:", user_chat_histories[user_id])
    # print("-+"*100)

    # set the user id in the response cookie
    resp = make_response(jsonify({ "response": response, "form_id": random_string }))

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
        # print("session fron /api/history:", session)
        resp = make_response(jsonify({
            "history": user_chat_histories[user_id],
            'form_id': session.get('form_id', '')
        }))
        # Pretiffy the JSON response
        resp.headers['Content-Type'] = 'application/json'

        # print("*"*20, "responses and requests from /api/history", len(user_chat_histories), "*"*20)
        # for response in user_chat_histories[user_id]:
            # print(response["role"], ":", response['parts'])
    except Exception as e:
        print("ERROR while loading history from /api/history")
        print("Exception:", e)

        resp = make_response(jsonify({"history": [], 'form_id': session.get('form_id', '')}))

    return resp

@app.route('/api/answers', methods=['POST'])
def get_answers():
    """
    Get the answers to the questions
    """

    if request.is_json:
        # Parse the JSON data
        data = request.get_json()
        # print("data json:", data)
    else:
        data = request.form.copy()
        # print("data :", data)
    session['answers'] = data

    return chat_endpoint()


if __name__ == '__main__':

    # Register the signal handler for SIGINT (Ctrl+C)
    # signal.signal(signal.SIGINT, handle_signal)
    # Register the signal handler for SIGINT (Ctrl+D)
    # signal.signal(signal.SIGTERM, handle_signal)
    app.run(port=5001, debug=True)

