import os
from pyrogram import Client, filters

# Get API credentials from environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create the bot client
app = Client("auto_filter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Command to start the bot
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Welcome to the Auto Filter Bot! Upload a file to get started.")

# Filter files by type and size (example: allow only images and videos under 10MB)
@app.on_message(filters.document | filters.photo | filters.video)
def filter_files(client, message):
    # Check file size
    if message.document and message.document.file_size > 10 * 1024 * 1024:  # 10MB limit
        message.reply("File is too large! Please upload a file smaller than 10MB.")
        return

    # Handle photo or video files
    if message.photo or message.video:
        message.reply("This is an image/video. Processing...")
    
    # If it's a document, check the file type
    if message.document:
        mime_type = message.document.mime_type
        if mime_type.startswith("image") or mime_type.startswith("video"):
            message.reply("This is an accepted file type!")
        else:
            message.reply("File type not supported. Please upload an image or video.")

# Run the bot
app.run()
