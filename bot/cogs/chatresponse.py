import os
import sys
import discord
from discord.ext import commands

class Chatresponse(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.triggers = []
        self.responses = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('Chat response cog has been loaded sucessfully')
        chatresponsechannel = self.bot.get_channel(int(os.getenv("chatresponsechannel")))
        messagelist = []
        messagelist = await chatresponsechannel.history(limit=sys.).flatten()

def setup(bot):
    bot.add_cog(Chatresponse(bot))
