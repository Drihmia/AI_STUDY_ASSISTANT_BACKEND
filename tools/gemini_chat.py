import google.generativeai as genai
import os
from system_prompt import system_prompt_parts

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

def gemini_model(system_messages: dict, api_key: str) -> genai.GenerativeModel:
    """
    Create a Gemini model
    """

    client_gemini = genai.configure(api_key=api_key)
    model=genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_messages.get("parts"),
    )

    return model

# Create the Gemini model
_gemini_model = gemini_model(system_prompt, api_key_gimini)

def chat_gemini(system_messages: dict) -> str:
    """
    Chat with the Gemini API
    """

    response = _gemini_model.generate_content(system_messages).text.strip()
    return '\n' + response.removeprefix("```html").removesuffix("```").strip()
