import discord
import sys
import os
import traceback
import json
from discord.ext import commands, tasks
from itertools import cycle

def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("--")(bot, message)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("--")(bot, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot, message)

bot = commands.Bot(command_prefix=get_prefix)
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
            'Fun.qna',
            'Fun.Avatar',
            'Fun.Meme',
            'BOT Info.Help',
            'BOT Info.Ping',
            'Settings.prefix',
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
