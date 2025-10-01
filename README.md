# AI Study Assistant

This is a Python-based AI Study Assistant that uses the Gemini API to provide a seamless and interactive chat experience. The application is built with Flask and can be configured to store chat histories either locally or in a remote MongoDB database.

## Repositories

*   **Frontend:** [https://github.com/Drihmia/AI_STUDY_ASSISTANT_FRONTEND](https://github.com/Drihmia/AI_STUDY_ASSISTANT_FRONTEND)
*   **Backend:** [https://github.com/Drihmia/AI_STUDY_ASSISTANT_BACKEND](https://github.com/Drihmia/AI_STUDY_ASSISTANT_BACKEND)

## Features

*   **Interactive Chat:** Engage in conversations with an AI-powered assistant.
*   **Persistent Chat History:** Your conversations are saved, allowing you to continue where you left off.
*   **Dual Storage Options:** Choose between local file-based storage or a remote MongoDB database for your chat histories.
*   **Secure API:** Endpoints are protected to ensure that only authorized users can access conversation data.
*   **Easy Deployment:** The application is designed for straightforward deployment to platforms like Render.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.8 or higher
*   pip (Python package installer)
*   A Gemini API key
*   A MongoDB database (if using remote storage)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Drihmia/AI_STUDY_ASSISTANT.git
    cd AI_STUDY_ASSISTANT
    ```

2.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**

    Create a `.env` file in the root of the project and add the following environment variables. You can use the `.env.example` file as a template.

    ```bash
    # Gemini API Key
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

    # MongoDB Connection URI (only required if STORAGE_TYPE is 'remote')
    MONGO_URI="YOUR_MONGODB_URI"
    MONGO_DB_NAME="chat_history"
    MONGO_COLLECTION_NAME="history"

    # Secret key for Flask session management
    SECRET_KEY="YOUR_SUPER_SECRET_KEY"

    # Password to protect the /api/list_conversations endpoint
    PASSWORD_CONVERSATIONS="YOUR_ADMIN_PASSWORD"

    # Storage type: 'local' or 'remote'
    STORAGE_TYPE="local"

    # Set to True for Flask debug mode
    AI_DEBUG=False
    ```

## Usage

To run the application locally, use the following command:

```bash
python3 chat.py
```

The application will be available at `http://localhost:5000`.

## API Endpoints

*   `GET /`: Root endpoint to check the status of the application.
*   `POST /api/chat`: The main chat endpoint to send and receive messages.
*   `GET /api/history`: Retrieve the chat history for a specific user.
*   `POST /api/answers`: Submit answers to a form presented by the AI.
*   `GET /api/list_conversations`: List all conversations (requires a password).
*   `GET /api/list_conversations/<conversation_id>`: Retrieve a specific conversation by its ID (requires a password).

For a detailed description of all the API endpoints in this project, please see the [API_ENDPOINTS.md](API_ENDPOINTS.md) file.

## Deployment

This application is ready to be deployed on Render. Here are the steps to deploy it:

1.  **Create a new Web Service on Render.**
2.  **Connect your GitHub repository.**
3.  **Configure the build and start commands:**
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `python3 chat.py`
4.  **Add your environment variables** in the Render dashboard.
5.  **Deploy the application.**

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
