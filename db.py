from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

mongo = AsyncIOMotorClient(Config.MONGO_URI)
db = mongo[Config.DB_NAME]

users = db["users"]
queue = db["queue"]
logs = db["logs"]

async def get_user(user_id: int):
    user = await users.find_one({"_id": user_id})
    if not user:
        user = {"_id": user_id, "profile": {}, "status": "idle", "partner_id": None}
        await users.insert_one(user)
    return user
