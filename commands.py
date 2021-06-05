import discord
from discord.utils import get
import requests
import json

async def greet(message, client):
  await message.channel.send('Hello {0.author}!'.format(message))
  emoji = '\N{THUMBS UP SIGN}'
  await message.add_reaction(emoji) 

async def quote(message, client):
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  await message.channel.send(quote)