from SaitamaRobot import pbot as bot
from pyrogram import filters

import requests

from bs4 import BeautifulSoup

@bot.on_message(filters.command('watchorder'))

def watchorderx(_,message):

	anime = message.text.replace('/watchorder' , '')	anime = anime.replace(' ' , '')

	res = requests.get(f'https://chiaki.site/?/tools/autocomplete_series&term={anime}').json()

	data = None

	id_ = res[0]['id']

	res_ = requests.get(f'https://chiaki.site/?/tools/watch_order/id/{id_}').text

	soup = BeautifulSoup(res_ , 'html.parser')

	anime_names = soup.find_all('span' , class_='wo_title')

	for x in anime_names:

		if data:

			data = f"{data}\n{x.text}"

		else:

			data = x.text

	message.reply_text(f'```{data}```')
