import string
import random
import requests
import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO

# gayness check
def percentIsGay(args):
    gayletters = ["g","a","y","j","o","r","d"]
    barelygayletters = ["x","u","r","w","z","j","k"]
    sortagayletters = ["p", "m", "i", "q"]
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

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in sortagayletters:
            gayness += 0.6
        wordlen += 1

    return (args + " is " + str((gayness/len(args))*100) + "% gay")

# gayness check without sentence
def otherpercentIsGay(args):
    gayletters = ["g","a","y","j","o","r","d"]
    barelygayletters = ["x","u","r","w","z","j","k"]
    sortagayletters = ["p", "m", "i", "q"]
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

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in sortagayletters:
            gayness += 0.6
        wordlen += 1

    return int(gayness/len(args)*100)


# gayness check without sentence
def hoemuch(args):
    hoeletters = ["s","l","u","t","b","i", "a", "h", "n"]
    barelyhoeletters = ["c","o","e","k"]
    sortahoeletters = ["p", "m", "i", "q"]
    hoeness = 0

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in hoeletters:
            hoeness += 1
        wordlen += 1

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in barelyhoeletters:
            hoeness += 0.5
        wordlen += 1

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in sortahoeletters:
            hoeness += 0.7
        wordlen += 1

    hoenessness = int(hoeness/len(args)*100)
    
    return hoenessness


# generates nitro code
def classicNitro():
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    classic_nitro_url = "https://discord.gift/" + code

    api_url = "https://discordapp.com/api/v8/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true"
    
    api_status = requests.get(api_url)
    if api_status.status_code ==  200:
        validity = "valid code"
        return(classic_nitro_url+"\n"+validity)
    else:
        validity = "could not generate a valid code, try again"
        return(validity)

# generates nitro code
def boostNitro():
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(24))
    boost_nitro_url = "https://discord.gift/" + code

    api_url = "https://discordapp.com/api/v8/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true"

    api_status = requests.get(api_url)
    if api_status.status_code ==  200:
        validity = "valid code"
        return(boost_nitro_url+"\n"+validity)
    else:
        validity = "could not generate a valid code, try again"
        return(validity)

class Funshit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Funshit cog has been loaded sucessfully')

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.id != message.author.id:  
            if 'uwu' in message.content:
                await message.channel.send("daddy harder please :weary:")
        
            if message.content.startswith("."):
                await message.channel.send('.')
        
            if message.content.startswith("kkk"):
                await message.channel.send(file=discord.File("images/kkk.PNG"))

            if message.content.startswith("bitch ass hoe") or message.content.startswith("HOE") or message.content.startswith("hoe"):
                for i in range(5):
                    await message.channel.send('hoes mad')    
            await self.bot.process_commands(message)

    @commands.command()
    async def howgay(self, ctx, *, args=None):
        if args!=None:
            isgay = percentIsGay(args)
            await ctx.send(isgay)

    @commands.command()
    async def hoe(self, ctx, *, args=None):
        if args!=None:
            ishoe = hoemuch(args)
            if (ishoe > 70):
                await ctx.send(file=discord.File("images/t.PNG"))
            elif (40 < ishoe <= 70):
                await ctx.send(file=discord.File("images/tier1hoe.jpg"))
            else:
                await ctx.send(file=discord.File("images/tier2hoe.jpg"))

    @commands.command()
    async def wouldtheyfuck(self, ctx, p1, p2):
        gayperson1 = otherpercentIsGay(str(p1))
        gayperson2 = otherpercentIsGay(str(p2))
        wouldthey = (gayperson1+gayperson2)/2
        if (wouldthey > 65):
            await ctx.send("they will fucking peg each other to death")
        elif (50 <= wouldthey <=65):
            await ctx.send("they will fuck")
        elif (wouldthey < 49):
            await ctx.send("homie can't even get his dick hard :(")

    @commands.command()
    async def kkk(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        kkkimg = Image.open("images/kkk.PNG")
        asset = user.avatar_url(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((72, 60))
        kkkimg.paste(pfp, (310, 152))
        kkkimg.save("images/kkkprofile.jpg")
        await ctx.send(file=discord.File("images/kkkprofile.jpg"))

    @commands.command(aliases=["cnitropls"])
    async def classicnitropls(self, ctx):
        await ctx.send(classicNitro())

    @commands.command(aliases=["bnitropls", "nitropls", "nitro"])
    async def boostnitropls(self, ctx):
        await ctx.send(boostNitro())

    

def setup(bot):
    bot.add_cog(Funshit(bot))