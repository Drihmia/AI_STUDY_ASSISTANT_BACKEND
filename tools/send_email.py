import os
import requests
import html
import re

def validate_email(email):
    """
    Validates email format.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def send_teacher_email(fullName, emailAddress, message):
    """
    Sends an email to the teacher with the student's message.
    Uses the Mailgun API to send the email.
    Returns a tuple: (success: bool, error_message: str or None)
    """
    # --- Validate inputs ---
    if not fullName or not fullName.strip():
        return False, "Full name is required"

    if not emailAddress or not validate_email(emailAddress):
        return False, "Valid email address is required"

    if not message or len(message.strip()) < 10:
        return False, "Message must be at least 10 characters long"

    # --- Get Mailgun and Teacher Email from Environment Variables ---
    mailgun_api_key = os.getenv('MAILGUN_API_KEY')
    mailgun_domain = os.getenv('MAILGUN_DOMAIN')
    teacher_email = os.getenv('TEACHER_EMAIL')

    if not all([mailgun_api_key, mailgun_domain, teacher_email]):
        error_msg = "Email not sent: Missing MAILGUN_API_KEY, MAILGUN_DOMAIN, or TEACHER_EMAIL environment variables."
        print(error_msg)
        return False, "Email configuration is missing"

    # --- Escape user input to prevent HTML injection ---
    safe_fullName = html.escape(fullName.strip())
    safe_emailAddress = html.escape(emailAddress.strip())
    safe_message = html.escape(message.strip())

    # --- Construct the Email ---
    subject = f"New Message from {safe_fullName} via AI Study Assistant"
    text_body = f"""You have received a new message from a student.

    From: {safe_fullName}
    Email: {safe_emailAddress}

    Message:
    {safe_message}
    """
    html_body = f"""<html>
    <body>
        <h2>New Message from a Student</h2>
        <p><strong>From:</strong> {safe_fullName}</p>
        <p><strong>Email:</strong> <a href="mailto:{safe_emailAddress}">{safe_emailAddress}</a></p>
        <hr>
        <h3>Message:</h3>
        <p style="white-space: pre-wrap;">{safe_message}</p>
    </body>
    </html>"""

    # --- Send the Request to Mailgun ---
    try:
        response = requests.post(
            f"https://api.mailgun.net/v3/{mailgun_domain}/messages",
            auth=("api", mailgun_api_key),
            data={
                "from": f"AI Study Assistant <mailgun@{mailgun_domain}>",
                "to": teacher_email,
                "subject": subject,
                "text": text_body,
                "html": html_body
            },
            timeout=10
        )

        # --- Check the Response ---
        if response.status_code == 200:
            print(f"Email sent successfully to {teacher_email}")
            return True, None
        else:
            error_msg = f"Failed to send email. Status code: {response.status_code}, Response: {response.text}"
            print(error_msg)
            return False, "Failed to send email. Please try again later."

    except requests.exceptions.Timeout:
        error_msg = "Email sending timed out"
        print(error_msg)
        return False, "Email service is taking too long to respond. Please try again later."
    except requests.exceptions.RequestException as e:
        error_msg = f"An error occurred while sending the email: {e}"
        print(error_msg)
        return False, "Failed to send email due to a network error."
