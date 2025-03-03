from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    title: str
    description: str
    location: str
    date: str
    price: float
    available_tickets: int

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = None
    price: Optional[float] = None
    available_tickets: Optional[int] = None
 
