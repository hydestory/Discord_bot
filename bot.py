import discord
from discord.ext import commands
import json
import random

with(open('setting.json','r',encoding='utf8')) as jfile:
    jdata=json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True
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

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def 蛇蛇(ctx):
    await ctx.send('嘶嘶')
    await ctx.send(file=discord.File(jdata["GECKO"]))

@bot.command()
async def mumei(ctx):
    selected_image = random.choices(jdata["MUMEI"], k=1)[0]
    await ctx.send(file=discord.File(selected_image))
    


bot.run(jdata['TOKEN'])

