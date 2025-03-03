from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = "eventdb"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
events_collection = db["events"]
 
