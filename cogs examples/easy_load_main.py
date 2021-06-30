# Sample Cogs Code for Simplification | Part-3
# Detailed Explainations ;)

# Most Basic Step is to Import the modules you need
import discord
import os # As you use it below
from discord.ext import commands

bot = commands.Bot(command_prefix = ".")

# Easier to load cogs as you don't have to mention it everytime.
if __name__ == '__main__':
    for filename in os.listdir('./cogs'): # Change './cogs' to your cogs folder name
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')

bot.run("Token")
#        ^^^^^ Bot Token is unique and should be added above to run the code as you want

# Please Consider ⭐️Starring my Project
"""=========================
CREATED with ❤️ by AbelR007
========================="""
