from fastapi import APIRouter, HTTPException
from models import Event, EventUpdate  
from .database import events_collection
from bson import ObjectId

router = APIRouter()

@router.post("/events/")
def create_event(event: Event):
    event_dict = event.dict()
    result = events_collection.insert_one(event_dict)
    return {"message": "Event created", "id": str(result.inserted_id)}

@router.get("/events/")
def get_events():
    events = list(events_collection.find({}, {"_id": 1, "title": 1, "date": 1}))
    for event in events:
        event["_id"] = str(event["_id"])
    return events

@router.get("/events/{event_id}")
def get_event(event_id: str):
    event = events_collection.find_one({"_id": ObjectId(event_id)})
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    event["_id"] = str(event["_id"])
    return event

@router.put("/events/{event_id}")
def update_event(event_id: str, update: EventUpdate):
    update_data = {k: v for k, v in update.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")
    
    result = events_collection.update_one({"_id": ObjectId(event_id)}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Event not found or no update made")
    
    return {"message": "Event updated successfully"}

@router.delete("/events/{event_id}")
def delete_event(event_id: str):
    result = events_collection.delete_one({"_id": ObjectId(event_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Event not found")
    
    return {"message": "Event deleted successfully"}
