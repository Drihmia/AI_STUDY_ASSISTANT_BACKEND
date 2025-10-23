import os
import requests

def send_teacher_email(fullName, emailAddress, message, subject):
    """
    Sends an email to the teacher with the student's message.
    Uses the Mailgun API to send the email.
    """
    # --- Get Mailgun and Teacher Email from Environment Variables ---
    mailgun_api_key = os.getenv('MAILGUN_API_KEY')
    mailgun_domain = os.getenv('MAILGUN_DOMAIN')
    teacher_email = os.getenv('TEACHER_EMAIL')

    if not all([mailgun_api_key, mailgun_domain, teacher_email]):
        raise ValueError("Email not sent: Missing MAILGUN_API_KEY, MAILGUN_DOMAIN, or TEACHER_EMAIL environment variables.")

    # --- Construct the Email ---
    text_body = f"""You have received a new message from a student.

    From: {fullName}
    Email: {emailAddress}
    Subject: {subject}
    
    Message:
    {message}
    """
    html_body = f"""<html>
    <body>
        <h2>New Message from a Student</h2>
        <p><strong>From:</strong> {fullName}</p>
        <p><strong>Email:</strong> <a href="mailto:{emailAddress}">{emailAddress}</a></p>
        <p><strong>Subject:</strong> {subject}</p>
        <hr>
        <h3>Message:</h3>
        <p>{message}</p>
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
            })
        
        response.raise_for_status()
        
        print(f"Email sent successfully to {teacher_email}")
        
        return response

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending the email: {e}")
        raise
