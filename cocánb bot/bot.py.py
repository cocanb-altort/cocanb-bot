import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = "ODAxOTgzMzI3MDIzMzk4OTEy.YAonLQ.nWD30TqqQkHvvGv8n_lI2o0rZuo"

# 2
bot = commands.Bot(command_prefix='u!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)
