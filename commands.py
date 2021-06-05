import discord
from discord.utils import get

async def greet(message, client):
  await message.channel.send('Hello {0.author}!'.format(message))
  emoji = '\N{THUMBS UP SIGN}'
  await message.add_reaction(emoji) 