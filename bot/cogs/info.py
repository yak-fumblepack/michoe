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
        emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        emb.set_thumbnail(url=guildicon)
        emb.add_field(name="Server: ", value=server.name)
        emb.add_field(name="Owner: ", value=server.owner, inline=False)
        emb.add_field(name="Member count: ", value=server.member_count, inline=True)
        emb.add_field(name="Voice channels: ", value=str(len([j for j in server.channels if type(j) == discord.channel.TextChannel])), inline=False)
        emb.add_field(name="Voice channels: ", value=str(len([j for j in server.channels if type(j) == discord.channel.VoiceChannel])), inline=False)
        emb.add_field(name="Emoji count:", value=str(len(server.roles)), inline=False)
        emb.add_field(name="Role count:", value=str(len(server.emojis)), inline=False)

        try:
            await ctx.send("called by:", author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")

    # code running help command
    @commands.command(aliases=["helpcode", "cinfo"])
    async def codeinfo(self, ctx):
        author = ctx.message.author

        emb = discord.Embed(title="Code running info", color=0x6b0080)
        emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        emb.add_field(name="Supported languages", value="ada\nassembly\nbash\nc#\nc\nc++\nclojure\nd\nlisp\nelixir\nerlang\nf#\nfortran\ngo\nhaskell\njava\njavascript\nkotlin\nlua\nocaml\noctave\nperl\nprolog\npython\npython3\nr\nrust\nruby\nscala\nscheme\nswift\ntcl\nvb (visual basic)\n")

        try:
            await ctx.send("called by:", author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")


def setup(bot):
    bot.add_cog(Info(bot))
