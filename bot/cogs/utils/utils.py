import discord
from discord.ext import commands

class Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Utility cog has been loaded sucessfully')

    @commands.command(aliases=["clear", "purgemsg", "purge"])
    async def clearmsg(self, ctx, msg_count=None):
        if msg_count=='all':
            await ctx.channel.purge(limit=99999)
        elif msg_count!=None:
            await ctx.channel.purge(limit=int(msg_count))


def setup(bot):
    bot.add_cog(Utils(bot))
