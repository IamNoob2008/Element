import discord
from discord.ext import commands


class Chat(commands.Cog, name="Extras"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "??":
            await message.channel.send(f"{message.author.name} didn't understand what you told!")
        elif message.content == "idk":
            await message.channel.send(f"{message.author.name} don't know what you asked!'")
        elif message.content == "hi":
            await message.channel.send(f"Hi {message.author.name}, welcome to the chat!")
        elif message.content == "dead chat":
            await message.channel.send(f"{message.author.name}, if it is dead chat then why are you chatting here!")
        elif message.contains("@RSGameTech#9977"):
            await message.channel.send(f":expressionless:")

def setup(bot):
    bot.add_cog(Chat(bot))
    print("Chat file is loaded!")
