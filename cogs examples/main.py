# This Code shows the necessary recquirements for a cog to run and helps you do that easily.
# Detailed Explainations too ;)

# Most Basic Step is to Import the modules you need
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ".")

all_extensions = [
    'cogs.general'
]

if __name__=='__main__':
    for extension in all_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')

bot.run("Token")
#        ^^^^^ Bot Token is unique and should be added above to run the code as you want



# Please Consider ⭐️Starring my Project
"""=========================
CREATED with ❤️ by AbelR007
========================="""
