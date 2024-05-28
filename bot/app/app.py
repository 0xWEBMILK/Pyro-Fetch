# Default imports
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram import enums


# Custom imports
from config_reader import bot_settings

from .handlers import ping
from .handlers import info


app = Client(
    # Name of my App
    "MyAccount",


    # API_HASH & API_ID
    api_hash=bot_settings.api_hash.get_secret_value(),
    api_id=bot_settings.api_id.get_secret_value(),
)


# Set parsemode
app.set_parse_mode(enums.ParseMode.MARKDOWN)


# Handler's
app.add_handler(
    MessageHandler(
        ping,
        filters.command(['ping'], prefixes=['/']) & filters.private
    ),
    group=1
)

app.add_handler(
    MessageHandler(
        info,
        filters.command(['info'], prefixes=['/']) & filters.private
    )
)