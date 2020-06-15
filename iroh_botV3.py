# This version refers to Bot events rather than use client events
# Bot is a subclass while client is a superclass

# Iroh Bot imports 
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands #xtensions library

# Environment variable values are stored separately in the same directory
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

bot = commands.Bot(command_prefix='!')
# Command is a wrapper object for a function that can be called by using text in Discord

# Similar to event but uses Bot
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name = "uncle", help = "provides Uncle Iroh's tidbits of wisdom to the user" )
async def uncle_iroh(ctx): #ctx is short for context
    iroh_quotes = [
        "It is usually best to admit mistakes when they occur, and to seek to restore honor",
        "It is important to draw wisdom from many different places.",
        "It's time for you to look inward and start asking yourself the big question: who are you and what do you want?",
        "Sharing tea with a fascinating stranger is one of life’s true delights.",
        "Hope is something you give yourself. That is the meaning of inner strength.",
        "Sometimes life is like this dark tunnel.",
        "Destiny is a funny thing. You never know how things are going to work out.",
        "While it is always best to believe in oneself, a little help from others can be a great blessing.",
        "Pride is not the opposite of shame, but its source. True humility is the only antidote to shame",
        "Life happens wherever you are, whether you make it or not."
    ]

    response = random.choice(iroh_quotes)
    await ctx.send(response)

@bot.command(name= "roll", help="rolls a dice to give you your fate in DnD. !roll 1 6")
async def roll(ctx, number_of_dice: int, number_of_sides: int): # Using Discord's converter here.
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name = "create-channel")
@commands.has_role('admin') # Checks if user is admin before executing this command
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name = channel_name)
    if not existing_channel:
        print(f"Creating a new channel: {channel_name}")
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the admin role for this command.')

bot.run(TOKEN)
    
    