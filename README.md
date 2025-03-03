# CS4067-Assgt-EventBooking-i220920-Aashir-Hameed
# Online Event Booking Platform

##  Overview
The **Online Event Booking Platform** is a **microservices-based system** where users can **browse events, book tickets, make payments, and receive notifications**.

The platform handles:  
 **User authentication**  
 **Event listings & availability**  
 **Ticket booking & payments**  
 **Email/SMS notifications**  

This system demonstrates:  
🔹 **Synchronous & Asynchronous communication**  
🔹 **PostgreSQL & MongoDB integration**  
🔹 **RabbitMQ for event-driven messaging**  
🔹 **Docker-based microservices architecture**  

---

## Tech Stack

| **Technology**   | **Usage**             |
|-----------------|---------------------|
| **FastAPI**     | Microservices Backend |
| **PostgreSQL**  | Relational Database (User & Booking Services) |
| **MongoDB**     | NoSQL Database (Event & Notification Services) |
| **RabbitMQ**    | Asynchronous Messaging |
| **Docker**      | Containerization |
| **JWT Auth**    | Secure User Authentication |

---

##  Microservices Architecture

| **Microservice**      | **Functionality**                                      | **Tech Stack**             | **Database**    | **Communication**  |
|----------------------|------------------------------------------------|--------------------------|---------------|----------------|
| **User Service**      | Manages user authentication & profiles | FastAPI, JWT, PostgreSQL | PostgreSQL    | REST API (Sync)  |
| **Event Service**     | Handles event listings & availability | FastAPI, MongoDB         | MongoDB       | REST API (Sync)  |
| **Booking Service**   | Manages ticket bookings & payments    | FastAPI, PostgreSQL, RabbitMQ | PostgreSQL | REST API (Sync), RabbitMQ (Async) |
| **Notification Service** | Sends email notifications | FastAPI, MongoDB, SMTP | MongoDB | RabbitMQ (Async) |

---

##  Microservice Communication

###  Synchronous Communication (REST API)
| **From**          | **To**             | **Method** | **API Endpoint** |
|------------------|------------------|-----------|----------------|
| User Service     | Event Service     | GET       | `/events` (Get event list) |
| User Service     | Booking Service   | POST      | `/bookings/create` (Create booking) |
| Booking Service  | Payment Gateway (Mock) | POST | `/payments` (Process payment) |
| Booking Service  | Event Service     | GET       | `/events/{event_id}/availability` (Check availability) |

###  Asynchronous Communication (RabbitMQ Events)
| **Publisher (Service Sending Event)** | **Consumer (Service Receiving Event)** | **Event Data** |
|-------------------------------------|---------------------------------|----------------|
| Booking Service  | Notification Service | `{ booking_id, user_email, status: "CONFIRMED" }` |

---

##  Project Setup & Installation

### 1️ Clone the Repository
```sh
git clone https://github.com/Aashir0920/CS4067-Assgt-EventBooking-i220920-Aashir-Hameed.git
cd CS4067-Assgt-EventBooking-i220920-Aashir-Hameed
```

---

### 2️ Set Up Environment Variables
Each microservice requires a **`.env`** file for configuration.

#### **User Service (`user_service/.env`)**
```
DATABASE_URL=postgresql://user:password@localhost:5432/user_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
#### **Event Service (`event_service/.env`)**
```
MONGO_URI=mongodb://localhost:27017/event_db
```
#### **Booking Service (`booking_service/.env`)**
```
DATABASE_URL=postgresql://user:password@localhost:5432/booking_db
RABBITMQ_URL=amqp://guest:guest@localhost/
```
#### **Notification Service (`notification_service/.env`)**
```
MONGO_URI=mongodb://localhost:27017/notifications_db
RABBITMQ_URL=amqp://guest:guest@localhost/
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
```

---

### 3️ Install Dependencies
Navigate into each microservice and install dependencies:
```sh
cd user_service
pip install -r requirements.txt

cd ../event_service
pip install -r requirements.txt

cd ../booking_service
pip install -r requirements.txt

cd ../notification_service
pip install -r requirements.txt
```

---

### 4️ Start Each Microservice
Run each microservice in a separate terminal:

#### **Start User Service**
```sh
cd user_service
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

#### **Start Event Service**
```sh
cd event_service
uvicorn main:app --host 0.0.0.0 --port 8002 --reload
```

#### **Start Booking Service**
```sh
cd booking_service
uvicorn main:app --host 0.0.0.0 --port 8003 --reload
```

#### **Start Notification Service**
```sh
cd notification_service
uvicorn main:app --host 0.0.0.0 --port 8004 --reload
```

---

##  Running with Docker
Each microservice has a **Dockerfile**, so you can run them in containers.

### 1️ Build Docker Images
```sh
docker build -t user-service user_service/
docker build -t event-service event_service/
docker build -t booking-service booking_service/
docker build -t notification-service notification_service/
```

### 2️ Run Containers
```sh
docker run -p 8001:8001 user-service
docker run -p 8002:8002 event-service
docker run -p 8003:8003 booking-service
docker run -p 8004:8004 notification-service
```

---

##  API Documentation
Each service provides an **interactive API documentation** at:  
- **User Service** → `http://localhost:8001/docs`
- **Event Service** → `http://localhost:8002/docs`
- **Booking Service** → `http://localhost:8003/docs`
- **Notification Service** → `http://localhost:8004/docs`

---

##  Jira & GitHub Integration
 **Jira Board** created for task management  
 **GitHub Project** with Kanban board for tracking progress  
 **GitHub Issues** linked to Jira for automatic updates  

---


##  Contributors
- **Aashir Hameed** (@Aashir0920)  
