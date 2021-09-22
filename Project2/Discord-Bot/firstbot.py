import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')
@bot.command(name='uncle')
async def on_message(ctx):
    iroh_quotes = [
        'Sick of tea? That\'s like being sick of breathing.',
        'Are you so busy fighting you cannot see your own ship has set sail?',
        'In the darkest times, hope is something you give yourself.',
        'Pride is not the opposite of shame, but its source. True humility is the only antidote to shame.'
    ]
    response = random.choice(iroh_quotes)
    await ctx.send(response)
@bot.command(name='turmoil')
async def on_message(ctx):
    zuko_quotes = [
        'HONOR!',
        'Hello, Zuko here!',
        'The scar IS NOT on the wrong side!',
        'That\'s rough buddy.',
    ]
    response = random.choice(zuko_quotes)
    await ctx.send(response)
bot.run(TOKEN)
