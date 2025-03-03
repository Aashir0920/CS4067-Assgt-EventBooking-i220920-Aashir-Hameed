from fastapi import FastAPI
from app.api.endpoints import bookings

app = FastAPI()

app.include_router(bookings.router)

@app.get("/")
def health_check():
    return {"status": "Booking Service is running"}
