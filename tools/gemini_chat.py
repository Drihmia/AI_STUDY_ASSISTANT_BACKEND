import google.generativeai as genai
import os
from system_prompt import system_prompt_parts
from time import sleep
from tools.utils import (get_current_time,
                         print_logs_with_time,
                         )
import datetime

# System prompt for the Gemini model
system_prompt = {
    "role": "user",
    "parts": system_prompt_parts
}

# Load the API key from the environment
api_key_gimini = os.environ.get("GEMINI_API_KEY")
if not api_key_gimini:
    print("Please set the GEMINI_API_KEY environment variable.")
    sys.exit(1)

def gemini_model(system_messages: dict, api_key: str, model_name: str) -> genai.GenerativeModel:
    """
    Create a Gemini model
    """

    print("!"*30, f"Model name: {model_name}", "!"*30)
    client_gemini = genai.configure(api_key=api_key)
    model=genai.GenerativeModel(
        model_name=model_name,
        system_instruction=system_messages.get("parts"),
        generation_config={
            "top_p": 0.98,
            "temperature": 0.5,
            "response_mime_type": "text/plain"
        },
    )

    return model

# Create the Gemini model
_gemini_model_send_message = gemini_model(system_prompt, api_key_gimini, "gemini-2.0-flash-exp")

_gemini_model_generate_content = gemini_model(system_prompt, api_key_gimini, "gemini-2.0-flash-thinking-exp-01-21")

def chat_gemini_send_message(system_messages: dict, message: str) -> str:
    """
    Chat with the Gemini API
    """

    # response = _gemini_model.generate_content(system_messages).text.strip()
    try:
        chat_session = _gemini_model_send_message.start_chat(history=system_messages)
        response = chat_session.send_message(message).text.strip()
        response = response.removeprefix("```html").removesuffix("```").strip()
        print("*"*30, "response from gemini send message", "*"*30)
        return '\n' + response
    except Exception as e:
        print("Error creating the Gemini model (send message) sleep 20s :", e)
        print("*"*50, "chat sleeping for 20s\n")
        sleep(20)
        # print("*"*50, "recursive call to chat_gemini_send_message\n")
        # chat_gemini_send_message(system_messages, message)
        # if "429 Resource has been exhausted" in str(e):
            # raise Exception("Gemini API rate limit exceeded. Please try again later. (send message)")
    return '\n'

def chat_gemini_generate_content(system_messages: dict) -> str:
    """
    Chat with the Gemini API
    """

    start = get_current_time(date_object=True)
    try:
        response = _gemini_model_generate_content.generate_content(system_messages).text.strip()
        response = response.removeprefix("```html").removesuffix("```").strip()
        print("*"*30, "response from gemini generate content", "*"*30)

        end = get_current_time(date_object=True)
        print_logs_with_time(f"Response time: {end - start}")
        return '\n' + response
    except Exception as e:
        print("Error creating the Gemini model (generat content) sleep 20s :", e)
        print("*"*50, "content sleeping for 20s\n")
        sleep(20)
        print("*"*50, "recursive call to chat_gemini_generate_content\n")
        chat_gemini_generate_content(system_messages)
        # if "429 Resource has been exhausted" in str(e):
            # raise Exception("Gemini API rate limit exceeded. Please try again later. (generate content)")
