from SaitamaRobot import pbot
from pyrogram import filters
import redis #redis is requirements

r = redis.Redis(
    host=os.environ.get("REDIS_URL"), # get it from redislabs.com and remove the last 4 numbers in the url after ":"
    port=os.environ.get("PORT"), # last 4 numbers
    password=os.environ["REDIS_PASSWORD"],
    decode_responses=True
)

@bot.on_message(filters.command('addchat'))
def addchat(_,message):
	r.set(message.chat.id , True)
    

@bot.on_message(filters.command('rmchat'))
def addchat(_,message):
	r.set(message.chat.id , False)

@bot.on_message(filters.text)
def chatbot(_,message):
	text = message.text
	kek = r.get(message.chat.id)
    if kek and "/" not in text:
      res = requests.get(f"https://kuki.up.railway.app/Kuki/chatbot?message={text}").json()
      reply = res['reply']
      message.reply_text(reply)
