from fastapi import APIRouter
from app.models.notification import Notification
from app.services.email_service import send_email

router = APIRouter()

@router.post("/send-notification/")
def send_notification(notification: Notification):
    subject = "Booking Confirmation"
    message = f"Your booking with ID {notification.booking_id} is {notification.status}."
    send_email(notification.user_email, subject, message)
    return {"message": "Notification sent"}
 
