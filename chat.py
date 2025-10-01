import os
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
from tools.utils import (
    load_chat_history,
    save_chat_history,
    load_all_feedback,
    save_feedback,
    load_all_teacher_messages,
    save_teacher_message,
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
from database import Database
import json
from bson.objectid import ObjectId

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- App Configuration ---
Compress(app)
app.config.update(
    COMPRESS_MIN_SIZE=500,
    COMPRESS_LEVEL=9,
    COMPRESS_ALGORITHM='gzip',
    COMPRESS_MIMETYPES=['application/json'],
    SECRET_KEY=getenv('SECRET_KEY'),
    PERMANENT_SESSION_LIFETIME=timedelta(days=365),
    SESSION_COOKIE_DOMAIN='.drihmia.me',
    SESSION_COOKIE_NAME='session',
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_SECURE=True,
)
CORS(app)

# --- Storage and Database Initialization ---
db = Database(os.environ.get("MONGO_URI"))
history_dir = 'chat_histories/'
feedback_dir = 'feedbacks/'
contact_teacher_dir = 'contact_teacher/'

user_chat_histories = {}
feedbacks = {}
teacher_messages = {}

last_message_user = {}
STORAGE_TYPE = getenv('STORAGE_TYPE', 'local')

# --- Initial Data Loading ---
if STORAGE_TYPE == 'remote':
    print("Loading chat histories from remote MongoDB...")
    user_chat_histories = db.get_all_histories()
    print(f"Number of chat histories loaded: {len(user_chat_histories)}")
else:
    print("Loading chat histories from local file system...")
    user_chat_histories = load_chat_history_startup(user_chat_histories, history_dir)
    print("Loading feedbacks from local file system...")
    feedbacks = load_all_feedback(feedback_dir)
    print(f"Number of feedbacks loaded: {len(feedbacks)}")
    print("Loading teacher messages from local file system...")
    teacher_messages = load_all_teacher_messages(contact_teacher_dir)
    print(f"Number of teacher messages loaded: {len(teacher_messages)}")

@app.before_request
def before_request():
    session.permanent = True

# --- Core API Endpoints ---
@app.route('/')
def root():
    return jsonify({"status": "ok"})

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    """
    Chat endpoint
    """

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
        user_chat_histories[user_id] = db.get_history(user_id)

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

                model_number = 2
        elif model_number == 2:
            try:
                response = chat_gemini_send_message(user_chat_histories[user_id] + temp_list, user_message)
            except Exception as e:
                print_logs_with_time("ERROR while sending message after response is empty")
                print_logs_with_time("Exception:", e)

                model_number = 1
        if tries >= max_tries:
            print_logs_with_time("+" * 50, "Max tries reached", "+" * 50)
            print_logs_with_time(("--------3"*10 + "\n")*4)
            return jsonify({ "response": '', "form_id": session.get('form_id', ''), 'error': 'The qouta has been reached, Please try again in a minute' }), 400
            response = "Sorry, I am unable to generate a response at the moment."
            response += "<br>The qouta for the day has been reached. Please try again in a few minutes."
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

        session['form_id'] = random_string

    # append the model's response to the chat history
    temp_list.append({"role": "model", "parts": append_current_time('model', response)})
    user_chat_histories[user_id].extend(temp_list)
    
    if STORAGE_TYPE == 'remote':
        Thread(target=db.add_messages, args=(user_id, temp_list), daemon=True).start()
    else:
        Thread(target=save_chat_history, args=(user_chat_histories[user_id], user_id, history_dir), daemon=True).start()

    # set the user id in the response cookie
    resp = make_response(jsonify({ "response": temp_list[1].get('parts', 'something went wrong'), "form_id": random_string, 'user_message': temp_list[0].get('parts', 'something went wrong') }))
    print_logs_with_time("session from /api/chat:", session)

    if not usr_id_exist:
        expire_date = datetime.now() + timedelta(days=365)
        resp.set_cookie('user_id',
                        value=user_id,
                        domain='.drihmia.me',
                        secure=True,
                        httponly=True,
                        samesite='Lax',
                        expires=expire_date
                        )
    return resp


@app.route('/api/history', methods=['GET'])
def load_history():
    # Get the user id from args:
    user_id = request.args.get("user_id")
    print_logs_with_time("user_id from args:", user_id)
    if not user_id or user_id == 'undefined':
        print_logs_with_time("User ID not found in args")
        return jsonify({ "response": '', "form_id": session.get('form_id', ''), 'error': 'User ID not found' }), 400
        user_id = request.cookies.get('user_id')

    # Get pagination parameters (page and limit), defaulting to page=1 and limit=30
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 2))

        if limit % 2 != 0:
            limit += 1
    except ValueError:
        return make_response(jsonify({
            "error": "Invalid page or limit parameter. Must be an integer.",
            "history": [],
            "page": 1,
            "limit": 5,
            "form_id": session.get('form_id', '')
        }), 400)

    try:
        if user_id not in user_chat_histories:
            raise ValueError("User history not found")

        user_history = user_chat_histories[user_id]
        total_messages = len(user_history)

        if total_messages % 2 != 0:
            total_messages -= 1

        max_page = (total_messages + limit - 1) // limit
        reversed_history = user_history[::-1]
        skip = (page - 1) * limit
        paginated_history = reversed_history[skip: skip + limit]

        resp = make_response(jsonify({
            "history": paginated_history[::-1],
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


# --- Feedback API Endpoints ---
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Submit new feedback.
    This endpoint allows users to submit feedback, which is then stored either in the
    local file system or a remote MongoDB database, depending on the server configuration.
    A `userId` is now required to link feedback to a user.
    """
    data = request.get_json()
    # Validate that all required fields are present
    if not data or not all(k in data for k in ['text', 'rating', 'userId']):
        return jsonify({"error": "Missing required feedback data: text, rating, and userId are required"}), 400

    # --- Create the feedback document ---
    feedback_id = str(ObjectId())
    feedback_doc = {
        "_id": feedback_id,
        "userId": data['userId'], # Link to the user
        "text": data['text'],
        "rating": data['rating'],
        "displayName": data.get('fullName', 'Anonymous'),
        "email": data.get('emailAdress', ''),
        "createdAt": datetime.utcnow().isoformat() + 'Z'  # ISO 8601 format for consistency
    }

    # --- Save the feedback based on storage type ---
    try:
        if STORAGE_TYPE == 'remote':
            # The `submit_feedback` method in the Database class handles MongoDB storage
            db.submit_feedback(feedback_doc)
        else:
            # The `save_feedback` utility function handles local file storage
            save_feedback(feedback_doc, feedback_dir)
            feedbacks[feedback_id] = feedback_doc  # Update in-memory cache
    except Exception as e:
        print_logs_with_time(f"ERROR submitting feedback: {e}")
        return jsonify({"error": "Could not save feedback"}), 500

    return jsonify({"success": True, "feedback": feedback_doc}), 201

@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    """
    Get feedback with cursor-based pagination.
    This endpoint retrieves a paginated list of feedback, allowing for features like
    infinite scrolling or a "load more" button.
    """
    limit = int(request.args.get('limit', 10))
    cursor = request.args.get('cursor')

    try:
        if STORAGE_TYPE == 'remote':
            # `get_feedback` in the Database class handles pagination for MongoDB
            items, next_cursor = db.get_feedback(cursor, limit)
            for item in items:
                item['_id'] = str(item['_id'])
            return jsonify({"items": items, "nextCursor": next_cursor})
        else:
            # --- Local storage pagination logic ---
            sorted_feedbacks = sorted(feedbacks.values(), key=lambda x: x['createdAt'], reverse=True)
            
            start_index = 0
            if cursor:
                try:
                    # Find the index of the item after the cursor
                    start_index = next(i for i, item in enumerate(sorted_feedbacks) if item['_id'] == cursor) + 1
                except StopIteration:
                    # If cursor is not found, it means we're at the end of the list
                    return jsonify({"items": [], "nextCursor": None})

            end_index = start_index + limit
            items = sorted_feedbacks[start_index:end_index]
            
            next_cursor = None
            if end_index < len(sorted_feedbacks):
                # The next cursor is the ID of the last item in the current page
                next_cursor = items[-1]['_id']
                
            return jsonify({"items": items, "nextCursor": next_cursor})

    except Exception as e:
        print_logs_with_time(f"ERROR getting feedback: {e}")
        return jsonify({"error": "Could not retrieve feedback"}), 500


# --- Contact Teacher Endpoint ---
@app.route('/api/contact_teacher', methods=['POST'])
def contact_teacher():
    """
    Submit a message to the teacher.
    This endpoint captures messages from users intended for the teacher, storing them
    with user identification for tracking.
    """
    data = request.get_json()
    if not data or not all(k in data for k in ['userId', 'fullName', 'emailAddress', 'message']):
        return jsonify({"error": "Missing required fields: userId, fullName, emailAddress, and message are required"}), 400

    # --- Create the message document ---
    message_id = str(ObjectId())
    message_doc = {
        "_id": message_id,
        "userId": data['userId'],
        "fullName": data['fullName'],
        "emailAddress": data['emailAddress'],
        "message": data['message'],
        "createdAt": datetime.utcnow().isoformat() + 'Z'  # ISO 8601 format
    }

    # --- Save the message based on storage type ---
    try:
        if STORAGE_TYPE == 'remote':
            db.submit_teacher_message(message_doc)
        else:
            save_teacher_message(message_doc, contact_teacher_dir)
            teacher_messages[message_id] = message_doc # Update in-memory cache
    except Exception as e:
        print_logs_with_time(f"ERROR submitting teacher message: {e}")
        return jsonify({"error": "Could not save message"}), 500

    return jsonify({"success": True, "message": "Your message has been sent to the teacher."}), 201


@app.route('/api/answers', methods=['POST'])
def get_answers():
    """
    Get the answers to the questions
    """
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.copy()
    session['answers'] = data

    return chat_endpoint()

@app.route('/api/list_conversations', methods=['GET'], strict_slashes=False)
def list_conversations():
    """
    List all the list_conversations with password
    """
    if request.args.get('password') != getenv('PASSWORD_CONVERSATIONS'):
        return jsonify({'error': 'Unauthorized'}), 401

    if STORAGE_TYPE == 'remote':
        return jsonify(db.get_conversations_list())

    if path.exists(history_dir):
        files = listdir(history_dir)
        files_with_time = [(file, datetime.fromtimestamp(path.getmtime(path.join(history_dir, file))), f"{path.getsize(path.join(history_dir, file)) / 1024:.2f} KB") for file in files]
        files_sorted = sorted(files_with_time, key=lambda x: x[1], reverse=True)
        return jsonify(files_sorted)
    return jsonify([])

@app.route('/api/list_conversations/<conversation_id>', methods=['GET'], strict_slashes=False)
def conversation(conversation_id):
    """
    Get the conversation based on the conversation ID
    """
    if request.args.get('password') != getenv('PASSWORD_CONVERSATIONS'):
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
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    print_logs_with_time("ERROR while handling exception")
    print_logs_with_time("Exception:", e)
    return jsonify({"error": str(e)}), 500

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400

if __name__ == '__main__':
    AI_DEBUG = getenv('AI_DEBUG', False)
    app.run(debug=AI_DEBUG, host='0.0.0.0', port=5000)