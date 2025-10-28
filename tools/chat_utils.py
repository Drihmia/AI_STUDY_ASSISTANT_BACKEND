# -*- coding: utf-8 -*-
"""This module contains utility functions for chat processing."""

import random
import string
from uuid import uuid4
from re import sub
from flask import session
from bs4 import BeautifulSoup

from tools.log import print_logs_with_time
from tools.utils import get_current_time

def generate_random_string(length=32):
    """Generates a random string of a given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def update_form_with_unique_ids(form_html):
    """
    Parses an HTML string to find all form-related elements (input, select, textarea, button)
    and adds a unique ID to each element that doesn't already have one.

    Args:
        html_content (str): The HTML content of the form.

    Returns:
        str: The modified HTML content with unique IDs added to form elements.
    """
    if not form_html:
        return ""

    soup = BeautifulSoup(form_html, 'html.parser')
    form_elements = soup.find_all(['input', 'textarea', 'select', 'button'])

    for element in form_elements:
        old_id = element.get('id')
        if not old_id:
            continue

        unique_id = generate_random_string()
        element['id'] = unique_id

        label = soup.find('label', {'for': old_id})
        if label:
            label['for'] = unique_id
            
    return str(soup)

def handle_form_in_response(response):
    """
    Checks for a form in the response, replaces its ID with a unique one,
    and updates the session with the new form ID.

    Args:
        response (str): The HTML response content from the model.

    Returns:
        str: The modified response with the updated form.
    """
    if '<form ' in response:
        random_string = '-' + str(uuid4())
        pattern = r'(<form\s+[^>]*id=")[^"]*(")'
        replacement = rf'\1{random_string}\2'
        
        try:
            response = sub(pattern, replacement, response)
            response = update_form_with_unique_ids(response)
        except Exception as e:
            print_logs_with_time(f"ERROR while replacing the form id: {e}")
            error_message = (
                "Sorry, there was an error with this form. "
                "Please communicate with us using this code: "
            )
            response = f"{response}\n\n{error_message}{random_string}"
        
        session['form_id'] = random_string
        
    return response

def update_time_in_time_tag(message, time):
    """Updates the time attribute in all time tags in the given HTML message."""
    soup = BeautifulSoup(message, 'html.parser')
    time_tags = soup.find_all('time')

    for time_tag in time_tags:
        time_tag.string = time
        if time_tag.has_attr('dir'):
            del time_tag['dir']
        if (not time_tag.previous_sibling or time_tag.previous_sibling.name != "br"):
            br_tag = soup.new_tag("br")
            time_tag.insert_before(br_tag)

    return str(soup)

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
