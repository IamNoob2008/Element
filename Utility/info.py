import discord
from discord.ext import commands

class info(commands.Cog, name="Utility"):
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
        embed = discord.Embed(title=f"Server Info",color=ctx.guild.owner.colour)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        fields = [("Owner",ctx.guild.owner,True),
        ("Total Member",ctx.guild.member_count,True),
        ("Region",str(ctx.guild.region).capitalize(),True),
        ("Bot Latency",round(self.bot.latency * 1000)}ms,True),
        ("Created At",ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"),True)
        ("ㅤ",f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)",False)]
        for name, value, inline in fields:
            embed.add_field(name=name,value=value,inline=inline)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

#    @commands.command()
#    async def ui(self, ctx , *,user: discord.Member = None):
#        if user is None:
#            user = ctx.message.author
#        embed = discord.Embed(
#            title="User Information",
#            color=0x134F5C
#        )
#        embed.set_thumbnail(url=ctx.author.avatar_url)
#        embed.add_field(name="Name",value=f"{ctx.author.name}")
#        embed.add_field(name="ID",value=f"{ctx.author.id}")
#        embed.add_field(name="Status",value=f"{ctx.author.status}")
#        #embed.add_field(name="Activity",value=f"{ctx.author.activity}")
#        embed.add_field(name="Created At",value=f"{ctx.author.created_at.strftime("%d/%m/%Y %H:%M:%S")}")
#        embed.add_field(name="ㅤ", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)",inline=False)
#        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(info(bot))
    print("info file is loaded!")
