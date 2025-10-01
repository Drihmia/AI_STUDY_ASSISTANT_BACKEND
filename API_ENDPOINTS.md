# API Endpoints

Here is a detailed description of all the API endpoints in the project.

---

### 1. Root

*   **Method:** `GET`
*   **Path:** `/`
*   **Description:** A simple health check endpoint to confirm that the application is running.
*   **Parameters:** None.
*   **Responses:**
    *   **200 OK:**
        ```json
        {
          "status": "Flask server is running"
        }
        ```

---

### 2. Chat Endpoint

*   **Method:** `POST`
*   **Path:** `/api/chat`
*   **Description:** This is the primary endpoint for interacting with the AI. It receives a user's message, processes it, gets a response from the Gemini API, and returns the AI's message. It also handles the submission of form answers collected via the `/api/answers` endpoint.
*   **Parameters:**
    *   `user_id` (Query String):
        *   **Optional/Conditionally Required:** While the server can generate a new ID for a first-time user, this ID is **required** to retrieve and continue an existing conversation. Your frontend should store the `user_id` (from the cookie or initial response) and send it with every subsequent request.
    *   `message` (JSON Body):
        *   **Required:** A string containing the user's message. This is ignored if the request is triggered internally from the `/api/answers` endpoint.
        ```json
        {
          "message": "Hello, how are you?"
        }
        ```
*   **Responses:**
    *   **200 OK:**
        ```json
        {
          "message": {
            "role": "model",
            "parts": "I am doing well, thank you for asking. How can I help you today?"
          }
        }
        ```
    *   **400 Bad Request:**
        ```json
        {
          "error": "No message provided"
        }
        ```
    *   **500 Internal Server Error:**
        ```json
        {
          "error": "An internal error occurred."
        }
        ```

---

### 3. Get Chat History

*   **Method:** `GET`
*   **Path:** `/api/history`
*   **Description:** Retrieves the chat history for a specific user with support for pagination.
*   **Parameters:**
    *   `user_id` (Query String):
        *   **Required:** The unique identifier for the user whose history you want to fetch.
    *   `page` (Query String):
        *   **Optional:** The page number for pagination. Defaults to `1`.
    *   `limit` (Query String):
        *   **Optional:** The number of messages to return per page. Defaults to `2`.
*   **Responses:**
    *   **200 OK:**
        ```json
        {
          "history": [
            {
              "role": "user",
              "parts": "2024-05-23 10:00:00 - Hello"
            },
            {
              "role": "model",
              "parts": "2024-05-23 10:00:01 - Hi there! How can I help you?"
            }
          ],
          "page": 1,
          "limit": 2,
          "max_page": 10,
          "form_id": "some_form_id_if_present"
        }
        ```
    *   **200 OK (with error):** This can occur if a general exception happens on the server. The status is 200, but the body contains an error message.
        ```json
        {
            "error": "Details of the specific exception",
            "history": [],
            "page": 1,
            "limit": 2,
            "max_page": 1,
            "form_id": "some_form_id_if_present"
        }
        ```
    *   **400 Bad Request:** This occurs if `page` or `limit` are not valid integers.
        ```json
        {
            "error": "Invalid page or limit parameter. Must be an integer.",
            "history": [],
            "page": 1,
            "limit": 5,
            "form_id": "some_form_id_if_present"
        }
        ```
    *   **404 Not Found:**
        ```json
        {
          "error": "History not found for this user"
        }
        ```

---

### 4. Submit Form Answers

*   **Method:** `POST`
*   **Path:** `/api/answers`
*   **Description:** Used to submit data from a form that the AI might have presented to the user. This endpoint stores the answers in the user's session and then internally calls the `/api/chat` endpoint to process them.
*   **Parameters:**
    *   **Form Data or JSON Body:** This endpoint accepts either `application/x-www-form-urlencoded` or `application/json`. The parameters are the key-value pairs of the form fields.
        ```json
        {
          "question_1_id": "User's answer to question 1",
          "language": "en"
        }
        ```
*   **Responses:**
    *   **200 OK:** (This endpoint internally calls `/api/chat`, so the response will be from the chat endpoint)
        ```json
        {
          "message": {
            "role": "model",
            "parts": "Thank you for providing your answers. I have processed them and can now..."
          }
        }
        ```
    *   **400 Bad Request:**
        ```json
        {
          "error": "No form data received"
        }
        ```

---

### 5. List All Conversations (Admin)

*   **Method:** `GET`
*   **Path:** `/api/list_conversations`
*   **Description:** A protected endpoint that returns a list of all conversation IDs, sorted by last modification time.
*   **Parameters:**
    *   `password` (Query String):
        *   **Required:** The password must match the `PASSWORD_CONVERSATIONS` environment variable to authorize the request.
*   **Responses:**
    *   **200 OK:**
        ```json
        [
          "user_123_abc",
          "user_456_def"
        ]
        ```
    *   **401 Unauthorized:**
        ```json
        {
          "error": "Not authorized"
        }
        ```

---

### 6. Get Specific Conversation (Admin)

*   **Method:** `GET`
*   **Path:** `/api/list_conversations/<conversation_id>`
*   **Description:** A protected endpoint that retrieves the entire chat history for a single, specified conversation.
*   **Parameters:**
    *   `conversation_id` (Path):
        *   **Required:** The unique identifier for the conversation you want to retrieve.
    *   `password` (Query String):
        *   **Required:** The password must match the `PASSWORD_CONVERSATIONS` environment variable.
*   **Responses:**
    *   **200 OK:**
        ```json
        {
          "history": [
            {
              "role": "user",
              "parts": "2024-05-23 10:00:00 - Hello"
            },
            {
              "role": "model",
              "parts": "2024-05-23 10:00:01 - Hi there! How can I help you?"
            }
          ]
        }
        ```
    *   **401 Unauthorized:**
        ```json
        {
          "error": "Not authorized"
        }
        ```
    *   **404 Not Found:**
        ```json
        {
          "error": "History not found for this user"
        }
        ```

---

### 7. Test Endpoint

*   **Method:** `GET`
*   **Path:** `/api/test/<value>`
*   **Description:** A simple endpoint for testing the server's response.
*   **Parameters:**
    *   `value` (Path):
        *   **Required:** If the value is `"ok"`, the endpoint returns a success message. Otherwise, it returns an error.
*   **Responses:**
    *   **200 OK:**
        ```json
        {
          "status": "ok"
        }
        ```
    *   **400 Bad Request:**
        ```json
        {
          "error": "test failed"
        }
        ```
