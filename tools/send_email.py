import os
import requests

def send_teacher_email(fullName, emailAddress, message):
    """
    Sends an email to the teacher with the student's message.
    Uses the Mailgun API to send the email.
    """
    # --- Get Mailgun and Teacher Email from Environment Variables ---
    mailgun_api_key = os.getenv('MAILGUN_API_KEY')
    mailgun_domain = os.getenv('MAILGUN_DOMAIN')
    teacher_email = os.getenv('TEACHER_EMAIL')

    if not all([mailgun_api_key, mailgun_domain, teacher_email]):
        print("Email not sent: Missing MAILGUN_API_KEY, MAILGUN_DOMAIN, or TEACHER_EMAIL environment variables.")
        return None

    # --- Construct the Email ---
    subject = f"New Message from {fullName} via AI Study Assistant"
    text_body = f"""You have received a new message from a student.

    From: {fullName}
    Email: {emailAddress}
    
    Message:
    {message}
    """
    html_body = f"""<html>
    <body>
        <h2>New Message from a Student</h2>
        <p><strong>From:</strong> {fullName}</p>
        <p><strong>Email:</strong> <a href="mailto:{emailAddress}">{emailAddress}</a></p>
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
        
        # --- Check the Response ---
        if response.status_code == 200:
            print(f"Email sent successfully to {teacher_email}")
        else:
            print(f"Failed to send email. Status code: {response.status_code}, Response: {response.text}")
        
        return response

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending the email: {e}")
        return None
