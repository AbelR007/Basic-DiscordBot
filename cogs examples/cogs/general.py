# General Cogs (Example Cog)
import discord
from discord.ext import commands 


# You may change the name here from "General" to "Whatever you like", but change the name back in setup function below 
class General(commands.Cog):
	
	# Creates instance and Its necessary (Don't change anything here)
	def __init__(self,bot):
		self.bot = bot
	
	# Example Command	
	@commands.command()      # Must use @commands.command instead of @bot.command
	async def hi(self,ctx):  # 'self' should be added everytime
		await ctx.send(f"Hi there, {ctx.author.mention}")


# The below command is necessary, otherwise the cog won't run
def setup(bot):
	bot.add_cog(General(bot))

"""========================
CREATED with ❤️ by AbelR007
========================"""
