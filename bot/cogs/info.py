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
        emb.add_field(name="Voice channels: ", value=str(len([j for j in server.channels if type(j) == discord.channel.TextChannel])), inline=False)
        emb.add_field(name="Voice channels: ", value=str(len([j for j in server.channels if type(j) == discord.channel.VoiceChannel])), inline=False)
        emb.add_field(name="Emoji count:", value=str(len(server.roles)), inline=False)
        emb.add_field(name="Role count:", value=str(len(server.emojis)), inline=False)

        try:
            await ctx.send(author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")

    # code running help command
    @commands.command(aliases=["helpcode", "cinfo"])
    async def codeinfo(self, ctx):
        author = ctx.message.author
        emb = discord.Embed(title="Code running info", color=0x6b0080, 
        description= 
        """
        ```asciidoc\n
            == Languages == 
            C# = 1
            VB.NET = 2
            F# = 3
            Java = 4
            Python = 5
            C (gcc) = 6
            C++ (gcc) = 7
            Php = 8
            Pascal = 9
            Objective-C = 10
            Haskell = 11
            Ruby = 12
            Perl = 13
            Lua = 14
            Nasm = 15
            Sql Server = 16
            Javascript = 17
            Lisp = 18
            Prolog = 19
            Go = 20
            Scala = 21
            Scheme = 22
            Node.js = 23
            Python 3 = 24
            Octave = 25
            C (clang) = 26
            C++ (clang) = 27    
            C++ (vc++) = 28
            C (vc) = 29
            D = 30
            R = 31
            Tcl = 32
            MySQL = 33
            PostgreSQL = 34
            Oracle = 35
            Swift = 37
            Bash = 38
            Ada = 39
            Erlang = 40
            Elixir = 41
            Ocaml = 42
            Kotlin = 43
            Brainf*** = 44
            Fortran = 45,
            Rust = 46,
            Clojure = 47
            ==================
            - To run the command:
        
            ;;runcode <the language number> <your code> 

        ```
        """)
        try:
            await ctx.send(author, embed=emb)
        except:
            await ctx.send("Sorry there was an error processing this command")


def setup(bot):
    bot.add_cog(Info(bot))
