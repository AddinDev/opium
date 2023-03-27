import discord
import os
from gpt import *
from dotenv import load_dotenv

load_dotenv()
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    if msg.startswith('p'):
        await message.channel.send('im on')

    if msg.startswith('q'):
        text = msg.partition(' ')[2]
        print("lookin for: " + text)
        await message.channel.send(chat(text))

    if msg.startswith('g'):
        text = msg.partition(' ')[2]
        print("drawing for: " + text)
        await message.channel.send(img(text))

try:
    client.run(os.getenv("BOT_TOKEN"))
    # keep_alive()
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
      