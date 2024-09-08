import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

# Initialize the Pyrogram Client
pr0fess0r_99 = Client(
    "𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗽𝗹𝗲𝗮𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗢𝗽𝘂𝘀𝗧𝗲𝗰𝗵𝘇",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"]
)

# Get environment variables
CHAT_ID = int(os.environ.get("CHAT_ID", None))
TEXT = "Hello there"
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: Client, message: Message):
    # Define inline buttons with updated URLs and texts
    button = [
        [InlineKeyboardButton("💸 Free 150$ Giveaway ✨", url="https://t.me/Quotexfreemoneybot"),
         InlineKeyboardButton("Free VIP and Tournament ✅", url="https://t.me/+8kuYmspERrk3MzU1")]
    ]
    
    # Reply to the start command with a message and buttons
    await message.reply_text(
        text="Hello there",
        reply_markup=InlineKeyboardMarkup(button),
        disable_web_page_preview=True
    )

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: Client, message: ChatJoinRequest):
    chat = message.chat  # Chat
    user = message.from_user  # User
    
    # Log user join
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡")
    
    # Approve the chat join request
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    
    # Send a welcome message if auto-approval is enabled
    if APPROVED == "on":
        await client.send_message(
            chat_id=chat.id,
            text=TEXT
        )

# Print a startup message and run the bot
print("𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗽𝗹𝗲𝗮𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗢𝗽𝘂𝘀𝗧𝗲𝗰𝗵𝘇")
pr0fess0r_99.run()
