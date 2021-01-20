import discord
from discord.ext import commands

class Kick(commands.Cog, name="Moderation"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title="Kick News",
            description=f"{member.name} has successfully kicked for {reason}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```Please mention the Name```")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("```Member not found in this server```")

def setup(bot):
    bot.add_cog(Kick(bot))
    print("Kick file is loaded!")
