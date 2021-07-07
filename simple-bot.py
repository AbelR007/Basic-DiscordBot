import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
	print("Bot is running.")

@client.command()
async def hello(ctx):
	await ctx.send(f"Hi there, {ctx.author.mention}")


client.run("Bot_token_here")

#====================================
# CREATED with :heart: by AbelR007
