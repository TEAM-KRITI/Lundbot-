from pyrogram import Client, filters
from pyrogram.types import Message, ChatMember
import logging
from AarumiMusic import app

logging.basicConfig(level=logging.INFO)

@app.on_message(filters.video_chat_started)
async def video_chat_started(client, message: Message):
    chat = message.chat
    await message.reply(
        f"🎥 Vᴏɪᴄᴇ Cʜᴧᴛ ʜᴧs Sᴛᴧʀᴛᴇᴅ ɪɴ {chat.title}!\n\nᴊᴏɪɴ ᴜs ɴᴏᴡ ғᴏʀ ᴧ ғᴜɴ ᴛɪᴍᴇ ᴛᴏɢᴇᴛʜᴇʀ..! 😉"
    )

@app.on_message(filters.video_chat_ended)
async def video_chat_ended(client, message: Message):
    chat = message.chat
    await message.reply(
        f"🚫 Vᴏɪᴄᴇ Cʜᴧᴛ ʜᴧs Eɴᴅᴇᴅ ɪɴ {chat.title}.\n\nᴛʜᴧɴᴋ ʏᴏᴜ ғᴏʀ ᴊᴏɪɴɪɴɢ..! sᴇᴇ ʏᴏᴜ ɴᴇxᴛ ᴛɪᴍᴇ..! 👋"
    )
