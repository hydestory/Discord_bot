import discord
import json
import random
from discord.ext import commands
from core.classes import Cog_Extensions
with(open('setting.json','r',encoding='utf8')) as jfile:
    jdata=json.load(jfile)


class react(Cog_Extensions):

    @commands.command()
    async def 蛇蛇(self,ctx):
        await ctx.send('嘶嘶')
        await ctx.send(file=discord.File(jdata["GECKO"]))

    @commands.command()
    async def mumei(self,ctx):
        selected_image = random.choices(jdata["MUMEI"], k=1)[0]
        await ctx.send(file=discord.File(selected_image))



def setup(bot):
    bot.add.cog(react(bot))