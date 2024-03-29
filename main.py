import discord
import os
import ngrok
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
    if message.author.name == "opium":
        return
    
    msg = message.content

    if msg.startswith('p'):
        await message.channel.send('im on')

    if msg.startswith('q'):
        text = msg.partition(' ')[2]
        print("lookin for: " + text)
        msg = chat(text)
        resulting_chunks = split_text_into_array(msg, 2000)

        for idx, chunk in enumerate(resulting_chunks):
            await message.channel.send(chunk)

    if msg.startswith('g'):
        text = msg.partition(' ')[2]
        print("drawing for: " + text)
        await message.channel.send(img(text))

    if msg.startswith('ngrok'):
        client = ngrok.Client("2RH60jgdU6eU6qeZXR1iKLWu0uH_5SBdsAv1xs7UMTd8WQn7g")
        for t in client.tunnels.list():
            await message.channel.send(t.public_url + " -> " + t.forwards_to)


def split_text_into_array(text, max_words_per_chunk):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(" ".join(current_chunk + [word])) > max_words_per_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

        current_chunk.append(word)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

try:
    client.run(os.getenv("BOT_TOKEN"))
    # keep_alive()
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
      