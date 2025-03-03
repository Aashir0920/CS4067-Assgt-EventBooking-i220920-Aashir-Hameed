from fastapi import FastAPI
from database import engine, Base
from routes import router

# Initialize FastAPI App
app = FastAPI()

# Create Tables
Base.metadata.create_all(bind=engine)

# Include Routes
app.include_router(router, prefix="/users")

# Root Endpoint
@app.get("/")
def home():
    return {"message": "User Service is Running"}

