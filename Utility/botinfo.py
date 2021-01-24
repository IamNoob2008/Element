import discord
from discord.ext import commands

class botinfo(commands.Cog, name="Utility"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title = f"<:ElementLogo:802919295755223060> Element BOT Info",
            description =f"Default prefix is --",
            color=0x134F5C
        )
        embed.set_image(url=ctx.guild.icon_url)
        embed.add_field(name="Total Server Joined", value=f"```{ctx.guild.joined}```")
        embed.add_field(name="Bot Latency", value=f"```{round(self.bot.latency * 1000)}ms```")
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(botinfo(bot))
    print("botinfo file is loaded!")
