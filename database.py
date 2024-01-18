from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()  # Load environment variables

Mongo_URI = os.getenv("MONGO_URI")  # Get MongoDB URI from environment variable

client = MongoClient(Mongo_URI)

db = client['ChatGPT_Eval']  # database name

# Accessing the specific collection
questions_collection = db['History']  # replace with your actual collection name
