import discord
from discord.ext import commands

class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Math runner cog has been loaded sucessfully')

    @commands.command(aliases=["+"])
    async def add(self, ctx, num1, num2):
        if num1!=None and num2!=None:
            await ctx.send(int(num1)+int(num2))

    

def setup(bot):
    bot.add_cog(Math(bot))
