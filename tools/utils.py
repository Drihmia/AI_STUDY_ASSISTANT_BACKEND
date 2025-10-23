import os
import json
from zoneinfo import ZoneInfo
from datetime import datetime
from tools.chat_utils import update_time_in_time_tag

# Function to load chat histories for a specific user
def load_chat_history(user_id, history_dir="chat_histories"):
    user_history_file = os.path.join(history_dir, f"history_{user_id}.json")
    if os.path.exists(user_history_file):
        try:
            with open(user_history_file, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except json.JSONDecodeError:
            print(f"Error loading chat history for user {user_id}.")
    return []

# Function to save chat histories to a user-specific file
def save_chat_history(user_chat_histories_user, user_id, history_dir="chat_histories"):
    user_history_file = os.path.join(history_dir, f"history_{user_id}.json")
    with open(user_history_file, 'w', encoding='utf-8') as json_file:
        try:
            json.dump(user_chat_histories_user, json_file, indent=4)
        except json.JSONDecodeError:
            print(f"Error saving chat history for user {user_id}.")
            return
    print(f"Chat history for user {user_id} saved successfully.")

def load_all_feedback(feedback_dir="feedbacks/"):
    """
    Loads all feedback from the local file system.
    """
    feedbacks = {}
    if not os.path.exists(feedback_dir):
        os.makedirs(feedback_dir)
    else:
        for filename in os.listdir(feedback_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(feedback_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        feedback_data = json.load(f)
                        feedbacks[feedback_data['_id']] = feedback_data
                except (json.JSONDecodeError, KeyError) as e:
                    print_logs_with_time(f"ERROR loading feedback from {filename}: {e}")
    return feedbacks

def save_feedback(feedback_doc, feedback_dir="feedbacks/"):
    """
    Saves a single feedback document to a local JSON file.
    """
    feedback_id = feedback_doc['_id']
    filepath = os.path.join(feedback_dir, f"{feedback_id}.json")
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(feedback_doc, f, indent=4)
        print(f"Feedback {feedback_id} saved successfully.")
    except Exception as e:
        print_logs_with_time(f"ERROR saving feedback locally: {e}")
        raise

def load_all_teacher_messages(messages_dir="contact_teacher/"):
    """
    Loads all teacher messages from the local file system.
    """
    messages = {}
    if not os.path.exists(messages_dir):
        os.makedirs(messages_dir)
    else:
        for filename in os.listdir(messages_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(messages_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        message_data = json.load(f)
                        messages[message_data['_id']] = message_data
                except (json.JSONDecodeError, KeyError) as e:
                    print_logs_with_time(f"ERROR loading teacher message from {filename}: {e}")
    return messages

def save_teacher_message(message_doc, messages_dir="contact_teacher/"):
    """
    Saves a single teacher message document to a local JSON file.
    """
    message_id = message_doc['_id']
    filepath = os.path.join(messages_dir, f"{message_id}.json")
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(message_doc, f, indent=4)
        print(f"Teacher message {message_id} saved successfully.")
    except Exception as e:
        print_logs_with_time(f"ERROR saving teacher message locally: {e}")
        raise


# Register signal handler for graceful shutdown
def handle_signal(signal, frame, user_chat_histories):
    print("\nSaving chat histories before shutdown...")
    for user_id in user_chat_histories.keys():
        save_chat_history(user_chat_histories[user_id], user_id)
    sys.exit(0)

def load_chat_history_startup(user_chat_histories, history_dir="chat_histories"):
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)
    else:
        files = os.listdir(history_dir)
        for file in files:
            if ".json" in file and "history" in file:
                user_id = file.split('_', 1)[-1].split('.')[0]
                user_chat_histories[user_id] = load_chat_history(user_id, history_dir=history_dir)
    print("Number of chat histories loaded:", len(user_chat_histories))
    return user_chat_histories

def get_time_zone_name(time_zone):
    try:
        return ZoneInfo(time_zone)
    except Exception as e:
        print("get_time_zone_name",e)
        return "UTC"

def get_current_time(time_zone='Africa/Casablanca', date_object=False):
    try:
        hold = get_time_zone_name(time_zone)
        if date_object:
            return datetime.now(hold)
        return datetime.now(hold).strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print("get_current_time", e)
        if date_object:
            return datetime.now()
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def append_current_time(role, message):
    current_time = get_current_time("Africa/Casablanca")
    if role.lower() == "user":
        if ('<time>' in message) or ('<time ' in message):
            return update_time_in_time_tag(message, current_time)
        return update_time_in_time_tag(f'<p>{message}</p><br><time>{current_time}</time>', current_time)
    else:
        if ('<time>' in message) or ('<time ' in message):
            return update_time_in_time_tag(message, current_time)
        return update_time_in_time_tag(f'{message}<br><time>{current_time}</time>', current_time)

def print_logs_with_time(*message):
    print(f"[{get_current_time('Africa/Casablanca')}]", *message)


if __name__ == "__main__":
    print("This is a utility module. It is not meant to be executed directly.")
