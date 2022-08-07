from zipapp import create_archive
import discord
import pyfiglet
import re
from API_KEY import Keys
from myDicordPolish import Polish

# class for keeping all the keys
keys = Keys()
discord_key = keys.discordKey()
client = discord.Client()

# dict to keep all the message channels
channels = dict()

@client.event
async def on_ready():
    ready = pyfiglet.figlet_format('Ready!')
    print(ready)

bot_aux = Polish()

@client.event
async def on_message(message):

    log = bot_aux.channelCommands(message) 
    if log == True:
        await message.channel.send('Added new channel')
        return

    elif log == False:
        if bot_aux.validCommand(message) == False:
            return

    
    channels = bot_aux.getValidChannels()
    currentChannel = bot_aux.getChannelName(message)

    for approvedChannel in channels:
        if approvedChannel == currentChannel:
            msg = bot_aux.retrieveExpression(message)
            font_msg = pyfiglet.figlet_format(msg)

            if len(msg) < 10:
                embed = discord.Embed(title = 'New word', description = '```' + font_msg + '```')
                await message.channel.send(embed = embed)
            else:
                await message.channel.send('```' + font_msg + '```')
            
            

client.run(discord_key)