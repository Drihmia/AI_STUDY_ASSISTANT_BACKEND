import os
import json


# Function to load chat histories for a specific user
def load_chat_history(user_id, history_dir="chat_histories"):
    user_history_file = os.path.join(history_dir, f"history_{user_id}.json")
    print("loading user history from:", user_history_file)
    if os.path.exists(user_history_file):
        try:
            with open(user_history_file, 'r') as json_file:
                return json.load(json_file)
        except json.JSONDecodeError:
            print("-"*40)
            print(f"Error loading chat history for user {user_id}.")
            print("-"*40)

    return []  # Return initial prompt if no history exists


# Function to save chat histories to a user-specific file
def save_chat_history(user_chat_histories, user_id, history_dir="chat_histories"):
    user_history_file = os.path.join(history_dir, f"history_{user_id}.json")
    with open(user_history_file, 'w') as json_file:
        try:
            json.dump(user_chat_histories[user_id], json_file, indent=4)
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
                print("loading chat history for user:", user_id)
                user_chat_histories[user_id] = load_chat_history(user_id, history_dir=history_dir)

    print("Number of chat histories loaded:", len(user_chat_histories))
    for chat in user_chat_histories:
        print(f"User {chat} has {len(user_chat_histories[chat])} messages in their chat history.")

    return user_chat_histories


