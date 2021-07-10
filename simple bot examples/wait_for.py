import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

@bot.command()
async def waitting(ctx):
	def check(x):
		return x.author == ctx.message.author
	
	ask_for_input = await bot.wait_for('message',check=check)
	
	content = ask_for_input.content
	await ctx.send(f"Recieved the message, {content}!")


bot.run("Token")
