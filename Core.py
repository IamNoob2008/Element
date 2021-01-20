import discord
import sys
import os
import traceback
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='--')
bot.remove_command('help')
status = cycle(["--help", "Discord Server, RSGameTech's Official", "https://discord.gg/7GQkt7s6Xx"])

@bot.event
async def on_ready():
    change_status.start()
    print("Bot is online")

@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

extensions=['Moderation.Clear',
            'Moderation.kick_ban',
            'Moderation.Embed',
            'Server Event.join_leave',
            'Fun.Q&A',
            'Fun.Avatar',
            'Fun.Meme',
            'BOT Info.Help',
            'BOT Info.Ping',
            'Extras.Chat'
]
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Error loading {extension}", file=sys.stderr)
            traceback.print_exc()

bot.run('NzkwODMyMjYzMjYwMDEyNTcz.X-GV8A.c-BuXXqCoBSsiH9w9cB6SMr4IXA')
