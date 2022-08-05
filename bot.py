# bot.py
import os
import random
import time
from warnings import catch_warnings

## bot.py uses discords bot API which is a subclass of client ##

# discord specific imports needed
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# creates the bot with a specified command prefix
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# joining voice channel
@bot.command(name='join', help='joins voice channel that user is in')
async def join(ctx):
    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send('User is not in a channel.')
    else:
        await channel.connect()

# leaving voice channel
@bot.command(name='leave', help='leaves voice channel')
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command(name='chirp', help='plays cricket chirping')
async def chirp(ctx):
    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send('User is not in a channel.')
    else:
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audio/CricketSound.mp4"))
        time.sleep(5)
        await ctx.voice_client.disconnect()


bot.run(TOKEN)
