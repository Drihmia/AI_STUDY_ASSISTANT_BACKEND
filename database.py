import os
from pymongo import MongoClient

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
