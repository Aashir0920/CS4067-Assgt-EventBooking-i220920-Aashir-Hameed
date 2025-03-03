from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Event Service")

# Include API routes
app.include_router(router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Event Service!"}
 
