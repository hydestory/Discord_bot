import discord
from discord.ext import commands
import json

with(open('setting.json','r',encoding='utf8')) as jfile:
    jdata=json.load(jfile)


intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def member_join(member):
    channel = bot.get_channel(int(jdata['JOIN']))
    await channel.send(f'{member} has joined the server.')

@bot.event
async def member_remove(member):
    channel = bot.get_channel(int(jdata['LEAVE']))
    await channel.send(f'{member} has left the server.')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


bot.run(jdata['TOKEN'])

