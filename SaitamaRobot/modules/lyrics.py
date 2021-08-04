from Python_ARQ import ARQ
from aiohttp import ClientSession
import os
from SaitamaRobot import pbot
from pyrogram import filters


arq_url = "https://thearq.tech"
arq_api = os.environ["arq_api"]


@pbot.on_message(filters.command('lyrics'))
async def lyrics(_,message):
    msg = message.text.replace(message.text.split(' ')[0], '')
    session = ClientSession()
    arq = ARQ(arq_api , arq_url , session)
    lyrics_ = arq.lyrics(msg)
    kek = lyrics_[0]
    await message.reply_text(kek)
    await session.close()
