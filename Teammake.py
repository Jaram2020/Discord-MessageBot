import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$", activity=discord.Activity(name="Teammake | $help", type=1))

class Teammake(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
    async def on_message(self, message):
        teampool = message.split(',')
        Ateam = []
        Bteam = []
        if (len(teampool) == 4):
            for i in range(2):
                random.shuffle(teampool)
                Ateam.append(teampool[0])
                teampool = teampool[1:]
                Bteam.append(teampool[0])
                teampool = teampool[1:]
            embed = discord.Embed(title = "Teammake complete", description = "Ateam: "+Ateam + '\n' + "Bteam: "+Bteam)
        elif (len(teampool) == 6):
            for i in range(3):
                random.shuffle(teampool)
                Ateam.append(teampool[0])
                teampool = teampool[1:]
                Bteam.append(teampool[0])
                teampool = teampool[1:] 
            embed = discord.Embed(title = "Teammake complete", description = "Ateam: "+Ateam + '\n' + "Bteam: "+Bteam)
                
        elif (len(teampool) == 8):
            for i in range(4):
                random.shuffle(teampool)
                Ateam.append(teampool[0])
                teampool = teampool[1:]
                Bteam.append(teampool[0])
                teampool = teampool[1:]
            embed = discord.Embed(title = "Teammake complete", description = "Ateam: "+Ateam + '\n' + "Bteam: "+Bteam)
        elif (len(teampool) == 10):
            for i in range(5):
                random.shuffle(teampool)
                Ateam.append(teampool[0])
                teampool = teampool[1:]
                Bteam.append(teampool[0])
                teampool = teampool[1:]
            embed = discord.Embed(title = "Teammake complete", description = "Ateam: "+Ateam + '\n' + "Bteam: "+Bteam)
        
        await message.send(embed=embed)
        
bot.add_cog(Teammake(bot))

bot.run('your token')