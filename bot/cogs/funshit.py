import string
import random
import discord
import requests
from discord.ext import commands

# gayness check
def percentIsGay(args):
    gayletters = ["g","a","y","m","i","c","h","a","e","l","p","n","s","G","A","Y","M","I","C","H","A","E","L","P","N","S"]
    barelygayletters = ["x","u","r","w","z","j","k"]
    gayness = 0

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in gayletters:
            gayness += 1
        wordlen += 1

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in barelygayletters:
            gayness += 0.4
        wordlen += 1

    return (args + " is " + str((gayness/len(args))*100) + "% gay")

# gayness check without sentence
def otherpercentIsGay(args):
    gayletters = ["g","a","y","m","i","c","h","a","e","l","p","n","s","G","A","Y","M","I","C","H","A","E","L","P","N","S"]
    barelygayletters = ["x","u","r","w","z","j","k"]
    gayness = 0

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in gayletters:
            gayness += 1
        wordlen += 1

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in barelygayletters:
            gayness += 0.4
        wordlen += 1

    return int(gayness/len(args)*100)

# generates nitro code
def classicNitro():
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    classic_nitro_url = "https://discord.gift/" + code

    api_url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true"
    
    api_status = requests.get(api_url)
    if api_status.status_code ==  200:
        validity = "valid code"
        return(classic_nitro_url+"\n"+validity)
    else:
        validity = "not valid"
        return(classic_nitro_url+"\n"+validity)

# generates nitro code
def boostNitro():
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(24))
    boost_nitro_url = "https://discord.gift/" + code

    api_url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true"

    api_status = requests.get(api_url)
    if api_status.status_code ==  200:
        validity = "valid code"
        return(boost_nitro_url+"\n"+validity)
    else:
        validity = "not valid"
        return(boost_nitro_url+"\n"+validity)
# main
class Funshit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Funshit cog has been loaded sucessfully')

    @commands.command()
    async def howgay(self, ctx, args=None):
        if args!=None:
            isgay = percentIsGay(args)
            await ctx.send(isgay)
    
    @commands.command()
    async def wouldtheyfuck(self, ctx, p1, p2):
        gayperson1 = otherpercentIsGay(str(p1))
        gayperson2 = otherpercentIsGay(str(p2))
        wouldthey = (gayperson1+gayperson2)/2
        if (wouldthey > 70):
            await ctx.send("they will fucking peg each other to death")
        elif (50 <= wouldthey <=70):
            await ctx.send("they will fuck")
        elif (wouldthey < 49):
            await ctx.send("homie can't even get his dick hard :(")

    @commands.command(aliases=["cnitropls"])
    async def classicnitropls(self, ctx):
        await ctx.send(classicNitro())

    @commands.command(aliases=["bnitropls", "nitropls", "nitro"])
    async def boostnitropls(self, ctx):
        await ctx.send(boostNitro())

def setup(bot):
    bot.add_cog(Funshit(bot))
