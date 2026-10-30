import os
from dotenv import load_dotenv   #Here we are Load the dotenv 
from pymongo import AsyncMongoClient 

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")      # access the Database / Mongo URI
DATABASE_NAME = os.getenv("DATABASE_NAME") # Access the Database Name

# Create MongoDB client
client = AsyncMongoClient(MONGODB_URL) # Async Mongo Client
db = client[DATABASE_NAME] # We are selecting the Database Name with the Help of The AuncMongoclient that we crreate 
users_collection = db["users"] # Accesing the User collection that we create 