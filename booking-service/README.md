# Booking Service

## Overview
The **Booking Service** manages event bookings, payment processing, and booking statuses.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- RabbitMQ (For asynchronous communication)

## Features
- Create Bookings
- Process Payments
- Check Booking Status
- Publish events to RabbitMQ for notifications

## API Endpoints
| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| POST   | `/bookings/create` | Create a new booking |
| GET    | `/bookings/{booking_id}` | Get booking details |

## Environment Variables
