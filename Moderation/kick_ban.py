import discord
from discord.ext import commands

class kick_ban(commands.Cog, name="Moderation"):
    def __init__(self,bot):
        self.bot = bot

    #Kick

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
        embed.set_footer(text=f"<:DiscordBOT:801303572183777280>[Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)")
        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```Please mention the Name```")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("```Member not found in this server```")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"```{ctx.author.mention}, you don't have the Kick Member permission!```")

    #Ban

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title="Ban News",
            description=f"{member.name} has successfully banned for {reason}",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"<:DiscordBOT:801303572183777280>[Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)")
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```Please mention the Name```")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("```Member not found in this server```")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"```{ctx.author.mention}, you don't have the Ban Member permission!```")

def setup(bot):
    bot.add_cog(kick_ban(bot))
    print("kick_ban file is loaded!")
