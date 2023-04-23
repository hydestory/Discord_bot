import discord
import json
import random
from discord.ext import commands
from core.classes import Cog_Extensions
with(open('setting.json','r',encoding='utf8')) as jfile:
    jdata=json.load(jfile)


class event(Cog_Extensions):

    @commands.Cog.listener() 
    async def member_join(self,member):
        channel = self.bot.get_channel(int(jdata['JOIN']))
        await channel.send(f'{member} has joined the server.')

    @commands.Cog.listener()                                                             
    async def member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['LEAVE']))
        await channel.send(f'{member} has left the server.')


    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = ['hi', 'hello', 'hey']
#or use content.endswith('hi') or content.endswith('hello') or content.endswith('hey')
        if msg.content in keyword and msg.author != self.bot.user:                  
            await msg.channel.send('Hello!')

#def setup(bot):
    #bot.add_cog(event(bot))