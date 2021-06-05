import os
import discord
from commands import *

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!greet'):
    await greet(message, client)

my_secret = os.environ['TOKEN']
client.run(my_secret)