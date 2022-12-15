# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import time

description = '''An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here.'''

token = "MTA1Mjc5Mzk0ODA4NDY0NTkzMQ.GqETAx.PB6UrhCSF3dh_XSvAbTFmyzw_6-Lo_-fikPov4"
command_prefix = '$'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=command_prefix, description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def chirp(ctx):
    """chirps at users"""
    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send("chirp.... user not in channel")
        return
        
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio("audio/CricketSound.mp4"))
    time.sleep(5)
    await ctx.voice_client.disconnect()
    

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('chirp... format has to be in NdN')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


bot.run(token)