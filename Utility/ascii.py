import discord
import pyfiglet
from discord.ext import commands

class Avatar(commands.Cog, name="Utility"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def user_av(self, ctx, *, text):
        a = pyfiglet.figlet_format(text)
        await ctx.send(a)

def setup(bot):
    bot.add_cog(Avatar(bot))
    print("Avatar file is loaded!")
