import discord
from discord.ext import commands

class Help(commands.Cog, name="BOT Info"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help",
            description=f"[Help](https://rsgametech.gitbook.io/element/)"
            color=discord.Color.green()
        )
        embed.set_field(name="Invite Element", value=f"[Invite](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    print("Help file is loaded!")
