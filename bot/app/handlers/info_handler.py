# Default imports
from pyrogram import Client

from .modules import priceFetch


# Information handler
async def info(client, message):
    coin = (message.text).split(' ')[1]
    currencyList = (message.text).split(' ')[2:]


    price = await priceFetch(
        coin=coin,
        currencyList=currencyList
    )


    await message.reply(price)