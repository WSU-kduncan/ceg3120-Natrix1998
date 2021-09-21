import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()

#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')

 #   for guild in client.guilds:
  #      if guild.name == GUILD:
   #         break
#
 #   print(
  #      f'{client.user} is connected to the following guild:\n'
   #     f'{guild.name}(id: {guild.id})'
    #)
bot = commands.Bot(command_prefix='!')
@bot.command(name='uncle')
async def on_message(ctx):
    iroh_quotes = [
        'Sick of tea? That\'s like being sick of breathing.',
        'Are you so busy fighting you cannot see your own ship has set sail?',
        'In the darkest times, hope is something you give yourself.',
        'Pride is not the opposite of shame, but its source. True humility is the only antidote to shame.'
    ]

    #hitchhiker_quotes = [
    #   'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
    #   'It is a mistake to think you can solve any major problems just with potatoes.',
    #   'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
    #   'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    # ]

    
    response = random.choice(iroh_quotes)
    await ctx.send(response)

bot.run(TOKEN)
