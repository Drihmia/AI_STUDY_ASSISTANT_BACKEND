Little project trying to descover the realm of AI and chatbots.

## Installation
```bash
# Python related packages:
pip3 install -r requirements.txt

# Node related packages:
node Install
npm install -g forever
```

## Description
This project is a simple chatbot that uses groq AI to answer questions.
I have feed it with prompts to respond to students questions about courses related to Physics and Chemistry of Moroccan high school.

## Usage
lanching the chatbot
```bash
python chatbot.py
OR
gunicorn -w 3 -b 127.0.0.1:5001 chat:app --error-logfile ai-error.log --access-logfile ai-access.log --capture-output --pid /run/chat.pid --daemon
```

lanching the web app
```bash
node server.js
OR
forever start server.js
```

Mode commands
````bash
forever list
forever stop server.js
forever logs
```
Open your browser and go to `http://localhost:3000/`

## Resources
- [Documentation](https://console.groq.com/docs/examples)
- [Groq API](https://console.groq.com/docs/api)
- [Python API](https://console.groq.com/docs/python)
- [Chatbot with Conversational Memory on LangChain](https://replit.com/@GroqCloud/Chatbot-with-Conversational-Memory-on-LangChain#main.py)
- [Groq Quickstart Conversational Chatbot](https://replit.com/@GroqCloud/Groq-Quickstart-Conversational-Chatbot?v=1#README.md)
