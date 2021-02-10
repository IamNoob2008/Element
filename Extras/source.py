import discord
from discord.ext import commands

class ascii(commands.Cog, name="Utility"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def source(self, ctx):
        embed = discord.Embed(
            title=""
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ascii(bot))
    print("ascii file is loaded!")