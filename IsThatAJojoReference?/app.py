import discord
from discord.ext import tasks
import json

class Enviroment:

    def __init__(self):

        configFile = open("config.json", "r")
        self.configData = json.loads(configFile.read())
        configFile.close()

        self.targets = []

client = discord.Client()
env = Enviroment()

@client.event
async def on_ready():
    
    pass

@client.event
async def on_message(message):

    print(f'{message.author.name} : {message.content}')

    if message.author.bot:
        return
    
    if not message.author in env.targets:
        env.targets.append(message.author)
        print("author added")

    await message.channel.send("Is that a jojo reference?")
    await dm(message.author, 5)

async def dm(author, amount):

    for i in range(amount):
        await author.send("Are you a jojo reference?")
        
client.run(env.configData['token'])