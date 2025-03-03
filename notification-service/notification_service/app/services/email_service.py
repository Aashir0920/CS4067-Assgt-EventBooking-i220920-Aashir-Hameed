import smtplib
from email.mime.text import MIMEText
from app.config import config

def send_email(to_email: str, subject: str, message: str):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = config.EMAIL_USERNAME
        msg["To"] = to_email

        with smtplib.SMTP(config.EMAIL_HOST, config.EMAIL_PORT) as server:
            server.starttls()
            server.login(config.EMAIL_USERNAME, config.EMAIL_PASSWORD)
            server.sendmail(config.EMAIL_USERNAME, to_email, msg.as_string())

        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Error sending email: {e}")
 
