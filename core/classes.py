import discord
from discord.ext import commands

class Cog_Extensions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        