from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, request, jsonify, make_response, session
from flask_cors import CORS
import google.generativeai as genai
from os import getenv
from re import sub
import signal
from uuid import uuid4
from system_prompt import system_prompt_parts
from tools.utils import (load_chat_history,
                         save_chat_history,
                         handle_signal,
                         load_chat_history_startup
                         )
from tools.gemini_chat import chat_gemini

load_dotenv()

app = Flask(__name__)

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

# Path to the directory where chat histories are saved
history_dir = 'chat_histories/'

# Dictionary to store chat histories for each user (identified by cookies)
user_chat_histories = load_chat_history_startup({}, history_dir)

# Load the chat histories on server startup
load_chat_history_startup(user_chat_histories, history_dir)


@app.before_request
def before_request():
    """
    Before request
    """
    session.permanent = True
    print("session from before_request:", session)


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
        user_message = f"My answers to your test are:<br>&emsp;➔ {"<br>&emsp;➔ ".join(formatted_answers)}<br>"
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
    print("session from /api/chat:", session)

    if not usr_id_exist:
        expire_date = datetime.now() + timedelta(days=365)
        resp.set_cookie('user_id',
                        value=user_id,
                        domain='.drihmia.me',   # Share cookie across all subdomains ai. and ai1. and any future subdomains.
                        secure=True,            # Set Secure=True to ensure it's only sent over HTTPS
                        httponly=True,          # For security
                        samesite='Lax',         # Set SameSite=Lax to prevent CSRF attacks
                        expires=expire_date     # Set the cookie to expire in 365 days
                        )
    return resp


@app.route('/api/history', methods=['GET'])
def load_history():
    # Get the user ID from the cookie
    user_id = request.cookies.get('user_id')

    # Get pagination parameters (page and limit), defaulting to page=1 and limit=30
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 30))
        limit = limit if limit%2 == 0 else limit + 1
    except ValueError:
        # If page or limit cannot be cast to integer, return bad request with error message
        return make_response(jsonify({
            "error": "Invalid page or limit parameter. Must be an integer.",
            "history": [],
            "page": 1,
            "limit": 5,
            "form_id": session.get('form_id', '')
        }), 400)

    try:
        # Check if the user has chat history
        if user_id not in user_chat_histories:
            raise ValueError("User history not found")

        user_history = user_chat_histories[user_id]

        # Reverse the history so the most recent messages are first
        reversed_history = user_history[::-1]

        # Calculate the index for pagination
        skip = (page - 1) * limit
        paginated_history = reversed_history[skip: skip + limit]

        # Prepare the response with paginated chat history
        resp = make_response(jsonify({
            "history": paginated_history[::-1],  # Reverse back to keep original order per page
            "page": page,
            "limit": limit,
            "form_id": session.get('form_id', '')
        }))
        resp.headers['Content-Type'] = 'application/json'

    except Exception as e:
        print("ERROR while loading history from /api/history")
        print("Exception:", e)

        resp = make_response(jsonify({
            "error": str(e),
            "history": [],
            "page": page,
            "limit": limit,
            "form_id": session.get('form_id', '')
        }))

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
    app.run(port=5001, debug=False)

