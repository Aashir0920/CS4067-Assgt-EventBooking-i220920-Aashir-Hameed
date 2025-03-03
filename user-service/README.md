# User Service

## Overview
The **User Service** handles user authentication and profile management for the Online Event Booking Platform. It enables user registration, login, and profile retrieval.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication

## Features
- User Registration
- User Login with JWT Authentication
- Retrieve User Profile

## API Endpoints
| Method | Endpoint            | Description |
|--------|---------------------|-------------|
| POST   | `/users/register`    | Register a new user |
| POST   | `/users/login`       | Authenticate user & get JWT token |
| GET    | `/users/profile`     | Get user profile (Authenticated) |

## Environment Variables
Create a `.env` file with:
 
