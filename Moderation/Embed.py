import discord
from discord.ext import commands

class Embed(commands.Cog, name="Moderation"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx, title: str = None, *, description: str = None, message = None):
        embed = discord.Embed(
            title=f"{title}",
            description=f"{description}",
            color=0xFFFF00
        )
        await ctx.send(embed=embed)

    @embed.error
    async def embed_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You don't have permision to do this```")

def setup(bot):
    bot.add_cog(Embed(bot))
    print("Embed file is loaded!")
