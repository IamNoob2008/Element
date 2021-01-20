import discord
from discord.ext import commands

class Clear(commands.Cog, name="Moderation"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```Please specify the amount of the message to delete.```")

def setup(bot):
    bot.add_cog(Clear(bot))
    print("Clear file is loaded!")
