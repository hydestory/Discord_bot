import discord
from discord.ext import commands
import json
import random
import os
from cmds.main import main
from cmds.react import react

with(open('setting.json','r',encoding='utf8')) as jfile:
    jdata=json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.add_cog(main(bot))
    await bot.add_cog(react(bot))
    print('Bot is ready.')

@bot.event
async def member_join(member):
    channel = bot.get_channel(int(jdata['JOIN']))
    await channel.send(f'{member} has joined the server.')

@bot.event
async def member_remove(member):
    channel = bot.get_channel(int(jdata['LEAVE']))
    await channel.send(f'{member} has left the server.')




if __name__ == "__main__":
    bot.run(jdata['TOKEN'])

