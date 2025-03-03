# Event Service

## Overview
The **Event Service** manages event listings and event details. Users can browse available events.

## Tech Stack
- FastAPI
- MongoDB
- Motor (MongoDB async driver)

## Features
- Create Events
- Get Event List
- Get Event Details
- Check Event Availability

## API Endpoints
| Method | Endpoint              | Description |
|--------|-----------------------|-------------|
| POST   | `/events/create`       | Create a new event |
| GET    | `/events`              | List all events |
| GET    | `/events/{event_id}`   | Get event details |
| GET    | `/events/{event_id}/availability` | Check event availability |

## Environment Variables
Create a `.env` file:
