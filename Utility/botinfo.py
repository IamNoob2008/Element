import discord
from discord.ext import commands

class botinfo(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bi(self, ctx):
        embed = discord.Embed(
            title=f"<:ElementLogo:802919295755223060> Element BOT Info",
            description=f"Default prefix is --",
            color=0x134F5C
        )
        embed.set_image(url=ctx.guild.icon_url)
        #embed.add_field(name="Total Server Joined", value=f"```{ctx.guild.joined}```")
        embed.add_field(name="Bot Latency",value=f"```{round(self.bot.latency * 1000)}ms```",inline=True)
        embed.add_field(name="ㅤ",value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)",inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def si(self, ctx):
        embed = discord.Embed(title=f"Server Info",color=0x134F5C)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Owner",value=f"{ctx.guild.owner}",inline=True)
        embed.add_field(name="Total Member",value=f"{ctx.guild.member_count}",inline=True)
        embed.add_field(name="Region", value=f"{ctx.guild.region.capitalise}",inline=True)
        embed.add_field(name="BOT Latency",value=f"{round(self.bot.latency * 1000)}ms",inline=False)
        embed.add_field(name="ㅤ",value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)",inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def ui(self, ctx ,user: discord.Member = None):
        if user is None:
            sui= discord.Embed(
                title="User Information",
                color=0x134F5C
            )
            sui.set_thumbnail(url=ctx.author.avatar_url)
            sui.add_field(name="Name",value=f"{ctx.author.name}")
            sui.add_field(name="ID",value=f"{ctx.author.id}")
            sui.add_field(name="Status",value=f"{ctx.author.status}")
            sui.add_field(name="Created At",value=f"{ctx.author.created}")
            sui.add_field(name="ㅤ", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)",inline=False)


def setup(bot):
    bot.add_cog(botinfo(bot))
    print("botinfo file is loaded!")
