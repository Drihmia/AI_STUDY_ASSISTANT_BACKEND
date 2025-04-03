import os
import json
from zoneinfo import ZoneInfo
from datetime import datetime
from tools.chat_utils import update_time_in_time_tag



# Function to load chat histories for a specific user
def load_chat_history(user_id, history_dir="chat_histories"):
    user_history_file = os.path.join(history_dir, f"history_{user_id}.json")
    # print("loading user history from:", user_history_file)
    if os.path.exists(user_history_file):
        try:
            with open(user_history_file, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except json.JSONDecodeError:
            # print("-"*40)
            print(f"Error loading chat history for user {user_id}.")
            # print("-"*40)

    return []  # Return initial prompt if no history exists


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

# Register signal handler for graceful shutdown (e.g., when Ctrl+C or Ctrl+D is pressed)
def handle_signal(signal, frame, user_chat_histories):
    print("\nSaving chat histories before shutdown...")
    for user_id in user_chat_histories.key():
        save_chat_history(user_id)
    sys.exit(0)

def load_chat_history_startup(user_chat_histories, history_dir="chat_histories"):
    # Load the chat histories on server startup
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)
    else:
        files = os.listdir(history_dir)
        for file in files:
            if ".json" in file and "history" in file:
                user_id = file.split('_', 1)[-1].split('.')[0]
                # print("loading chat history for user:", user_id)
                user_chat_histories[user_id] = load_chat_history(user_id, history_dir=history_dir)

    print("Number of chat histories loaded:", len(user_chat_histories), "*"*30)
    # for chat in user_chat_histories:
        # print(f"User {chat} has {len(user_chat_histories[chat])} messages in their chat history.")

    return user_chat_histories


def get_time_zone_name(time_zone):
    """
    Get the time zone name from the time zone key
    Args: time_zone: The time zone key
    Return: The time zone name
    """

    try:
        return ZoneInfo(time_zone)
    except Exception as e:
        print("get_time_zone_name",e)
        return "UTC"

def get_current_time(time_zone='Africa/Casablanca', date_object=False):
    """
    Get the current time in the specified time zone
    Args: time_zone: The time zone key
    Return: The current time in the specified time zone
    """

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
    """
    append the current time to the message to:
        user: user messsage will be included in a <p> tag and the time will be included in a <time> tag
        AI Model: AI Model HTML message is html already so the time will be included in a <time> tag
    Args: role: The role of the message sender
          message: The message to append the current time to it
    Return: The message with the current time appended to it
    """

    current_time = get_current_time("Africa/Casablanca")
    if role.lower() == "user":
        if ('<time>' in message) or ('<time ' in message):
            return update_time_in_time_tag(message, current_time)
        return update_time_in_time_tag(f'<p>{message}</p><br><time>{current_time}</time>', current_time)
    else:
        if ('<time>' in message) or ('<time ' in message):
            return update_time_in_time_tag(message, current_time)
        return update_time_in_time_tag(f'{message}<br><time>{current_time}</time>', current_time)


# Should take ..args and print them with the current time
def print_logs_with_time(*message):
    """
    Print a message with the current time
    Args: message: The message to print
    """

    print(f"[{get_current_time('Africa/Casablanca')}]", *message)


if __name__ == "__main__":
    # print("This is a utility module. It is not meant to be executed directly.")
    # print("get_time_zone_name", "Africa/Casablanca:", get_time_zone_name("Africa/Casablanca"))
    print("get_current_time", "Africa/Casablanca:", get_current_time("Africa/Casablanca"))
