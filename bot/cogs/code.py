import json
import time
import urllib.error
import urllib.parse
import urllib.request

import discord
from discord.ext import commands


class Code(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # displays ready message on load
    @commands.Cog.listener()
    async def on_ready(self):
        print('Code runner cog has been loaded sucessfully')

    @commands.command(aliases=["run"])
    async def runcode(self, ctx, lang=None, *, args=None):
        author = ctx.message.author
        if lang!=None and args!=None:

            # sends data to rextester.com 
            # rextester requires it to be formatted this way more info -> (https://rextester.com/main)
            api_url = 'https://rextester.com/rundotnet/api'
            postdata = urllib.parse.urlencode({
                'LanguageChoice': lang,
                'Program': args,
                'Input': "",
                'CompilerArgs': "-o a.out source_file.cpp"
            })

            # supplying values
            pdbytes = str.encode(postdata)
            request = urllib.request.Request(api_url, pdbytes)
            response = urllib.request.urlopen(request)
            output = response.read()

            # decode json strings
            response_decoded = json.loads(output)
            comp_warnings = response_decoded["Warnings"]
            comp_errors = response_decoded["Errors"]
            comp_results = response_decoded["Result"]
            comp_status = response_decoded["Stats"]

            # displays the status of the compilation 
            emb = discord.Embed(title="Running code", color=0x6b0080)
            emb.add_field(name="Called by: ", value="{}".format(author))
            emb.add_field(name="Compilation Warnings: ", value="```{}```".format(comp_warnings), inline=False)
            emb.add_field(name="Compilation Errors: ", value="```{}```".format(comp_errors), inline=False)
            emb.add_field(name="Compilation Status: ", value="```{}```".format(comp_status), inline=False)
            emb.add_field(name="Compilation Results: ", value="```{}```".format(comp_results), inline=False)
            emb.set_footer(text="Running using the rextester api")

            try:
                await ctx.send(embed=emb)
            except:
                await ctx.send("Sorry there was an error processing this command")
        else:
            await ctx.send("Please provide the correct input: run ;;codeinfo to see more")

def setup(bot):
    bot.add_cog(Code(bot))
