import requests
import os
from dotenv import load_dotenv

load_dotenv()
PAYMENT_SERVICE_URL = os.getenv("PAYMENT_SERVICE_URL")

def process_payment(user_id, amount):
    response = requests.post(f"{PAYMENT_SERVICE_URL}/payments", json={"user_id": user_id, "amount": amount})
    return response.json()
