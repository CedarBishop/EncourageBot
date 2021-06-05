import os
import discord
from commands import *
import random


client = discord.Client()


sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!"
]

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!greet'):
    await greet(message, client)

  if message.content.startswith('!quote'):
    await quote(message, client)

my_secret = os.environ['TOKEN']
client.run(my_secret)