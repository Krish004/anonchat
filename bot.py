from config import Config
from pyrogram import Client
from handlers import *  # registers handlers

app = Client(
    "anon-bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

print("🚀 Bot starting...")
app.run()
