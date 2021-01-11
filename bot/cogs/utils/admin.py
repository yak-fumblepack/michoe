import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin cog has been loaded sucessfully')

    @commands.command()
    async def say(self, ctx, dm_type=None, dm_id=None, *, args=None):
        if dm_type == 'channel' and dm_id!=None:
            try: 
                target = await self.bot.fetch_channel(dm_id)
                await target.send(args)
                await ctx.message.delete()
                await ctx.send("sent")
            except:
                await ctx.send("Error could not dm the channel")
        else:
            await ctx.send("Failed to specify channel, channelid")
    
    @commands.command()
    @commands.check_any(commands.is_owner(), commands.has_permissions(administrator=True), commands.has_permissions(manage_messages=True), commands.has_role("william?"))
    async def dm(self, ctx, dm_type=None, dm_id=None, *, args=None):
        if dm_type == 'user' and dm_id!=None:
            try: 
                target = await self.bot.fetch_user(dm_id)
                await target.send(args)
                await ctx.message.delete()
                await ctx.send("sent")
            except:
                await ctx.send("Error could not dm the user")
        else:
            await ctx.send("Failed to specify user, userid or you're lacking the permission")

def setup(bot):
    bot.add_cog(Admin(bot))