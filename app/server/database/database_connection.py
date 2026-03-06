import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.server.config.config import Settings

# Importing enviroment Variables
settings = Settings()

# Database Configuration

client = AsyncIOMotorClient(settings.MONGODB_URL, serverSelectionTimeoutMS=5000)
client.get_io_loop = asyncio.get_event_loop

# Database Connection Test

try:
    db_connection = client.server_info()
    print("Connection to Mongo DB Server Successfull")
except Exception as e:
    print("Connection Unsuccessfull")
    print(str(e))

database = client.tasks_api

# Database Collections

tasks = database.get_collection("tasks_collection")