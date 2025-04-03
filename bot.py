import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    """Prints a hello message."""
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command("roll")
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command("heh")
async def heh(ctx, count_heh = 5):
    """Prints the syllable 'he' multiplied by the desired amount of times."""
    await ctx.send("he" * count_heh)

def get_duck_image_url():    
    url = 'https://randomfox.ca/floof'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command('duck')
async def duck(ctx):
    """Prints an url to a fox image"""
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command("info")
async def info(ctx):
    """Shows a bit of info regarding the bot (not the same as help command)"""
    await ctx.send("Sample Discord bot running in Python 3.11, created by Legofan123e.")
bot.run("token")