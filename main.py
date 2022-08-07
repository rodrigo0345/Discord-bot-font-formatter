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
    if log == 1:
        await message.channel.send('Added new channel')

    elif log == 0:
        await message.channel.send('Invalid command')

    elif log == -1:
        channels = bot_aux.getValidChannels()
        currentChannel = bot_aux.getChannelName(message)

        for approvedChannel in channels:
            if approvedChannel == currentChannel:
                msg = bot_aux.getMessageContent(message)
                font_msg = pyfiglet.figlet_format(msg)
                await message.channel.send('<res>' + font_msg + '</res>')
            

client.run(discord_key)