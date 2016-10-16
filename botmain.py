#! python2
import discord
import os
import asyncio
client = discord.Client()
prefix = "*"

import requests.packages.urllib3 
requests.packages.urllib3.disable_warnings()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def info(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, 'Calculating messages...')
	
token = "retracted"
client.run(token)