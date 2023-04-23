import discord
from discord.ext import commands
import json,asyncio,datetime
from core.classes import Cog_Extensions

class task(Cog_Extensions):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(1097490266329469040)
            while not self.bot.is_closed():
                await self.channel.send('test')
                await asyncio.sleep(5)
        
        self.bg_task = self.bot.loop.create_task(interval())

    
    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')