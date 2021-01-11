import discord
from discord.utils import get
from discord.ext import commands
import os
import youtube_dl

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Music cog has been loaded sucessfully')

    @commands.command(aliases=["jvc", "vc", "join"])
    async def joinvc(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            print(f"connected to {channel}\n")

        await ctx.send(f"joined {channel}")

    @commands.command(aliases=["p"])
    async def play(self, ctx, url:str):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                print("removed old song file")
        except PermissionError:
            print("trying to delete song file, but it's being played")
            await ctx.send("can't delete, music file is playing")
            return

        await ctx.send("downloading song")

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("downloading audio now\n")
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"renamed file: {file}\n")
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07

        new_name = name.rsplit("-", 2)
        await ctx.send(f"done! playing: {new_name[0]}")
        print("playing\n")
        
def setup(bot):
    bot.add_cog(Music(bot))
