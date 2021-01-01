import discord
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print('Info cog has been loaded sucessfully')

    # singular server info command 
    @commands.command(aliases=["servinfo", "sinfo"], no_pm=True)
    async def serverinfo(self, ctx):
        author = ctx.message.author
        server = ctx.message.guild
        guildicon = server.icon_url


        emb = discord.Embed(title=str(server), color=0x9966cc)
        emb.set_thumbnail(url=guildicon)
        emb.add_field(name="Server: ", value=server.name)
        emb.add_field(name="Owner: ", value=server.owner, inline=False)
        emb.add_field(name="Member count: ", value=server.member_count, inline=True)
        emb.add_field(name="Online members: ", value=sum(member.status!=discord.Status.offline and not member.bot for member in server.members), inline=False)
        emb.add_field(name="Voice channels: ", value=str(len([j for j in server.channels if type(j) == discord.channel.TextChannel])), inline=False)
        emb.add_field(name="Voice channels: ", value=str(len([j for j in server.channels if type(j) == discord.channel.VoiceChannel])), inline=False)
        emb.add_field(name="Emoji count:", value=str(len(server.roles)), inline=False)
        emb.add_field(name="Role count:", value=str(len(server.emojis)), inline=False)

        try:
            await ctx.send(author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")


def setup(bot):
    bot.add_cog(Info(bot))
