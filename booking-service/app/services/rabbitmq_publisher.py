import pika
import os
from dotenv import load_dotenv
import json

load_dotenv()

RABBITMQ_URL = os.getenv("RABBITMQ_URL")

def publish_message(queue, message):
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    connection.close()
