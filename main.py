import discord
import sys
import os
import traceback
import json
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv
from keep_alive import keep_alive

def get_prefix(bot, message):
  if not message.guild:
    return commands.when_mentioned_or("--")(bot, message)

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  if str(message.guild.id) not in prefixes:
    return commands.when_mentioned_or("--")(bot, message)

  prefix = prefixes[str(message.guild.id)]
  return commands.when_mentioned_or(prefix)(bot, message)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.remove_command('help')
status = cycle(["--help", "Discord Server, RSGameTech's Official"])

@bot.event
async def on_ready():
  change_status.start()
  print("Bot is online")

@tasks.loop(seconds=5)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

@bot.command()
@bot.is_owner()
async def reload(ctx):
  async with ctx.typing:
    embed = discord.Embed(
      title = "Reloading all Cogs!"
    )
    for ext in os.listdir("./cogs/"):
      if ext.endswith(".py") and not ext.startswith("_"):
        try:
          bot.unload_extension(f"cogs.{ext[:-3]}")
          bot.load_extension(f"cogs.{ext[:-3]}")
          embed.add_field(name="Reloaded:- '{ext}'!",)
        except Exception as e:
          embed.add_field(name="Failed to reload:- '{ext}'",value=e)
        await asyncio.sleep(0.5)
    await ctx.send(embed=embed)

extensions = ['cogs.moderation',
              'cogs.fun',
							'Server Event.join_leave',
							'Utility.avatar',
							'Utility.help',
							'Utility.prefix',
							'Utility.info',
							'Utility.ping',
              'Utility.ascii',
              'Extras.Chat',
              'Extras.source'
]
if __name__ == '__main__':
  for extension in extensions:
    try:
      bot.load_extension(extension)
    except Exception as e:
      print(f"Error loading {extension}", file=sys.stderr)
      traceback.print_exc()

keep_alive()
bot.run(os.getenv('TOKEN'))
