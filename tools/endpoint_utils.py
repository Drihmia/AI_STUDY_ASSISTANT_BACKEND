# -*- coding: utf-8 -*-
"""
Utility functions for handling chat and image endpoints.
"""

import os
from uuid import uuid4
from threading import Thread
from flask import session, make_response, jsonify, request
from datetime import datetime, timedelta

from tools.utils import (
    load_chat_history,
    save_chat_history,
)

def get_user_id(request, user_chat_histories):
    """
    Retrieves the user ID from the request arguments or cookies, or generates a new one.

    Args:
        request: The Flask request object.
        user_chat_histories (dict): A dictionary of user chat histories.

    Returns:
        A tuple containing the user ID (str) and a boolean indicating if the user is new.
    """
    user_id = request.args.get('user_id')
    if not user_id or user_id == 'undefined':
        user_id = request.cookies.get('user_id')
    
    is_new_user = not user_id
    if is_new_user:
        user_id = str(len(user_chat_histories)) + '_' + str(uuid4())
        
    return user_id, is_new_user

def load_user_history(user_id, user_chat_histories, storage_type, db, history_dir):
    """
    Loads the chat history for a given user if it's not already in memory.

    Args:
        user_id (str): The ID of the user.
        user_chat_histories (dict): The dictionary of in-memory chat histories.
        storage_type (str): The storage type ('remote' or 'local').
        db: The database instance for remote storage.
        history_dir (str): The directory for local history files.
    """
    if user_id not in user_chat_histories:
        if storage_type == 'remote':
            user_chat_histories[user_id] = db.get_history(user_id)
        else:
            user_chat_histories[user_id] = load_chat_history(user_id, history_dir)

def save_history(user_id, temp_list, user_chat_histories, storage_type, db, history_dir):
    """
    Extends the user's chat history with new messages and saves it in a background thread.

    Args:
        user_id (str): The user's ID.
        temp_list (list): The list of new messages to add.
        user_chat_histories (dict): The dictionary containing all user histories.
        storage_type (str): 'remote' or 'local'.
        db: The database object for remote storage.
        history_dir (str): The directory for local storage.
    """
    if user_id not in user_chat_histories:
        user_chat_histories[user_id] = []
    user_chat_histories[user_id].extend(temp_list)

    if storage_type == 'remote':
        Thread(target=db.add_messages, args=(user_id, temp_list), daemon=True).start()
    else:
        # Ensure the full, updated history is saved
        full_history = user_chat_histories[user_id]
        Thread(target=save_chat_history, args=(full_history, user_id, history_dir), daemon=True).start()

def save_and_respond_chat(user_id, temp_list, user_chat_histories, storage_type, db, history_dir, is_new_user):
    """
    Saves chat history and returns a JSON response, setting a cookie for new users.

    Args:
        user_id (str): The user's ID.
        temp_list (list): A list of new messages [user_message, model_response].
        user_chat_histories (dict): Dictionary of all user histories.
        storage_type (str): The storage type ('remote' or 'local').
        db: The database instance for remote storage.
        history_dir (str): The directory for local history files.
        is_new_user (bool): Flag indicating if this is a new user.

    Returns:
        Flask.Response: The JSON response object, possibly with a new user cookie.
    """
    save_history(user_id, temp_list, user_chat_histories, storage_type, db, history_dir)

    response_data = {
        "response": temp_list[1].get('parts', 'something went wrong'),
        "form_id": session.get('form_id', ''),
        "user_message": temp_list[0].get('parts', 'something went wrong')
    }
    
    resp = make_response(jsonify(response_data))

    if is_new_user:
        expire_date = datetime.now() + timedelta(days=365)
        resp.set_cookie(
            'user_id',
            value=user_id,
            domain='.drihmia.me',
            secure=True,
            httponly=True,
            samesite='Lax',
            expires=expire_date
        )
    return resp
