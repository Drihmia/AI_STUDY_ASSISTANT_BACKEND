import os
from pymongo import MongoClient, DESCENDING
from bson import BSON
from bson.objectid import ObjectId

class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        print("Client:", self.client)
        self.db = self.client[os.environ.get("MONGO_DB_NAME", "chat_history")]
        print("DB:", self.db)
        self.collection = self.db[os.environ.get("MONGO_COLLECTION_NAME", "history")]
        print("Collection:", self.collection)
        # Add a new collection for feedback
        self.feedback_collection = self.db[os.environ.get("MONGO_FEEDBACK_COLLECTION_NAME", "feedback")]
        print("Feedback Collection:", self.feedback_collection)

    def get_history(self, user_id):
        """
        Retrieves the chat history for a given user_id.
        """
        history = self.collection.find_one({"_id": user_id})
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
                    "size_kb": {"$divide": [{"$$bsonsize": "$$ROOT"}, 1024]}
                }
            }
        ]
        conversations = list(self.collection.aggregate(pipeline))
        
        for conv in conversations:
            time_tag_str = conv.get('last_message_time', '')
            if '<time>' in time_tag_str:
                start = time_tag_str.find('<time>') + len('<time>')
                end = time_tag_str.find('</time>')
                if start != -1 and end != -1:
                     conv['last_message_time'] = time_tag_str[start:end].strip()
                else:
                    conv['last_message_time'] = ''

            conv['size_kb'] = f"{conv['size_kb']:.2f} KB"

        conversations.sort(key=lambda x: x.get('last_message_time', ''), reverse=True)
        return [(c['_id'], c['last_message_time'], c['size_kb']) for c in conversations]

    # START: NEW FEEDBACK METHODS
    def submit_feedback(self, feedback_doc):
        """
        Inserts a feedback document into the feedback collection.
        The _id is expected to be a string representation of an ObjectId.
        """
        try:
            # The _id from chat.py is a string, which is fine.
            self.feedback_collection.insert_one(feedback_doc)
        except Exception as e:
            print(f"Error inserting feedback: {e}")
            raise

    def get_feedback(self, cursor=None, limit=10):
        """
        Retrieves feedback from the collection with cursor-based pagination.
        Sorts by createdAt descending.
        """
        query = {}
        if cursor:
            try:
                # We query for documents created before the cursor's timestamp.
                # The cursor is the `createdAt` field of the last item from the previous page.
                query['createdAt'] = {'$lt': cursor}
            except Exception as e:
                print(f"Error processing cursor: {e}")
                return [], None

        # Sort by createdAt descending to get the most recent feedback first
        items = list(self.feedback_collection.find(query).sort('createdAt', DESCENDING).limit(limit))

        next_cursor = None
        if len(items) == limit:
            # The `createdAt` of the last item is the cursor for the next page
            next_cursor = items[-1]['createdAt']
        
        return items, next_cursor
    # END: NEW FEEDBACK METHODS
