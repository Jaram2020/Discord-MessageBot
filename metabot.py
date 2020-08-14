import discord
import weather
import blackjack

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # print('Message from {0.author}: {0.content}'.format(message))
        msg = message.content
        if '심심' in msg:
            await message.channel.send("$Game_Blackjack")
        if '날씨' in msg:
            # await message.channel.send("$weather 안산")
            weather.Weather()
        if '덥다' in msg:
            await message.channel.send("$weather 안산")
        # if '비 와' in msg:
            #await message.channel.send("$rain")
        # if '우산' in msg:
            #await message.channel.send("$rain")
            
        # if (message.startswith('!hi')):
        #     await message.send("Hello World")


client = MyClient()
client.run('your token')