import discord
from discord.ext import commands

class F(commands.Cog, name="Extras"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def f(self, ctx, member):
        embed = discord.Embed(
            title="F",
            description=f"{ctx.author.mention} has "
        )
        await ctx.send(embed=embed)
            

def setup(bot):
    bot.add_cog(F(bot))
    print("F file is loaded!")
