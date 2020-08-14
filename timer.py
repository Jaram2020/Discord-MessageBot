import discord, time
import datetime

from discord.ext import commands

class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start = 0
        self.end = 0
    
    @commands.command()
    async def time(self, message, args): #args 0:00:00 string 형태
        sec = args.split(":")
        for i in range(len(sec)):
            sec[i] = int(sec[i])
        if len(sec) != 3:
            await message.send("시간:분:초 형태로 입력해주세요.")
        else:
            total = 3600 * sec[0] + 60 * sec[1] + sec[2]
            time.sleep(total)
            await message.send("설정하신 시간이 종료되었습니다.")
    
    @commands.command()
    async def time_start(self, msg):
        self.start = time.perf_counter()
        
    @commands.command()
    async def time_stop(self, message):
        if self.start == 0:
            await message.send("time_start 명령을 먼저 실행해주세요.")
        else:
            self.end = time.perf_counter()
            time_result = round(self.end-self.start,3)
            hour = int(time_result // 3600)
            minute = int((time_result % 3600) // 60)
            seconds = int(time_result % 60)
            await message.send("{0}:{1}:{2}".format(hour,minute,seconds))
            self.start = 0
    
    @commands.command()
    async def what_time_is_it_now(self, message):
        now = datetime.datetime.today()
        now = now + datetime.timedelta(hours=9)
        await message.send("현재는 `{0}`년 `{1}`월 `{2}`일 `{3}`시 `{4}`분입니다.".format(now.year, now.month, now.day, now.hour, now.minute))

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"),
                   description='Simple bot example')
        
@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.add_cog(Timer(bot))
bot.run('your token')
