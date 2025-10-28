# -*- coding: utf-8 -*-

import os
from datetime import timedelta
from flask import Flask
from flask_cors import CORS
from flask_compress import Compress
from dotenv import load_dotenv

from database import Database
from tools.utils import (
    load_all_feedback,
    load_all_teacher_messages,
    load_chat_history_startup,
)

# --- App Initialization and Configuration ---
load_dotenv()

app = Flask(__name__)
Compress(app)

app.config.update(
    COMPRESS_MIN_SIZE=500,
    COMPRESS_LEVEL=9,
    COMPRESS_ALGORITHM='gzip',
    COMPRESS_MIMETYPES=['application/json'],
    SECRET_KEY=os.getenv('SECRET_KEY'),
    PERMANENT_SESSION_LIFETIME=timedelta(days=365),
    SESSION_COOKIE_DOMAIN='.drihmia.me',
    SESSION_COOKIE_NAME='session',
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_SECURE=True,
)

CORS(
    app,
    origins=[
        "https://ai.drihmia.me",
        "http://localhost:3000",
    ],
    supports_credentials=True,
)

# --- Storage and Database Initialization ---
STORAGE_TYPE = os.getenv('STORAGE_TYPE', 'local')
db = None
if STORAGE_TYPE == 'remote':
    print("Using remote MongoDB storage")
    db = Database(os.environ.get("MONGO_URI"))

history_dir = 'chat_histories/'
feedback_dir = 'feedbacks/'
contact_teacher_dir = 'contact_teacher/'

user_chat_histories = {}
feedbacks = {}
teacher_messages = {}
last_message_user = {}
last_image_status_user = {}

# --- Initial Data Loading ---
if STORAGE_TYPE == 'remote':
    if db:
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
