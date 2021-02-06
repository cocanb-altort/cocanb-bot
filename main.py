import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from unicodedata import *
from replit import db
from keep_alive import keep_alive
from datetime import datetime, timedelta
from time import localtime, strftime

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='*')

@bot.command(name='tochar', help='Converts unicode codepoint to character')
async def unicode(ctx, codepoint):
    response = chr(int(codepoint, 16))
    await ctx.send('```' + response + '```')

@bot.command(name='tocode', help='Converts character to unicode codepoint')
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

@bot.command(name='time', help='Shows current time given a timezone (In HH:MM format)')
async def time (ctx, timezone):
  hours = int(timezone[:-3])+int(timezone[-2:])/60
  future_time = datetime.today() + timedelta(hours=hours)
  if timezone == '00:00':
    plus = '±'
  elif timezone[0] != '-':
    plus = '+'
  else:
    plus = ''
  week_day = future_time.weekday()
  weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
  week_day = weekdays[week_day]
  if timezone[-3] == ':':
    await ctx.send('```' + week_day + ', ' + str(future_time) + ', UTC' + plus + timezone + '```')
  else:
    pass

keep_alive()
bot.run(TOKEN)
