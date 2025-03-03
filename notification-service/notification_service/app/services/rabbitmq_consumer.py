import pika
import json
from app.services.email_service import send_email
from app.config import config

def callback(ch, method, properties, body):
    data = json.loads(body)
    booking_id = data.get("booking_id")
    user_email = data.get("user_email")
    status = data.get("status")

    subject = "Booking Confirmation"
    message = f"Your booking with ID {booking_id} is {status}."

    send_email(user_email, subject, message)
    print(f"Processed notification for booking {booking_id}")

def start_consumer():
    connection = pika.BlockingConnection(pika.URLParameters(config.RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue="notifications")

    channel.basic_consume(queue="notifications", on_message_callback=callback, auto_ack=True)

    print("Waiting for messages...")
    channel.start_consuming()
 
