import smtplib
from email.message import EmailMessage
from app.config import settings
from app.logger import get_logger

logger = get_logger("email")

def send_contact_email(data: dict):
    msg = EmailMessage()
    msg["Subject"] = f"New Contact Form – {data['inquiry_type']}"
    msg["From"] = settings.EMAIL_SENDER
    msg["To"] = settings.EMAIL_RECEIVER
    msg["Reply-To"] = data["email"]

    msg.set_content(f"""
New Contact Submission

Inquiry Type: {data['inquiry_type']}
Name: {data['first_name']} {data.get('last_name', '')}
Email: {data['email']}

Location:
State: {data.get('state', 'N/A')}
City: {data.get('city', 'N/A')}
Zipcode: {data.get('zipcode', 'N/A')}

Message:
{data['message']}
""")

    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(settings.EMAIL_SENDER, settings.EMAIL_PASSWORD)
            server.send_message(msg)
        logger.info("Email sent successfully")

    except Exception as e:
        logger.error(f"Email sending failed: {e}")
