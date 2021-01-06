import os

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

import asyncio
import io
import os
import random
import urllib.parse
import urllib.request

from PIL import Image

# basic settings
load_dotenv()
token = os.getenv("token")

bot = commands.Bot(command_prefix=';;')
bot.remove_command("help")

cogs = [
    'cogs.info',
    'cogs.code',
    'cogs.math',
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

bot.run(token)
