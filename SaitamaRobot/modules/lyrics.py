
from Python_ARQ import ARQ
from aiohttp import ClientSession
import os

from pyrogram.types.messages_and_media import message
from SaitamaRobot import pbot
from pyrogram import filters


api_url = "https://thearq.tech/"
api_key = os.environ["arq_api"]


@pbot.on_message(filters.command('lyrics'))
async def main():
    session = ClientSession()
    message = message.text.replace(message.text.split(' ')[0], '')
    arq = ARQ(api_url, api_key, session)
    results = await arq.lyrics(message)
    lyrics = results.result
    await message.reply_text(lyrics)
    await session.close()
