import discord
from discord.ext import commands

bot = commands.Bot('h')

@bot.event
async def on_ready():
	print('bot online')
