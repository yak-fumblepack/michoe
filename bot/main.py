import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# basic settings
load_dotenv()
token = os.getenv("token")

bot = commands.Bot(command_prefix=';;', help_command=None)

cogs = [
    'cogs.info',
    'cogs.code',
    'cogs.math',
    'cogs.funshit',
    'cogs.utils.admin',
    'cogs.utils.utils',
    'cogs.music.music'
    ]

for cog in cogs:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f'Could not load cog {cog}: {str(e)}')




# main 

@bot.event
async def on_ready():
    print('Bot is running')

# load and unload cogs for modularity purposes 
@bot.command()
@commands.is_owner()
async def loadcog(ctx, cogname=None):
    if cogname == None:
        return
    try:
        bot.load_extension(cogname)
    except Exception as e:
        print(f'Could not load cog {cogname}: {str(e)}')
        await ctx.send(f'Could not load cog {cogname}: {str(e)}')
    else: 
        print(f'Loaded cog: {cogname} sucessfully')
        await ctx.send(f'Loaded cog: {cogname} sucessfully')

@bot.command()
@commands.is_owner()
async def unloadcog(ctx, cogname=None):
    if cogname == None:
        return
    try:
        bot.unload_extension(cogname)
    except Exception as e:
        print(f'Could not unload cog {cogname}: {str(e)}')
        await ctx.send(f'Could not unload cog {cogname}: {str(e)}')
    else: 
        print(f'Unloaded cog: {cogname} sucessfully')
        await ctx.send(f'Unloaded cog: {cogname} sucessfully')


@bot.command()
@commands.is_owner()
async def kill(ctx):
    await bot.logout()


@bot.command()
async def ginfo(ctx):
    for guild in bot.guilds:
        emb = discord.Embed(title=str(guild), color=0x9966cc)
        emb.set_thumbnail(url=guild.icon_url)
        emb.add_field(name="Owner:", value=guild.owner, inline=False)
        emb.add_field(
            name="Member count:", value=guild.member_count, inline=False)
        await ctx.send(embed=emb)

@bot.command()
async def probeserver(ctx, serverid=None):
    if serverid!=None:
        guild = await bot.fetch_guild(int(serverid))
        emb = discord.Embed(title=str(guild), color=0x9966cc)
    
        await ctx.send(embed=emb)

bot.run(token)
