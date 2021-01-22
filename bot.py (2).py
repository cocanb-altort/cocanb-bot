import os
import random
from dotenv import load_dotenv
from unicodedata import *
import datetime
import time
from datetime import datetime
from time import localtime, strftime


from discord.ext import commands

load_dotenv()
TOKEN = "ODAxOTgzMzI3MDIzMzk4OTEy.YAonLQ.nWD30TqqQkHvvGv8n_lI2o0rZuo"

# command prefix
bot = commands.Bot(command_prefix='c!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# c!codepoint [hex code]
@bot.command(name='codepoint', help='Converts unicode codepoint to character')
async def unicode(ctx, codepoint):
    response = chr(int(codepoint, 16))
    await ctx.send('```' + response + '```')

# c!character [character]
@bot.command(name='character', help='Converts unicode codepoint to character')
async def unicode(ctx, character):
    response = hex(ord(character))
    response = response[2:]
    if len (response) == 1:
        response = '000' + response
    elif len (response) == 2:
        response = '00' + response
    elif len (response) == 3:
        response = '0' + response
    else:
        pass
    await ctx.send('```U+' + response + '```')

# c!localtime (doesn't work yet)
#@bot.command(name='localtime', help='gives current time in selected timezone')
#async def localtime(ctx):
#    timenow = datetime.now().strftime("%A, %d %B %Y %H:%M:%S.%f, ")
#    timezone = strftime("UTC%z", localtime())
#    response = timenow+timezone[:6]+":"+timezone[6:]
#    await ctx.send(str(response))
    
bot.run(TOKEN)
