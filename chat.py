import os
import sys
import json
from flask import Flask, request, jsonify, make_response
from dotenv import load_dotenv
import signal
from uuid import uuid4
import google.generativeai as genai


load_dotenv()


app = Flask(__name__)
model_name = os.environ.get("MODEL_NAME")

geometry_TC_PC = """
Géométrie de quelques molécules

I – Règles du DUET et de l’OCTET :

Activité : L'hélium (He, Z = 2), le néon (Ne, Z = 10) et l'argon (Ar, Z = 18) sont des éléments qui existent naturellement sous forme d'atomes isolés. Ce sont des gaz nobles, inertes chimiquement, car leurs couches externes sont saturées.

a. Structure électronique des éléments :

He : (K)₂
Ne : (K)₂ (L)₈
Ar : (K)₂ (L)₈ (M)₈
b. La couche externe de chaque atome est-elle saturée ? La couche externe de ces atomes est saturée, car elle contient le nombre maximal d'électrons autorisé par couche.

c. Structure électronique de lithium (Li, Z = 3) et chlore (Cl, Z = 17) :

Li : (K)₂ (L)₁
Cl : (K)₂ (L)₈ (M)₇ Ces deux atomes sont instables, car leurs couches externes ne sont pas saturées.
d. Structure électronique des ions Li⁺ et Cl⁻ :

Li⁺ : (K)₂
Cl⁻ : (K)₂ (L)₈ (M)₈ Ces ions sont stables car leurs couches externes sont saturées.
Stabilité des gaz rares : Les gaz rares (Hélium, Néon, Argon, etc.) ne participent quasiment pas à des réactions chimiques, car leur couche externe est saturée. Ils sont stables sous forme d'atomes isolés.

Énoncé des règles :

Règle du DUET : Les éléments de numéro atomique Z ≤ 4 ont une structure électronique similaire à celle de l'hélium (He : (K)₂), avec deux électrons dans leur couche externe.
Règle de l’OCTET : Les éléments de numéro atomique 5 ≤ Z ≤ 18 tendent à acquérir une structure électronique similaire à celle des gaz rares (Ne, Ar), avec huit électrons dans leur couche externe.
Application aux ions monoatomiques stables : Les ions monoatomiques stables suivent les règles du duet et de l'octet :

leur structure électronique est similaire à celle des gaz rares ;
la structure électronique au-dessous est appelle equalement la configuration électronique, la repartition des électrons dans les couches électroniques.
Li⁺ : (K)₂, Li : (K)₂ (L)₁
Na⁺ : (K)₂ (L)₈, Na : (K)₂ (L)₈ (M)₁
Be²⁺ : (K)₂, Be : (K)₂ (L)₂
Mg²⁺ : (K)₂ (L)₈, Mg : (K)₂ (L)₈ (M)₂
F⁻ : (K)₂ (L)₈, F : (K)₂ (L)₇
S²⁻ : (K)₂ (L)₈ (M)₈, S : (K)₂ (L)₈ (M)₆
O²⁻ : (K)₂ (L)₈, O : (K)₂ (L)₆
Cl⁻ : (K)₂ (L)₈ (M)₈, Cl : (K)₂ (L)₈ (M)₇
II – Les molécules :

Définition : Une molécule est un ensemble d'atomes reliés entre eux par des liaisons chimiques. Elle est stable et électriquement neutre.

Liaison covalente : Une liaison covalente se forme lorsque deux atomes partagent un ou plusieurs électrons de leurs couches externes. Cela crée un doublet d'électrons qui lie les deux atomes.

Exemples de la structure électronique des molécules :

Hydrogène (H, Z = 1) : (K)₁, monovalent.
Oxygène (O, Z = 8) : (K)₂ (L)₆, bivalent.
Azote (N, Z = 7) : (K)₂ (L)₅, trivalent.
Carbone (C, Z = 6) : (K)₂ (L)₄, tétravalent.
Représentation de Lewis : La représentation de Lewis d'une molécule montre les atomes et les paires d'électrons liants et non liants. Voici la méthode pour la déterminer :

Écrire la structure électronique de chaque atome.
Déterminer le nombre total d'électrons de couches externes.
Déterminer le nombre total de doublets d'électrons.
Déterminer le nombre de liaisons covalentes pour chaque atome en fonction de la règle du duet ou de l'octet.
Exemple : Représenter selon le modèle de Lewis les molécules PCl₃, H₂O, CH₄, C₂H₄O₂.

III – Isomères :

Types de formules :

Formule brute : Indique le nombre et le type des atomes dans la molécule.
Formule semi-développée : Indique les liaisons entre atomes principaux.
Formule développée : Formule détaillée en supprimant les paires d'électrons non liants.
Isomère : Les isomères sont des molécules qui ont la même formule brute mais différentes structures ou propriétés. Exemple : C₃H₈O.

IV – Géométrie des molécules :

Géométrie spatiale des molécules : La disposition spatiale des atomes est influencée par la répulsion entre les doublets d'électrons. Les atomes sont disposés de manière à être le plus éloignés possible.

Exemples :

CH₄ : tétraédrique
NH₃ : pyramide
H₂O : coudée (V)
CO₂ : linéaire

"""


system_prompt = {
    "role": "user",
    "parts": f"""never use a language but French or English, or arabic and Darija Maroccan aslo
each msg should be in a single language

if you respond in Marocain Darija or arabic, You must use arabic characters only.
IF A response in Marocain Darija or arabic, It should contains only arabic characters.
Never use latin characters in Marocain Darija or arabic responses.


You are a helpful assistant. For the first question, ask the student in both French and English, or arabic and Darija MArocain aslo, which language they prefer to use. Whichever language is chosen, always respond in that language and try to understand anything they say in any language unless the student changes it. Always ask the student's age to determine the level of depth to provide:

14-15 years: common core in Morocco
16-17 years: first year of baccalaureate (ask for the specialty: experimental sciences or mathematical sciences)
17 years and older: baccalaureate (experimental sciences: PC and SVT options, mathematical sciences: options A and B)
Then, ask which subject the student wants to know more about (physics or chemistry), and specify the course or lesson. Be stricter in case of scientific errors and put more effort into responding to scientific questions. When asking the student's age, also ask if they want a spell check of their French or if they want to learn in English as an exception if he/she has not chosen Maroccan Darija. Never ask more than one question per prompt. respond to the student formatted in HTML.

Be short in your answers and only reponse of what is being asked, and respect the above rules.
    IF students responded for age between 14-15 years:
        if the chimestry lesson called "Géometrie de quelques molécules" (Geometry of some molecules):
            Apply THIS: ${(geometry_TC_PC)}
            IMPORTANT NOTE: Any thing related to this lesson should be in French and the answers should from the above text only.

tranlate the above rules into english:
1. The mass must be in Kg in physics and in g in chemistry.
2. the distance in meter.
3. the angles in radian or degree.
4. the volumes in cubic meter.
5. the pressures in pascal or bar or atm.
6. the energies in Joule.
7. the temperatures in Kelvin for 1bac or more or Celsius for all.
8. the forces in Newton.
9. the powers in Watt.
10. the charges in Coulomb.
11. the tensions in Volt.
12. the capacities in Farad.
13. the resistances in Ohm.
13. the intensities in Ampere.
14. the frequencies in Hertz.
15. the magnetic fields in Tesla.


Use only the above units of measure and respect the above rules.
"""
}


# Gemini API
api_key_gimini = os.environ.get("GEMINI_API_KEY")
# print("Gemini api key:", api_key_gimini)
client_gemini = genai.configure(api_key=api_key_gimini)
model=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt.get("parts"),
)



# Dictionary to store chat histories for each user (identified by cookies)
user_chat_histories = {}

# Path to the directory where chat histories are saved
history_dir = 'chat_histories/'

# Function to load chat histories for a specific user
def load_chat_history(user_id):
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
def save_chat_history(user_id):
    user_history_file = os.path.join(history_dir, f"history_{user_id}.json")
    with open(user_history_file, 'w') as json_file:
        try:
            json.dump(user_chat_histories[user_id], json_file, indent=4)
        except json.JSONDecodeError:
            print(f"Error saving chat history for user {user_id}.")
            return

    print(f"Chat history for user {user_id} saved successfully.")

# Register signal handler for graceful shutdown (e.g., when Ctrl+C or Ctrl+D is pressed)
def handle_signal(signal, frame):
    print("\nSaving chat histories before shutdown...")
    for user_id in user_chat_histories:
        save_chat_history(user_id)
    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handle_signal)

# Register the signal handler for SIGINT (Ctrl+D)
signal.signal(signal.SIGTERM, handle_signal)

# Load the chat histories on server startup
if not os.path.exists(history_dir):
    os.makedirs(history_dir)


def chat_gemini(system_messages):
    """
    Chat with the Gemini API
    """

    response = model.generate_content(system_messages).text.strip()
    print("*"*40)
    return '\n' + response.removeprefix("```html").removesuffix("```").strip()


@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    # Get the user message from the request
    user_message = request.json.get('message')

    # Get the user ID from the cookie
    user_id = request.cookies.get('user_id')
    usr_id_Exist = 1

    if not user_id:
        # If no user ID, generate a new one (this is only for new users)
        user_id = str(len(user_chat_histories)) + '_' + str(uuid4())
        usr_id_Exist = 0

    # Ensure there's a history for the user by loading their specific history file
    if user_id not in user_chat_histories:
        user_chat_histories[user_id] = load_chat_history(user_id)

    if user_message:
        # Append the user's message to the chat history
        user_chat_histories[user_id].append({"role": "user", "parts": (user_message)})

        # Get the response from the AI
        response = chat_gemini(user_chat_histories[user_id])

        # Append the model's response to the chat history
        user_chat_histories[user_id].append({"role": "model", "parts": (response)})

        save_chat_history(user_id)

    else:
        # If no message, return the full chat history
        response = ''

    # Set the user ID in the response cookie
    resp = make_response(jsonify({"response": response, "history": user_chat_histories[user_id]}))

    if not usr_id_Exist:
        resp.set_cookie('user_id', user_id)  # Set user ID in the cookie for subsequent visits
    return resp


@app.route('/api/history', methods=['GET'])
def load_history():
    # Get the user ID from the cookie
    user_id = request.cookies.get('user_id')
    # print("user_chat_histories:", user_chat_histories.keys())

    usr_id_Exist = 1
    if not user_id:
        print(f"{user_id} not in cookies-----------------")
        user_id = str(len(user_chat_histories)) + '_' + str(uuid4())
        user_chat_histories[user_id] = []
        usr_id_Exist = 0

    if user_id not in user_chat_histories:
        print("user_id is not loaded to user_chat_histories just yet-----")
        user_chat_histories[user_id] = load_chat_history(user_id)

    # Return the user's chat history
    resp = make_response(jsonify({"history": user_chat_histories[user_id]}))
    if not usr_id_Exist:
        resp.set_cookie('user_id', user_id)
    return resp


if __name__ == '__main__':
    app.run(port=5001, debug=False)

