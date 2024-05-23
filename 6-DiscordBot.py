#Tutorial for bot setup: https://realpython.com/how-to-make-a-discord-bot-python/
#Run in terminal: $ pip install -U discord.py

import discord 
import random
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'{bot.user.name} has connected to Discord!')


# GREETING

@bot.command()
async def hello(ctx):
  name = ctx.message.author.name
  await ctx.send(f'Hi {name}!')


# JOKE

joke = "I told my wife I was going to build us a car out of spaghetti. She said I was crazy and to stop making stupid comments. You should have seen her face when I drove pasta."

@bot.command()
async def vits(ctx):
  await ctx.send(vittighed)


# ENCOURAGEMENTS

encouragements = ['You are beautiful', 'You are great', 'I believe in you!']

@bot.command()
async def encouragement(ctx):
  encouragement = random.choice(encouragements)
  await ctx.send(f'Hi {encouragement}')

@bot.command()
async def add(ctx, *args):
  new = " ".join(args[:])
  encouragements.append(new)
  await ctx.send(encouragements)

@bot.command()
async def delete(ctx, *args):
  old = " ".join(args[:])
  if old in encouragements:
    encouragements.remove(old)
  await ctx.send(encouragements)


  
# TIC-TAC-TOE

board = '''
[1] [2] [3]
[4] [5] [6]
[7] [8] [9]'''

@bot.command()
async def new(ctx):
  global board
  board = '''
[1] [2] [3]
[4] [5] [6]
[7] [8] [9]'''
  await ctx.send(board)

@bot.command()
async def X(ctx, position):
  global board
  board = board.replace(position, 'X')
  await ctx.send(board)

@bot.command()
async def O(ctx, position):
  global board
  board = board.replace(position, 'O')
  await ctx.send(board)


TOKEN = 'YOUR-TOKEN'
bot.run(TOKEN)

