# Default imports
from pyrogram import Client


# Ping handler
async def ping(client, message):
    await message.reply('pong.')