import os
from pymongo import MongoClient
from bson import BSON

class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        print("Client:", self.client)
        self.db = self.client[os.environ.get("MONGO_DB_NAME", "chat_history")]
        print("DB:", self.db)
        self.collection = self.db[os.environ.get("MONGO_COLLECTION_NAME", "history")]
        print("Collection:", self.collection)

    def get_history(self, user_id):
        """
        Retrieves the chat history for a given user_id.
        """
        history = self.collection.find_one({"_id": user_id})
        print("get_history:", history)
        if history:
            return history["messages"]
        return []

    def add_messages(self, user_id, messages):
        """
        Adds multiple messages to the chat history for a given user_id.
        """
        self.collection.update_one(
            {"_id": user_id},
            {"$push": {"messages": {"$each": messages}}},
            upsert=True
        )

    def get_all_histories(self):
        """
        Retrieves all chat histories from the collection.
        """
        histories = self.collection.find()
        user_chat_histories = {}
        for history in histories:
            print("get_all_histories:", history)
            user_chat_histories[history["_id"]] = history["messages"]
        return user_chat_histories

    def get_conversations_list(self):
        """
        Retrieves a list of all conversations with metadata.
        """
        pipeline = [
            {
                "$project": {
                    "_id": 1,
                    "last_message_time": {
                        "$let": {
                            "vars": {
                                "last_message": {"$arrayElemAt": ["$messages", -1]}
                            },
                            "in": "$$last_message.parts"
                        }
                    },
                    "size_kb": {"$divide": ["$bsonSize", 1024]}
                }
            }
        ]
        conversations = list(self.collection.aggregate(pipeline))
        
        # Extract the time from the <time> tag in last_message_time
        for conv in conversations:
            time_tag_str = conv.get('last_message_time', '')
            # Basic parsing, can be improved with regex for robustness
            if '<time>' in time_tag_str:
                start = time_tag_str.find('<time>') + len('<time>')
                end = time_tag_str.find('</time>')
                if end == -1: # Handle self-closing tags if any
                    end = time_tag_str.find('/>')
                if start != -1 and end != -1:
                     conv['last_message_time'] = time_tag_str[start:end].strip()
                else:
                    conv['last_message_time'] = '' # Set as empty if not found

            conv['size_kb'] = f"{conv['size_kb']:.2f} KB"


        # Sort by last message time
        conversations.sort(key=lambda x: x.get('last_message_time', ''), reverse=True)
        return [(c['_id'], c['last_message_time'], c['size_kb']) for c in conversations]
