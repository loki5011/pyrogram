import os
from pyrogram import Client

# Get values from environment variables
API_ID = os.getenv("API_ID")  # Replace with your API ID from Telegram
API_HASH = os.getenv("API_HASH")  # Replace with your API Hash from Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Replace with your Bot Token from BotFather

# Create the bot client instance
app = Client(
    "my_bot",  # This is the session name, can be anything
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define a handler for all incoming messages
@app.on_message()
def handle_message(client, message):
    message.reply("Hello! I am a Pyrogram bot.")

# Start the bot
app.run()
