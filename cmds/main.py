import discord
import json
import random
from discord.ext import commands
from core.classes import Cog_Extensions
with(open('setting.json','r',encoding='utf8')) as jfile:
    jdata=json.load(jfile)


class main(Cog_Extensions):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def hello(self,ctx):
        await ctx.send('Hello!')

    @commands.command()
    async def reload(self,ctx,extension):
        await self.bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'Reloaded {extension} done.')

    @commands.command()
    async def info(self,ctx, *, member: discord.Member):
        """Tells you some info about the member."""
        msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
        await ctx.send(msg)

    @info.error
    async def info_error(self,ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...')

def setup(bot):
    bot.add_cog(main(bot))