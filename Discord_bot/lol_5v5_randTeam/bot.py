# bot.py
import os, discord
import random as r
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

users = []

client = discord.Client(intents=intents)

def shuffling(users):
    lane = ['탑', '정글', '미드', '원딜', '서폿']
    result = ""
    r.shuffle(users)
    for i in range(2):
        for j in range(5):
            result += str(i+1) + "팀 "+ lane[j] + " " + users[j+5*i] + "\n"
        if i == 0:
            result += "-----------------------\n"
    
    return result

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    name = message.author.global_name
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")
        print(message.author.global_name)
    
    if message.content.startswith("!사용법"):
        await message.channel.send("!참가 이름\n이름 부분에 자기 이름을 적어주세요.\n처음부터 시작하고 싶으시면 !리셋")
    if message.content.startswith("!리셋"):
        users.clear()
        await message.channel.send("리셋 되었습니다.")

    if message.content.startswith("!참가"):
        if name not in users:
            users.append(name)
            await message.channel.send(f"{name}님이 참가신청 했습니다. ({len(users)}/10)")
            if len(users) == 10:
                await message.channel.send(shuffling(users))
                users.clear()
        else: await message.channel.send(f"{name}님은 이미 참가 신청하셨습니다.")
    '''if message.content.startswith("!참가"):
        tmp, name = message.content.split(' ')
        users.append(name)
        if len(users) == 10:
            await message.channel.send(shuffling(users))
            users.clear()'''

client.run(TOKEN)