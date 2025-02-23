import google.generativeai as genai
import os
from system_prompt import system_prompt_parts
from IPython.display import HTML

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

def gemini_model(system_messages: dict, api_key: str, model_name) -> genai.GenerativeModel:
    """
    Create a Gemini model
    """

    client_gemini = genai.configure(api_key=api_key)
    model=genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
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
        return '\n' + response
    except Exception as e:
        print("Error creating the Gemini model:", e)
    return '\n'

def chat_gemini_generate_content(system_messages: dict) -> str:
    """
    Chat with the Gemini API
    """


    try:
        response = _gemini_model_generate_content.generate_content(system_messages).text.strip()
        response = response.removeprefix("```html").removesuffix("```").strip()
        return '\n' + response
    except Exception as e:
        print("Error creating the Gemini model:", e)
    return '\n'
