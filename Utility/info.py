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
        fields = [("Bot Latency",f"{round(self.bot.latency* 1000)}ms",True),
        ("Created By","RSGameTech#9977",True),
        ("Bot Version","V0.2(Beta)",True),
        ("Language Using","Python",True),
        ("Total Server Joined","....",True),
        ("Total User Useing","....",True),
        ("Links",f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot),<:supporter:775594205186883585>: [Support Server](discord.gg/PKP4mG6E3G)",False)]
        for name, value, inline in fields:
            embed.add_field(name=name,value=value,inline=inline)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def si(self, ctx):
        embed = discord.Embed(title=f"Server Info",color=ctx.guild.owner.colour)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        fields = [("Owner",ctx.guild.owner,True),
        ("Total Member",ctx.guild.member_count,True),
        ("Region",str(ctx.guild.region).capitalize(),True),
        ("Created At",ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"),True),
        ("Links",f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot),<:supporter:775594205186883585>: [Support Server](discord.gg/PKP4mG6E3G)",False)]
        for name, value, inline in fields:
            embed.add_field(name=name,value=value,inline=inline)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def ui(self, ctx , *,user: discord.Member = None):
        if user is None:
            user = ctx.author
        embed = discord.Embed(
            title="User Information",
            color=0x134F5C
        )
        embed.set_thumbnail(url=user.avatar_url)
        fields = [("Name",str(user.name),True),
        ("ID",user.id,True),
        ("Status",str(user.status).capitalize(),True),
        ("Activity",str(user.activity).split(".")[-1],True),
        ("Created At",user.created_at.strftime("%d/%m/%Y %H:%M:%S"),True),
        ("Joined At",user.joined_at.strftime("%d/%m/%Y %H:%M:%S"),True),
        ("Links",f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot),<:supporter:775594205186883585>: [Support Server](discord.gg/PKP4mG6E3G)",False)]
        for name, value, inline in fields:
            embed.add_field(name=name,value=value,inline=inline)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(info(bot))
    print("info file is loaded!")
