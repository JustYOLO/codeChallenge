# bot.py
import os, discord
import random as r
from dotenv import load_dotenv

class bot(discord.client):
    def __init__(self) -> None:
        self.__users = []

    def shuffling(self) -> None:
        pass

    async def on_ready(self):
            print(f'We have logged in as {client.user}')
            for guild in client.guilds:
                print(f"connected in {guild}")

        async def on_message(message):
            name = message.author.global_name
            if message.author == client.user:
                return

            if message.content.startswith("!hello"):
                await message.channel.send("Hello!")
                print(message.author.global_name)
            
            if message.content.startswith("!사용법"):
                await message.channel.send("!참가 라고 적으세요!\n10명이 !참가 를! 적으면 랜덤하게 팀을 만들어 줍니다.\n처음부터 시작하고 싶으시면 !리셋")
            if message.content.startswith("!리셋"):
                users.clear()
                await message.channel.send("리셋 되었습니다.")

            # !t is for testing purpose
            '''if message.content.startswith("!t"):
                tmp, name = message.content.split(' ')
                users.append(name)
                if len(users) == 10:
                    await message.channel.send(shuffling(users))
                    users.clear()'''
                    
            if message.content.startswith("!참가"):
                if name not in users:
                    users.append(name)
                    await message.channel.send(f"{name}님이 참가신청 했습니다. ({len(users)}/10)")
                    if len(users) == 10:
                        await message.channel.send(shuffling(users))
                        users.clear()
                else: await message.channel.send(f"{name}님은 이미 참가 신청하셨습니다.")

        __client.run(TOKEN)

b = bot()
b.main()


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)