import os
import discord
from commands import *
import random
from replit import db


client = discord.Client()


sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!"
]

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len (encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  options = starter_encouragements
  if "encouragements" in db.keys():
    for enc in db["encouragements"]:
      options.append(enc)

  if msg.startswith('!greet'):
    await greet(message, client)

  if msg.startswith('!quote'):
    await quote(message, client)

  if msg.startswith('!new'):
    encouraging_message = msg.split("!new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added")

  if msg.startswith('!delete'):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("!delete ",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith('!all'):
    encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

my_secret = os.environ['TOKEN']
client.run(my_secret)