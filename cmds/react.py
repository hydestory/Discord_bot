import discord
import json
import random
from discord.ext import commands
from core.classes import Cog_Extensions
import datetime
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

    @commands.command()
    async def botsay(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def profile(self,ctx):
        embed=discord.Embed(title="My profile", description="this is my profile", color=0x1fdba2,
                            timestamp=datetime.datetime.now())
        embed.set_author(name="Hydestory", icon_url="https://lh3.googleusercontent.com/r03KXBiBoG7_YYHPpHePJay2x9jXeO0ulvlwaIJZoiolm7j7OaEpJB2IiSSISZtjtfGEt6nJb54IkHTt5yx4xCnafPI7m2eWV4d0bCuSwOJKxHV0_keVR9H_tkwV3laBZaBdnY5OY_9GIkfWFuPet-rA7VNdrKo0gD57-ssKnvcvHdKbkhsrFY3JZ4uL2sFaZo8MUWtaWwPl0ilpjWLGbTv0I8vsDw0TbqURY3Y9nJnx8PbRe9TpE2PSVdaDONiMFIpKzob6_U_PvK0wlLL9jkB9gCKU2StzZGzO4HMq2gUR3Qk7Zfqz1wEJumPOaVMEKCuuRHb1oTYyW4_qdMy407R0N5ENT_lpBa-Ty4z38rvQfw2GZruCwFWhW_YBdEW9L_lZNZadkUO7dDW9rfyXsUXOUcmV7ShQn_J2zbVpwzc-dRCoV53wxaXqcynCVBvnPCl_0uiYpfkwGDBTFdS4WRUr6LVa4J-dAccYiNyLxBFOUdY1Hqtri-I9_-Kf9bY42fteV7l0oymCSrGinVcm_pdYtjI1c2xxWN9hRutI5h-5Al-5HGUDC7BevlFxiEVujdekhjAiS9292lROIRGgAQjsUZcFXSOKJ0ksJdkjt8SyhaqRtisV4d1sNaJg7pZdBq34jJ-KlBNbaSuRJS-wAagelsB8StEafpJMK6zZm8IRPl1Y1zabQnj6miWjhfQ-9QKT9B35WUtqFPfQrHFkjjRGYiGTenm_8QVbwe3emheAJenrEmsPRKqu_1ieon31wbYQ0mCzuLT4dEvqUEt2r58f-7j--05AwR8IJbbqc0KT2ktKTQ7XSMJag2KQuF2sPPRCBa_O4avbKjOVXJzmR8oQcplmfUcJHnbXj4dSUU3n_PWCIhhuxCoITSw3DKidG9PeNAy3nYWBiXd2vkZWAOJtcNIEJ3HeIT_R_WS8gA8QcC2MYxoJs5HAHDiOsoDGdSU5h1djnAfjvseRCw2RWyRqWcVTd6OOUmiLccU-odJzAB0F8Z7TGMc=w664-h376-s-no?authuser=0")
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/r03KXBiBoG7_YYHPpHePJay2x9jXeO0ulvlwaIJZoiolm7j7OaEpJB2IiSSISZtjtfGEt6nJb54IkHTt5yx4xCnafPI7m2eWV4d0bCuSwOJKxHV0_keVR9H_tkwV3laBZaBdnY5OY_9GIkfWFuPet-rA7VNdrKo0gD57-ssKnvcvHdKbkhsrFY3JZ4uL2sFaZo8MUWtaWwPl0ilpjWLGbTv0I8vsDw0TbqURY3Y9nJnx8PbRe9TpE2PSVdaDONiMFIpKzob6_U_PvK0wlLL9jkB9gCKU2StzZGzO4HMq2gUR3Qk7Zfqz1wEJumPOaVMEKCuuRHb1oTYyW4_qdMy407R0N5ENT_lpBa-Ty4z38rvQfw2GZruCwFWhW_YBdEW9L_lZNZadkUO7dDW9rfyXsUXOUcmV7ShQn_J2zbVpwzc-dRCoV53wxaXqcynCVBvnPCl_0uiYpfkwGDBTFdS4WRUr6LVa4J-dAccYiNyLxBFOUdY1Hqtri-I9_-Kf9bY42fteV7l0oymCSrGinVcm_pdYtjI1c2xxWN9hRutI5h-5Al-5HGUDC7BevlFxiEVujdekhjAiS9292lROIRGgAQjsUZcFXSOKJ0ksJdkjt8SyhaqRtisV4d1sNaJg7pZdBq34jJ-KlBNbaSuRJS-wAagelsB8StEafpJMK6zZm8IRPl1Y1zabQnj6miWjhfQ-9QKT9B35WUtqFPfQrHFkjjRGYiGTenm_8QVbwe3emheAJenrEmsPRKqu_1ieon31wbYQ0mCzuLT4dEvqUEt2r58f-7j--05AwR8IJbbqc0KT2ktKTQ7XSMJag2KQuF2sPPRCBa_O4avbKjOVXJzmR8oQcplmfUcJHnbXj4dSUU3n_PWCIhhuxCoITSw3DKidG9PeNAy3nYWBiXd2vkZWAOJtcNIEJ3HeIT_R_WS8gA8QcC2MYxoJs5HAHDiOsoDGdSU5h1djnAfjvseRCw2RWyRqWcVTd6OOUmiLccU-odJzAB0F8Z7TGMc=w664-h376-s-no?authuser=0")
        embed.add_field(name="name", value="hydestory", inline=True)
        embed.set_footer(text="this is a sample")
        await ctx.send(embed=embed)
    

#def setup(bot):
 #   bot.add.cog(react(bot))