#written by ,\#0001

import discord
import discord.utils
import discord.role
import time
import asyncio
global wordlist

## CONFIG
token = "" #Bot token
server_id = "" #Server(Guild) id
wordlist = ("word1", "word2", "word3") #Words to blacklist (CHANGE THIS)
mute_time = 15 #Minutes

seconds = mute_time * 60
word = ""
client = discord.Client()
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == server_id:
            break
    print('[*]' + ' Connected to Discord!')        
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="myko"))

@client.event
async def on_message(message):
    
    if message.content == "W":
        if message.author.bot:
            return
        await message.channel.send("W")

    for word in wordlist:
        if word in message.content:
            await message.delete()
            await message.channel.send("> **No slurs please " + str(message.author) + ", muted for " + str(mute_time) + " minutes.**")
            member = message.author
            role = discord.utils.get(message.guild.roles, name = "Muted")
            await member.add_roles(role)
            print("[*] " + str(message.author) + " has been muted for saying " + str(message.content))
            if time:
                await asyncio.sleep(seconds)
                await member.remove_roles(role)

client.run(token)