from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, request, jsonify, make_response, session
from flask_cors import CORS
from flask_compress import Compress
import google.generativeai as genai
from os import getenv
from re import sub
import signal
from threading import Thread
from uuid import uuid4
from system_prompt import system_prompt_parts
from tools.utils import (load_chat_history,
                         save_chat_history,
                         handle_signal,
                         load_chat_history_startup,
                         append_current_time,
                         )
from tools.chat_utils import update_form_with_unique_ids
from tools.gemini_chat import (
    chat_gemini_generate_content,
    chat_gemini_send_message,
)

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

# Path to the directory where chat histories are saved
history_dir = 'chat_histories/'

user_chat_histories = {}

last_message_user = {}

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
    model_number = 1

    if not user_id:
        # if no user id, generate a new one (this is only for new users)
        user_id = str(len(user_chat_histories)) + '_' + str(uuid4())
        usr_id_exist = 0

    # ensure there's a history for the user by loading their specific history file
    if user_id not in user_chat_histories.keys():
        user_chat_histories[user_id] = []

    user_message = ""
    if request.is_json:
        # get the user message from the request
        user_message = request.json.get('message', "").strip()
    answers = session.get('answers')

    structured_message_based_on_user_language = {
        'en': 'my answers to your test are',
        'fr': 'mes réponses à votre test sont',
        'ar': 'إجاباتي على اختبارك هي',
    }

    if answers:
        language = answers.get('language', 'en')
        print("answers:", answers)
        formatted_answers = [k + ': ' + v for k, v in answers.items() if k != 'language']
        user_message = f"{structured_message_based_on_user_language.get(language)}:<br>&emsp;➔ {"<br>&emsp;➔ ".join(formatted_answers)}<br>"
    session['answers'] = None

    if not user_message:
        return jsonify({ "response": '', "form_id": session.get('form_id', '') })

    if last_message_user.get(user_id) == user_message:
        print("User message is the same as the last message", "+" * 20)
        return jsonify({ "response": '', "form_id": session.get('form_id', '') })

    print("*" * 50)
    print("Last message user:", last_message_user.get(user_id))
    print("*" * 50)
    last_message_user[user_id] = user_message
    print("User message:", user_message)
    print("*" * 50)

    # append the user's message to the chat history
    temp_list = [{"role": "user", "parts": (append_current_time('user', user_message))}]

    # get the response from the ai
    try:
        response: str = chat_gemini_generate_content(user_chat_histories[user_id] + temp_list)
        print("response from gemini_generate_content:", response[-100:-1] + response[-1])
        model_number = 1
    except Exception as e:
        print("ERROR while generating content")
        print("Exception:", e)
        try:
            response: str = chat_gemini_send_message(user_chat_histories[user_id] + temp_list, user_message)
            model_number = 2
        except Exception as e:
            print("ERROR while sending message")
            print("Exception:", e)
            response = "Sorry, I am unable to generate a response at the moment. Please try again later."

    hopeless = False
    while response and not response.strip():
        print("=" * 50, end=' ')
        print("response is empty", end=' ')
        print("=" * 50)
        if model_number == 1:
            try:
                response = chat_gemini_generate_content(user_chat_histories[user_id] + temp_list)
            except Exception as e:
                print("ERROR while generating content after response is empty")
                print("Exception:", e)

                if hopeless:
                    response = "Sorry, I am unable to generate a response at the moment. Please try again later."
                    hopeless = False
                    break
                model_number = 2
                hopeless = True
        elif model_number == 2:
            try:
                response = chat_gemini_send_message(user_chat_histories[user_id] + temp_list, user_message)
            except Exception as e:
                print("ERROR while sending message after response is empty")
                print("Exception:", e)

                if hopeless:
                    response = "Sorry, I am unable to generate a response at the moment. Please try again later."
                    hopeless = False
                    break
                model_number = 1
                hopeless = True

    random_string = session.get('form_id', '')
    if '<form ' in response:
        pattern = r'(<form\s+[^>]*id=")[^"]*(")'
        random_string = '-' + str(uuid4())
        replacement = rf'\1{random_string}\2'

        res = response
        try:
            response = sub(pattern, replacement, response)
            response = update_form_with_unique_ids(response)
        except Exception as e:
            print("ERROR while replacing the form id")
            print("Exception:", e)
            response = (response + "\n\n" +
                        "Sorry, there was an error with this form. \
                        Please communicate with us using this code: "
                        + random_string)
            # random_string = ""  # reset the random string if there's an error

        # if res != response:
        session['form_id'] = random_string

    # append the model's response to the chat history
    temp_list.append({"role": "model", "parts": append_current_time('model', response)})
    user_chat_histories[user_id].extend(temp_list)
    # save_chat_history(user_chat_histories[user_id], user_id, history_dir)
    Thread(target=save_chat_history, args=(user_chat_histories[user_id], user_id, history_dir), daemon=True).start()




    # set the user id in the response cookie
    resp = make_response(jsonify({ "response": temp_list[1].get('parts', 'something went wrong'), "form_id": random_string }))
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
        limit = int(request.args.get('limit', 200))

        # Ensure limit is even
        if limit % 2 != 0:
            limit += 1
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
        total_messages = len(user_history)

        # Ensure total_messages is even (if an odd number exists, remove the last entry)
        if total_messages % 2 != 0:
            total_messages -= 1

        # Calculate the max_page based on the even messages pairs
        max_page = (total_messages + limit - 1) // limit

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
            "max_page": max_page,
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
            "max_page": 1,
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
    app.run(port=5001, debug=True)

