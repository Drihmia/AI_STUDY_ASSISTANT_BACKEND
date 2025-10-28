# -*- coding: utf-8 -*-

# --- Imports ---
import os
from uuid import uuid4
from re import sub
from flask import request, jsonify, session, make_response
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId

from app import (
    app, 
    db, 
    user_chat_histories, 
    feedbacks, 
    teacher_messages, 
    last_message_user, 
    last_image_status_user,
    STORAGE_TYPE,
    history_dir,
    feedback_dir,
    contact_teacher_dir
)

from tools.utils import (
    save_feedback,
    save_teacher_message,
)
from tools.log import print_logs_with_time
from tools.chat_utils import handle_form_in_response, append_current_time
from tools.gemini_chat import (
    chat_gemini_generate_content,
    chat_gemini_send_message,
    chat_gemini_generate_content_from_image,
)
from tools.send_email import send_teacher_email
from tools.endpoint_utils import (
    get_user_id,
    load_user_history,
    save_and_respond_chat,
    save_history
)

# --- Hooks ---
@app.before_request
def before_request():
    session.permanent = True

# --- Core API Endpoints ---
@app.route('/')
def root():
    """Root endpoint to check the status of the server."""
    return jsonify({"status": "ok"})

@app.route('/api/image', methods=['POST'])
def image_endpoint():
    """
    Handles image-based chat requests. It receives an image and an optional message,
    generates a response using a generative AI model, and saves the conversation history.
    """
    user_id, _ = get_user_id(request, user_chat_histories)
    load_user_history(user_id, user_chat_histories, STORAGE_TYPE, db, history_dir)

    user_message = request.form.get('message', "").strip()
    print_logs_with_time("user_message from image endpoint:", user_message)

    if 'image' not in request.files:
        return jsonify({"response": '', "form_id": session.get('form_id', ''), 'error': 'No image part in the request'}), 400

    image = request.files['image']
    if not image or image.filename == '':
        return jsonify({"response": '', "form_id": session.get('form_id', ''), 'error': 'No selected image'}), 400

    filename = secure_filename(image.filename)
    if not filename:
        return jsonify({"response": '', "form_id": session.get('form_id', ''), 'error': 'Invalid image filename'}), 400

    if last_image_status_user.get(user_id) == filename:
        print_logs_with_time("Image is the same as the last image", "+" * 20)
        return jsonify({"response": '', "form_id": session.get('form_id', ''), 'error': 'Image already processed'}), 400

    temp_list = [{"role": "user", "parts": (append_current_time('user', user_message))}]
    response = chat_gemini_generate_content_from_image(user_chat_histories.get(user_id, []) + temp_list, image)
    response = handle_form_in_response(response)
    temp_list.append({"role": "model", "parts": append_current_time('model', response)})
    
    save_history(user_id, temp_list, user_chat_histories, STORAGE_TYPE, db, history_dir)
    last_image_status_user[user_id] = filename

    return jsonify({"response": response, "form_id": session.get('form_id', ''), 'user_message': user_message}), 200

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    """
    Handles text-based chat requests. It processes user messages, generates AI responses,
    and manages the conversation history. It also handles form submissions and duplicate messages.
    """
    if not request.is_json:
        print_logs_with_time("Request is not JSON, redirecting to /api/image endpoint")
        return image_endpoint()

    user_id, is_new_user = get_user_id(request, user_chat_histories)
    load_user_history(user_id, user_chat_histories, STORAGE_TYPE, db, history_dir)

    user_message = request.json.get('message', "").strip()
    answers = session.get('answers')

    structured_message_based_on_user_language = {
        'en': 'my answers to your test are',
        'fr': 'mes réponses à votre test sont',
        'ar': 'إجاباتي على اختبارك هي',
    }

    if answers:
        language = answers.get('language', 'en')
        formatted_answers = [f"{k}: {v}" for k, v in answers.items() if k != 'language']
        user_message = f"{structured_message_based_on_user_language.get(language)}:<br>&emsp;➔ {'<br>&emsp;➔ '.join(formatted_answers)}<br>"
        session['answers'] = None

    if not user_message:
        return jsonify({"response": '', "form_id": session.get('form_id', ''), 'user_message': user_message})

    if last_message_user.get(user_id) == user_message:
        print_logs_with_time("User message is the same as the last message", "+" * 20)
        return jsonify({"response": '', "form_id": session.get('form_id', ''), 'user_message': user_message})

    last_message_user[user_id] = user_message
    print_logs_with_time("User message:", user_message)

    temp_list = [{"role": "user", "parts": (append_current_time('user', user_message))}]

    try:
        response = chat_gemini_generate_content(user_chat_histories.get(user_id, []) + temp_list)
        if not response:
            raise Exception("Response is empty")
    except Exception as e:
        print_logs_with_time(f"ERROR while generating content: {e}")
        try:
            response = chat_gemini_send_message(user_chat_histories.get(user_id, []) + temp__list, user_message)
        except Exception as e:
            print_logs_with_time(f"ERROR while sending message: {e}")
            return jsonify({"response": '', "form_id": session.get('form_id', ''), 'error': 'The quota has been reached, Please try again in a minute'}), 400

    if not response or not response.strip():
        return jsonify({"response": '', "form_id": session.get('form_id', ''), 'error': 'The quota has been reached, Please try again in a minute'}), 400

    response = handle_form_in_response(response)

    temp_list.append({"role": "model", "parts": append_current_time('model', response)})
    return save_and_respond_chat(user_id, temp_list, user_chat_histories, STORAGE_TYPE, db, history_dir, is_new_user)

# --- History API Endpoint ---
@app.route('/api/history', methods=['GET'])
def load_history_endpoint():
    """Endpoint to retrieve paginated chat history for a user."""
    user_id = request.args.get("user_id")
    if not user_id or user_id == 'undefined':
        return jsonify({"response": '', "form_id": session.get('form_id', ''), 'error': 'User ID not found'}), 400

    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 2))
        if limit % 2 != 0:
            limit += 1
    except ValueError:
        return make_response(jsonify({"error": "Invalid page or limit parameter. Must be an integer.", "history": [], "page": 1, "limit": 5, "form_id": session.get('form_id', '')}), 400)

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

        resp = make_response(jsonify({"history": paginated_history[::-1], "page": page, "limit": limit, "max_page": max_page, "form_id": session.get('form_id', '')}))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    except Exception as e:
        print_logs_with_time(f"ERROR while loading history: {e}")
        return make_response(jsonify({"error": str(e), "history": [], "page": page, "limit": limit, "max_page": 1, "form_id": session.get('form_id', '')}))

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
    if not data or not all(k in data for k in ['text', 'rating', 'userId']):
        return jsonify({"error": "Missing required feedback data: text, rating, and userId are required"}), 400

    feedback_id = str(ObjectId())
    feedback_doc = {
        "_id": feedback_id,
        "userId": data['userId'],
        "text": data['text'],
        "rating": data['rating'],
        "displayName": data.get('fullName', 'Anonymous'),
        "email": data.get('emailAdress', ''),
        "createdAt": datetime.utcnow().isoformat() + 'Z'
    }

    try:
        if STORAGE_TYPE == 'remote':
            db.submit_feedback(feedback_doc)
        else:
            save_feedback(feedback_doc, feedback_dir)
            feedbacks[feedback_id] = feedback_doc
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
            items, next_cursor = db.get_feedback(cursor, limit)
            for item in items:
                item['_id'] = str(item['_id'])
            return jsonify({"items": items, "nextCursor": next_cursor})
        else:
            sorted_feedbacks = sorted(feedbacks.values(), key=lambda x: x['createdAt'], reverse=True)
            start_index = 0
            if cursor:
                try:
                    start_index = next(i for i, item in enumerate(sorted_feedbacks) if item['_id'] == cursor) + 1
                except StopIteration:
                    return jsonify({"items": [], "nextCursor": None})

            end_index = start_index + limit
            items = sorted_feedbacks[start_index:end_index]
            next_cursor = items[-1]['_id'] if end_index < len(sorted_feedbacks) else None
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
    with user identification for tracking. It also sends an email notification to the teacher.
    """
    data = request.get_json()
    if not data or not all(k in data for k in ['userId', 'fullName', 'emailAddress', 'message']):
        return jsonify({"error": "Missing required fields"}), 400

    if len(data['message'].strip()) < 10:
        return jsonify({"error": "Message must be at least 10 characters long"}), 400

    message_id = str(ObjectId())
    message_doc = {
        "_id": message_id,
        "userId": data['userId'],
        "fullName": data['fullName'],
        "emailAddress": data['emailAddress'],
        "message": data['message'],
        "createdAt": datetime.utcnow().isoformat() + 'Z'
    }

    email_success, email_error = send_teacher_email(data['fullName'], data['emailAddress'], data['message'])
    if not email_success:
        print_logs_with_time(f"ERROR sending email to teacher: {email_error}")
        return jsonify({"error": email_error or "Failed to send email"}), 500

    try:
        if STORAGE_TYPE == 'remote':
            db.submit_teacher_message(message_doc)
        else:
            save_teacher_message(message_doc, contact_teacher_dir)
            teacher_messages[message_id] = message_doc
    except Exception as e:
        print_logs_with_time(f"Email was sent successfully but message storage failed: {e}")

    return jsonify({"success": True, "message": "Your message has been sent to the teacher."}), 201

# --- Utility & Debug Endpoints ---
@app.route('/api/answers', methods=['POST'])
def get_answers():
    """Endpoint to receive and store form answers in the session."""
    session['answers'] = request.get_json() if request.is_json else request.form.copy()
    return chat_endpoint()

@app.route('/api/list_conversations', methods=['GET'])
def list_conversations():
    """Endpoint to list all conversations, requires a password for authorization."""
    if request.args.get('password') != os.getenv('PASSWORD_CONVERSATIONS'):
        return jsonify({'error': 'Unauthorized'}), 401

    if STORAGE_TYPE == 'remote':
        return jsonify(db.get_conversations_list())

    if os.path.exists(history_dir):
        files = os.listdir(history_dir)
        files_with_time = [(file, datetime.fromtimestamp(os.path.getmtime(os.path.join(history_dir, file))), f"{os.path.getsize(os.path.join(history_dir, file)) / 1024:.2f} KB") for file in files]
        files_sorted = sorted(files_with_time, key=lambda x: x[1], reverse=True)
        return jsonify(files_sorted)
    return jsonify([])

@app.route('/api/list_conversations/<conversation_id>', methods=['GET'])
def conversation(conversation_id):
    """Endpoint to retrieve a specific conversation by its ID, requires a password."""
    if request.args.get('password') != os.getenv('PASSWORD_CONVERSATIONS'):
        return jsonify({'error': 'Unauthorized'}), 401

    if conversation_id in user_chat_histories:
        conversation_history = user_chat_histories[conversation_id].copy()
        conversation_history.reverse()
        return jsonify(conversation_history)

    return jsonify({'error': 'Conversation ID not found'}), 404

@app.route("/api/test/<value>", methods=["GET"])
def test(value: str = "error"):
    """A simple test endpoint to verify server status."""
    if value.lower() == "ok":
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "error": "Invalid value"}), 400

# --- Error Handlers ---
@app.errorhandler(404)
def not_found(e):
    """Handles 404 Not Found errors."""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    """Handles 500 Internal Server Error."""
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    """Handles all other exceptions."""

    print_logs_with_time(f"Unhandled exception: {e}")
    return jsonify({"error": str(e)}), 500

@app.errorhandler(400)
def bad_request(e):
    """Handles 400 Bad Request errors."""
    return jsonify({"error": "Bad request"}), 400

# --- Main Execution Block ---
if __name__ == '__main__':
    AI_DEBUG = os.getenv('AI_DEBUG', 'False').lower() in ('true', '1', 't')
    app.run(debug=AI_DEBUG, host='0.0.0.0', port=5002)
