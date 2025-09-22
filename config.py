import os

class Config:
    # Telegram Bot
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "12345"))   # optional if using BotToken only
    API_HASH = os.environ.get("API_HASH", "api_hash_here")

    # Mongo
    MONGO_URI = os.environ.get("MONGO_URI", "")
    DB_NAME = os.environ.get("DB_NAME", "anon_chat")

    # Audit & Admin
    AUDIT_CHAT_ID = int(os.environ.get("AUDIT_CHAT_ID", "0"))  # Channel/Group for logs
    ADMIN_IDS = list(map(int, os.environ.get("ADMIN_IDS", "0").split(",")))  # comma-separated

    # Matching
    ENABLE_PREF_MATCH = os.environ.get("ENABLE_PREF_MATCH", "false").lower() == "true"

    # Deployment
    PORT = int(os.environ.get("PORT", "8080"))
    WEBHOOK = os.environ.get("WEBHOOK_URL", "")
config.py
