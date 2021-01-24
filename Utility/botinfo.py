import discord
from discord.ext import commands

class botinfo(commands.Cog, name="Utility"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title = f"",
            color=0x134F5C
        )
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(botinfo(bot))
    print("botinfo file is loaded!")
