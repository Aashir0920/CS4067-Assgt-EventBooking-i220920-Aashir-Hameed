from pydantic import BaseModel

class Notification(BaseModel):
    booking_id: str
    user_email: str
    status: str
 
