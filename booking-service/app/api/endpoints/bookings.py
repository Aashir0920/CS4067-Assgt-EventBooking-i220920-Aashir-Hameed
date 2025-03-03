from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.booking import Booking
from app.services.payment_service import process_payment
from app.services.rabbitmq_publisher import publish_message
import os
import requests

router = APIRouter()

EVENT_SERVICE_URL = os.getenv("EVENT_SERVICE_URL")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/bookings/")
def create_booking(user_id: int, event_id: int, db: Session = Depends(get_db)):
    # Check Event Availability
    event_response = requests.get(f"{EVENT_SERVICE_URL}/events/{event_id}/availability")
    if event_response.status_code != 200 or not event_response.json().get("available", False):
        raise HTTPException(status_code=400, detail="Event not available")

    # Process Payment
    payment_response = process_payment(user_id, 100)
    if payment_response.get("status") != "SUCCESS":
        raise HTTPException(status_code=400, detail="Payment failed")

    # Create Booking
    booking = Booking(user_id=user_id, event_id=event_id, status="CONFIRMED")
    db.add(booking)
    db.commit()
    db.refresh(booking)

    # Publish Event to RabbitMQ
    publish_message("booking_confirmations", {"booking_id": booking.id, "user_id": user_id, "status": "CONFIRMED"})

    return {"message": "Booking successful", "booking_id": booking.id}

@router.get("/bookings/{booking_id}")
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking
