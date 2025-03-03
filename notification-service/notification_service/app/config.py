import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
    EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.example.com")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
    EMAIL_USERNAME = os.getenv("EMAIL_USERNAME", "your-email@example.com")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "your-email-password")

config = Config()
 
