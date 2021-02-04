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
        ("Bot Version","V0.2 (Beta)",True),
        ("Language Using","Python",True),
        ("Total Server Joined","....",True),
        ("Total User Useing","....",True),
        ("Links",f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot),<:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)",False)]
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
        ("Links",f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot),<:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)",False)]
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
        for activity in member.activities:
                    if isinstance(activity, Game):
                        name = activity.name
                        Type = "Playing"
                        Activity = f"{name}"
                    elif isinstance(activity, Streaming):
                        name2 = activity.name
                        name3 = activity.platform
                        Type = "Streaming"
                        Activity = f"{name2} on {name3}"
                    elif isinstance(activity, Spotify):
                        name4 = activity.title
                        name5 = activity.artists
                        Type = "Listening to Spotify"
                        Activity = f"**Song Name**:{name4}\n**Song Artists:**{name5}"
                    elif isinstance(activity, CustomActivity):
                        name6 = activity.name
                        Type = "Custom Status"
                        Custom = f"{name6}"
                    else:
                        name7 = activity.name
                        Type =  "Playing"
                        Activity = f"{name7}"
        fields = [("Name",str(user.name),True),
        ("ID",user.id,True),
        ("Status",str(user.status).capitalize(),True),
        ("Activity",str(user.custom_status)[-1],True),
        ("Created At",user.created_at.strftime("%d/%m/%Y %H:%M:%S"),True),
        ("Joined At",user.joined_at.strftime("%d/%m/%Y %H:%M:%S"),True),
        ("Activity",f"{Type} {Activity}",True),
        ("Custom Status",Custom,True),
        ("Links",f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot),<:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)",False)]
        for name, value, inline in fields:
            embed.add_field(name=name,value=value,inline=inline)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(info(bot))
    print("info file is loaded!")
