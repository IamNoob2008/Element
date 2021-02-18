import discord
from discord.ext import commands

class owner(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()

def setup(bot):
    bot.add_cog(owner(bot))
    print("owner file is loaded!")
