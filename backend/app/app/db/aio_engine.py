from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://mongo:changethis@mongodb:27017")
MongoEngine = AIOEngine(motor_client=client, database="icon")
