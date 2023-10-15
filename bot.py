import discord
from discord.ext import commands
import json
from cmds.main import main
from cmds.react import react
from cmds.event import event
from cmds.task import task

with(open('setting.json','r',encoding='utf8')) as jfile:
    jdata=json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    cogs = [main, react, event, task]
    for cog in cogs:
        bot.add_cog(cog(bot))
    print('Bot is ready.')

@bot.command()
async def unload(ctx, cog):
    await bot.remove_cog(f'cmds.{cog}')
    await ctx.send(f'Unload {cog} done.')

@bot.command()
async def load(ctx, cog):
    await bot.add_cog(f'cmds.{cog}')
    await ctx.send(f'Load {cog} done.')



if __name__ == "__main__":
    bot.run(jdata['TOKEN'])

