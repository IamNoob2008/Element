import discord
from discord.ext import commands

class Avatar(commands.Cog, name="Fun"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def av(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.message.author
        embed = discord.Embed()
        embed.add_field(name=user.name,value=f"[Download]({user.avatar_url})")
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))
    print("Avatar file is loaded!")
