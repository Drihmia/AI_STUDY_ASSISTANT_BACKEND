from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, request, jsonify, make_response, session
from flask_cors import CORS
from flask_compress import Compress
import google.generativeai as genai
from os import getenv, path, listdir
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
                         get_current_time,
                         print_logs_with_time,
                         )
from tools.chat_utils import update_form_with_unique_ids
from tools.gemini_chat import (
    chat_gemini_generate_content,
    chat_gemini_send_message,
)
from chat_gimini import chat_endpoint as chat_endpoint_gemini

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
    print_logs_with_time("session from before_request:", session)


# Add root endpoint handler
@app.route('/')
def root():
    return jsonify({"status": "ok"})


@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    """
    Chat endpoint
    """
    return chat_endpoint_gemini()

    # Get the user id from args:
    user_id = request.args.get('user_id')
    print_logs_with_time("user_id from args:", user_id)
    if not user_id or user_id == 'undefined':
        print_logs_with_time("User ID not found in args")
        return jsonify({ "response": '', "form_id": session.get('form_id', ''), 'error': 'User ID not found' }), 400
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
        print_logs_with_time("answers:", answers)
        formatted_answers = [k + ': ' + v for k, v in answers.items() if k != 'language']
        user_message = f"{structured_message_based_on_user_language.get(language)}:<br>&emsp;➔ {'<br>&emsp;➔ '.join(formatted_answers)}<br>"
    session['answers'] = None

    if not user_message:
        return jsonify({ "response": '', "form_id": session.get('form_id', '') , 'user_message': user_message })

    if last_message_user.get(user_id) == user_message:
        print_logs_with_time("User message is the same as the last message", "+" * 20)
        return jsonify({ "response": '', "form_id": session.get('form_id', ''), 'user_message': user_message })

    last_message_user[user_id] = user_message
    print_logs_with_time("User message:", user_message)
    print_logs_with_time("*" * 50)

    # append the user's message to the chat history
    temp_list = [{"role": "user", "parts": (append_current_time('user', user_message))}]

    # get the response from the ai
    try:
        response: str = chat_gemini_generate_content(user_chat_histories[user_id] + temp_list)
        if not response:
            raise Exception("Response is empty")

        print_logs_with_time("response from gemini_generate_content:", response[:10], '\t'*2, response[-50:] + '\n')

    except Exception as e:
        print_logs_with_time("ERROR while generating content")
        print_logs_with_time("Exception:", e)
        try:
            response: str = chat_gemini_send_message(user_chat_histories[user_id] + temp_list, user_message)

            if response:
                print_logs_with_time("response from gemini_send_message (After an error in generate content):", response[:10], '\t'*2, response[-50:] + '\n')
            model_number = 2
        except Exception as e:
            print_logs_with_time("ERROR while sending message")
            print_logs_with_time("Exception:", e)
            print_logs_with_time(("+++++*"*10 + "\n")*4)
            return jsonify({ "response": '', "form_id": session.get('form_id', ''), 'error': 'The qouta has been reached, Please try again in a minute' }), 400
            response = "Sorry, I am unable to generate a response at the moment. Please try again later."

    hopeless = False
    max_tries = 20
    tries = 0
    if not response:
        response = '\n'
    while response and not response.strip():
        tries += 1
        print_logs_with_time("=" * 50)
        print_logs_with_time("response is empty")
        print_logs_with_time("=" * 50)
        if model_number == 1:
            try:
                response = chat_gemini_generate_content(user_chat_histories[user_id] + temp_list)
            except Exception as e:
                print_logs_with_time("ERROR while generating content after response is empty")
                print_logs_with_time("Exception:", e)

#                 if hopeless:
                    # print_logs_with_time(("--------1"*10 + "\n")*4)
                    # response = "Sorry, I am unable to generate a response at the moment. Please try again later."
                    # break
                # hopeless = True
                model_number = 2
        elif model_number == 2:
            try:
                response = chat_gemini_send_message(user_chat_histories[user_id] + temp_list, user_message)
            except Exception as e:
                print_logs_with_time("ERROR while sending message after response is empty")
                print_logs_with_time("Exception:", e)

                # if hopeless:
                    # print_logs_with_time(("--------2"*10 + "\n")*4)
                    # response = "Sorry, I am unable to generate a response at the moment. Please try again later."
                    # break
                # hopeless = True
                model_number = 1
        if tries >= max_tries:
            print_logs_with_time("+" * 50, "Max tries reached", "+" * 50)
            print_logs_with_time(("--------3"*10 + "\n")*4)
            return jsonify({ "response": '', "form_id": session.get('form_id', ''), 'error': 'The qouta has been reached, Please try again in a minute' }), 400
            response = "Sorry, I am unable to generate a response at the moment."
            response += "<br>The qouta for the day has been reached. Please try again in a few minutes."
            # return jsonify({ "response": '', "form_id": session.get('form_id', ''), 'error': 'The qouta has been reached, Please try again in a minute' }), 400
            break

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
            print_logs_with_time("ERROR while replacing the form id")
            print_logs_with_time("Exception:", e)
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
    resp = make_response(jsonify({ "response": temp_list[1].get('parts', 'something went wrong'), "form_id": random_string, 'user_message': temp_list[0].get('parts', 'something went wrong') }))
    print_logs_with_time("session from /api/chat:", session)

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
    # Get the user id from args:
    user_id = request.args.get("user_id")
    print_logs_with_time("user_id from args:", user_id)
    if not user_id or user_id == 'undefined':
        print_logs_with_time("User ID not found in args")
        # Get the user ID from the cookie
        return jsonify({ "response": '', "form_id": session.get('form_id', ''), 'error': 'User ID not found' }), 400
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
        print_logs_with_time("ERROR while loading history from /api/history")
        print_logs_with_time("Exception:", e)

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
        # print_logs_with_time("data json:", data)
    else:
        data = request.form.copy()
        # print_logs_with_time("data :", data)
    session['answers'] = data

    return chat_endpoint()

@app.route('/api/list_conversations', methods=['GET'], strict_slashes=False)
def list_conversations():
    """
    List all the list_conversations with password
    """

    if request.args.get('password') != getenv('PASSWORD', "123123"):
        return jsonify({'error': 'Unauthorized'}), 401

    if path.exists(history_dir):
        files = listdir(history_dir)
        # Create a list of tuples (filename, modification time, size in KB)
        files_with_time = [(file, datetime.fromtimestamp(path.getmtime(path.join(history_dir, file))), f"{path.getsize(path.join(history_dir, file)) / 1024:.2f} KB") for file in files]

        # Sort by modification time
        files_sorted = sorted(files_with_time, key=lambda x: x[1], reverse=True)
        return jsonify(files_sorted)
    return jsonify([])

# Content of a conversation based on the conversation ID
@app.route('/api/list_conversations/<conversation_id>', methods=['GET'], strict_slashes=False)
def conversation(conversation_id):
    """
    Get the conversation based on the conversation ID
    """

    if request.args.get('password') != getenv('PASSWORD', "123123"):
        return jsonify({'error': 'Unauthorized'}), 401

    if conversation_id in user_chat_histories:
        conversation = user_chat_histories[conversation_id].copy()
        conversation.reverse()
        return jsonify(conversation)

    return jsonify({'error': 'Conversation ID not found'}), 404


@app.route("/api/test/<value>", methods=["GET"], strict_slashes=False)
def test(value: str = "error"):
    """
    Test endpoint that returns a succuss message if the value is "ok"
    otherwise returns an error message
    """
    if value.lower() == "ok":
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "error": "Invalid value"}), 400


@app.errorhandler(404)
def not_found(e):
    """
    404 error handler
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    """
    500 error handler
    """
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Handle exceptions
    """
    print_logs_with_time("ERROR while handling exception")
    print_logs_with_time("Exception:", e)
    return jsonify({"error": str(e)}), 500

@app.errorhandler(400)
def bad_request(e):
    """
    400 error handler
    """
    return jsonify({"error": "Bad request"}), 400

if __name__ == '__main__':

    # Register the signal handler for SIGINT (Ctrl+C)
    # signal.signal(signal.SIGINT, handle_signal)
    # Register the signal handler for SIGINT (Ctrl+D)
    # signal.signal(signal.SIGTERM, handle_signal)
    AI_DEBUG = getenv('AI_DEBUG', False)
    app.run(debug=AI_DEBUG, host='0.0.0.0', port=5000)

