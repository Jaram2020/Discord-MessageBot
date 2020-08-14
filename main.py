import discord, asyncio
import time

from blackjack import BlackJack
from weather import Weather

bot = discord.Client()

async def msgEmbed(msg, title, description):
    embed = discord.Embed(title=title, description=description)
    return await msg.channel.send(embed=embed)

@bot.event
async def on_ready():
    print('Logged in as {0} {1}'.format(bot.user.name, bot.user.id))
    print('------')
    game = discord.Game("Simple Bot | $help")
    await bot.change_presence(status=discord.Status.online, activity=game)

    
@bot.event
async def on_message(msg):
    if "심심" in msg.content:
        await msg.channel.send("$blackjack")
        
    if msg.content == "$blackjack":
        game = BlackJack(msg, bot)
        await game.start()
        
    
    if msg.content.startswith("$weather"):
        message = msg.content.split(" ")
        show = Weather(msg, bot)
        if (len(message) == 1):
            await show.weather()
        else:
            await show.weather(message[1])
    
    if "날씨" in msg.content:
        message = msg.content.split("날씨")
        city = message[0].rstrip()
        city = city.split(' ')
        city = city[-1]
        # await msg.channel.send(message)
        show = Weather(msg, bot)
        await show.weather(city)
        # if (len(message) == 2):
        #     await show.weather(message[0])
        # else:
        #     await show.weather()

bot.run('your token')