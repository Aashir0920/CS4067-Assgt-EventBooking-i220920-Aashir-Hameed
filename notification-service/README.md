# Notification Service

## Overview
The **Notification Service** listens to RabbitMQ messages and sends confirmation emails/SMS to users when a booking is confirmed.

## Tech Stack
- FastAPI
- MongoDB (For storing notifications)
- RabbitMQ (For consuming messages)
- SMTP (For sending emails)

## Features
- Listen for booking confirmation messages from RabbitMQ
- Send email notifications
- Log sent notifications in MongoDB

## API Endpoints
| Method | Endpoint       | Description |
|--------|---------------|-------------|
| GET    | `/health`     | Check if service is running |

## Environment Variables
MONGO_URI=mongodb://localhost:27017/notifications_db RABBITMQ_URL=amqp://guest:guest@localhost/ SMTP_SERVER=smtp.gmail.com SMTP_PORT=587 EMAIL_USER=your_email@gmail.com EMAIL_PASS=your_email_password

perl
Copy
Edit

## Setup & Run
```sh
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8004 --reload
