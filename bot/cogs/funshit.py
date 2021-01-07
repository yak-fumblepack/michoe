import string
import random
import discord
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
def nitro():
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    nitro_url = "https://discord.gift/" + code
    return(nitro_url)

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

    @commands.command()
    async def nitropls(self, ctx):
        await ctx.send(nitro())

def setup(bot):
    bot.add_cog(Funshit(bot))
