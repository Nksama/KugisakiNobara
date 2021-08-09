import requests
from SaitamaRobot import pbot
from pyrogram import filters
import os


@pbot.on_message(filters.command("github"))
def git(_,message):
    user = message.text.replace(message.text.split(' ')[0], '')
    res = requests.get(f"https://api.github.com/users/{user}").json()

    with open("test.jpg" , "wb") as f:
        f.write(res.content)


    data = f"""
**Name**: {res['name']}
**Username**: {res['login']}
**Location**: {res['location']}
**Bio**: {res['bio']}
**Public Repos**: {res['public_repos']}
**Location**: {res['location']}
**Followers**: {res['followers']}
**Following**: {res['following']}
"""
    pbot.send_photo(message.chat.id , "test.jpg" , caption=data , parse_mode="markdown")
    os.remove("test.jpg")


