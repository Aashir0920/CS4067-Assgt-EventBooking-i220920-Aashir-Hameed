from fastapi import FastAPI
import threading
from app.api.endpoints.notifications import router as notification_router
from app.services.rabbitmq_consumer import start_consumer

app = FastAPI()

# Include the API routes
app.include_router(notification_router, prefix="/notifications")

# Start RabbitMQ consumer in a separate thread
threading.Thread(target=start_consumer, daemon=True).start()

@app.get("/")
def read_root():
    return {"message": "Notification Service is running"}
 
