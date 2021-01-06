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


        emb = discord.Embed(title=str(server), color=0x6b0080)
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
            await ctx.send(author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")

    # admin help command 
    @commands.command(aliases=["adhelp"])
    async def adminhelp(self, ctx):
        author = ctx.message.author

        emb = discord.Embed(title="Admin help", color=0x6b0080)
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=";;say channel", value=";;say channel <channel id> <message>", inline=False)
        emb.add_field(name=";;dm user", value=";;dm user <user id> <message> **(admin, manage messages, or bot owner only)**", inline=False)

        try:
            await ctx.send(author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")
    
    # singular help command to display the specific cog help commands
    @commands.command(aliases=["help"])
    async def helpcmd(self, ctx):
        author = ctx.message.author
        server = ctx.message.guild
        guildicon = server.icon_url

        emb = discord.Embed(title=str(server), color=0x6b0080)
        emb.set_thumbnail(url=guildicon)
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name="Main.py help", value=";;kill **(bot owner only)**\n;;loadcog cogs.<cogname> **(bot owner only)**\n;;unloadcog cogs.<cogname> **(bot owner only)**", inline=False)
        emb.add_field(name="cogs.Funshit help", value=";;shithelp or ;;funshithelp", inline=False)
        emb.add_field(name="cogs.Info help", value=";;serverinfo for server info", inline=False)
        emb.add_field(name="cogs.Math help", value=";;mathhelp or mhelp", inline=False)
        emb.add_field(name="cogs.Code help", value=";;codeinfo or ;;cinfo", inline=False)
        emb.add_field(name="cogs.Admin help", value=";;adminhelp or ;;adhelp", inline=False)

        try:
            await ctx.send(author, embed=emb)
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
            await ctx.send(author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")

    # funshit help command
    @commands.command(aliases=["fshithelp", "shithelp"])
    async def funshithelp(self, ctx):
        author = ctx.message.author

        emb = discord.Embed(title="Fun shit help", color=0x6b0080)
        emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        emb.add_field(name=";;howgay", value=";;howgay <username or name>")
        emb.add_field(name=";;nitropls", value="generates random nitro url (probably won't work)")

        try:
            await ctx.send(author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")

    # math help command
    @commands.command(aliases=["mhelp"])
    async def mathhelp(self, ctx):
        author = ctx.message.author

        emb = discord.Embed(title="Math help", color=0x6b0080)
        emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        emb.add_field(name=";;+", value=";;add <number 1> <number 2>")

        try:
            await ctx.send(author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")

def setup(bot):
    bot.add_cog(Info(bot))
