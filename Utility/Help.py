import discord
from discord.ext import commands

class Help(commands.Cog, name="BOT Info"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help",
            description="Here are all the category",
            color=discord.Color.green()
        )
        embed.add_field(name="Mod", value="--help_mod")
        embed.add_field(name="Info", value="--help_info")
        embed.add_field(name="Fun", value="--help_fun")
        await ctx.send(embed=embed)

    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def help_mod(self, ctx):
        embed = discord.Embed(
            title="Mod Command",
            description='''Note:- [] -> Required, () -> Optional
1) Clear -> --clear [No. of message]
2) Kick  -> --kick [User]
3) Ban   -> --ban [User]
4) Embed -> --embed [Title] [Description]
'''
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def help_info(self, ctx):
        embed = discord.Embed(
            title="Fun Command",
            description='''Note:- [] -> Required, () -> Optional
1) Help -> --help
2) Ping -> --ping
'''
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def help_fun(self, ctx):
        embed = discord.Embed(
            title="Info Command",
            description='''Note:- [] -> Required, () -> Optional
1) Q&A         -> --qna [Question]
2) Avatar Icon -> --avatar (User)
'''
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    print("Help file is loaded!")
