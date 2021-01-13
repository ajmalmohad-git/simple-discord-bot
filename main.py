import discord
import os
import requests
import json
import wikipedia
from keep_alive import keep_alive

client = discord.Client()


def getactivity():
    response = requests.get("https://www.boredapi.com/api/activity")
    data = json.loads(response.content)
    activity = data["activity"]
    typeof = data["type"]
    conclude = f"Random Activity : {activity} \nActivity Type : {typeof}"
    return (conclude)


def getjoke():
    response = requests.get(
        "https://official-joke-api.appspot.com/random_joke")
    data = json.loads(response.text)
    setup = data["setup"]
    punchline = data["punchline"]
    conclude = f"{setup} \n{punchline}"
    return (conclude)

def getquote():
    response = requests.get(
        "https://api.quotable.io/random")
    data = json.loads(response.text)
    author = data['author']
    content = data['content']
    conclude = f"{content}\n-{author}"
    return (conclude)

def getmeme():
    response = requests.get(
        "https://meme-api.herokuapp.com/gimme")
    data = json.loads(response.text)
    meme = data["preview"][3]
    return (meme)

@client.event
async def on_ready():
    print('We are logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg.startswith('!hello'):
        await message.channel.send(f'Hello! <@{message.author.id}>')

    if msg.startswith('!help'):
        info = discord.Embed(
            title="Bot by Ajmal Moha'd",
            description=
            "\n**Commands:**\n\n***!hello*** - Say hello to bot\n\n***!help*** - Get help about the commands\n\n***!info*** - Get info about the bot\n\n***!bored*** - Gives you a random activityt\n\n***!meme*** - Gives you a Random Meme\n\n***!quote*** - Gives you a Famous Quote\n\n***!joke*** - Wanna hear a joke?\n\n***!wiki*** *<searchterm>* - Do a quick wiki search\n*Eg:* ***!wiki*** *python*\n\n\n**Thanks for using**"
        )
        await message.channel.send(content=None, embed=info)

    if msg.startswith('!bored'):
        activity = getactivity()
        await message.channel.send(f"Hey,  <@{message.author.id}>\n{activity}")

    if msg.startswith('!joke'):
        joke = getjoke()
        await message.channel.send(f"Hey,  <@{message.author.id}>\n{joke}")
    
    if msg.startswith('!quote'):
        quote = getquote()
        await message.channel.send(f"Hey,  <@{message.author.id}>\n{quote}")

    if msg.startswith('!info'):
        info = discord.Embed(
          title="Bot by Ajmal Moha'd",
          description="This bot is made with Python\nFun and a handy bot\n\n\n***Creator: Ajmal Moha'd***\n***Contact: ajmalajmal.2017@gmail.com***\n***Instagram: @ajmal_mohad***\n***Twitter: @ajmal_mohad1***"
        )
        await message.channel.send(content=None,embed=info)

    if msg.startswith('!wiki'):
        term = msg.split("!wiki",1)[1]
        result = wikipedia.summary(f"{term}", sentences = 5)
        info = discord.Embed(title=f"Search Result for {term} Requested by {message.author.name}",description=result)
        await message.channel.send(content=f"Hey,  <@{message.author.id}>\n",embed=info)

    if msg.startswith('!meme'):
        memelink = getmeme()
        meme = discord.Embed(title=f"Random Meme Requested by {message.author.name}",description=memelink) 
        await message.channel.send(content=None,embed=meme)


keep_alive()
client.run(os.getenv('TOKEN'))
