import discord
from discord.ext import commands

class f(commands.Cog, name="Fun"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def f(self, ctx, *, user: discord.Member = None):
        if user is None:
            await ctx.send(f"{ctx.author.mention} has paid the respect")
        else:
            embed = discord.Embed(
                title="F",
                description=f"{ctx.author.mention} has paid the respect for {user.mention}"
            )
            await ctx.send(embed=embed)
            

def setup(bot):
    bot.add_cog(f(bot))
    print("f file is loaded!")
