import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def member_join(member):
    channel = bot.get_channel(1097490266329469040)
    await channel.send(f'{member} has joined the server.')

@bot.event
async def member_remove(member):
    channel = bot.get_channel(1097490307551068221)
    await channel.send(f'{member} has left the server.')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


bot.run('MTA5NzE3MTAzOTcyMjY2ODI2Mg.Gb3BEM.ttNz0jDuMWb63kfJ4C99vjrB7FTthh841liM2I')

