import discord
import json
import openai

from discord.ext import commands
from core.classes import Cog_Extensions


with(open('setting.json','r',encoding='utf8')) as jfile:
    jdata=json.load(jfile)


memory = []
openai.api_key = jdata['OPENAI_API_KEY']

class main(Cog_Extensions):

    @commands.command()
    async def ping(self,ctx):
        '''Ping the bot'''
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def hello(self,ctx):
        await ctx.send('Hello!')

    @commands.command()
    async def info(self,ctx, *, member: discord.Member):
        """Tells you some info about the member."""
        msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
        await ctx.send(msg)

    @info.error
    async def info_error(self,ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...')

    @commands.command()
    async def clean(self,ctx, num: int):
        '''Clean the chat'''
        await ctx.channel.purge(limit=num+1)
    
    @commands.command()
    async def ask(self,ctx, *, question):
        '''Ask the bot a question use GPT-3.5 Turbo'''
        
        global memory
            # 将先前的问题和答案添加到上下文中
        conversation = "\n".join(memory)

        # 调用 GPT-3.5 Turbo 来回答问题
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{conversation}\nUser: {question}\nAI:",
            temperature=0.5,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        answer = response.choices[0].text.strip()

        # 将问题和答案添加到记忆中
        memory.append(f"User: {question}")
        memory.append(f"AI: {answer}")

        # 如果记忆超过 token 限制，删除早期的对话片段
        while sum(len(line) + 1 for line in memory) > 4096:
            memory.pop(0)
            memory.pop(0)

        await ctx.send(answer)
#def setup(bot):
 #   bot.add_cog(main(bot))