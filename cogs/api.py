import discord
import requests
import json
from discord.ext import commands


class api(commands.Cog, name="API"):
    def __init__(self, bot):
        self.bot = bot

    #Meme

    @commands.command()
    async def meme(self, ctx):
        r = requests.get("https://memes.blademaker.tv/api/memes")
        res = r.json()
        title = res['title']
        ups = res['ups']
        downs = res['downs']
        sub = res['subreddit']
        author = res['author']
        embed = discord.Embed(
            title=f"{title}\nAuthor: {author}\nSubreddit: {sub}",
            color=0xADD8E6
        )
        embed.set_image(url=res['image'])
        embed.set_footer(text=f"👍: {ups}, 👎: {downs}")
        await ctx.send(embed=embed)

    #Font

    @commands.command()
    async def font(self, ctx, font, *, text):
        f = (f"https://gdcolon.com/tools/gdfont/img/{text}?font={font}")
        embed = discord.Embed()
        embed.set_image(url = f)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Wasted

    @commands.command()
    async def wasted(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.message.author
        w = f"https://some-random-api.ml/canvas/wasted?avatar={user.avatar_url}"
        embed = discord.Embed()
        embed.set_image(url = w)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Say

    @commands.command()
    async def say(self, ctx, *, text):
        s = (f"https://gdcolon.com/tools/gdtextbox/img/{text}?color=blue&name={ctx.author.name}&char=scratch")
        await ctx.send(s)

    #Comment

    @commands.command()
    async def comment(self, ctx, *, text):
        c = (f"https://gdcolon.com/tools/gdcomment/img/{text}?name={ctx.author.name}&likes={ctx.guild.member_count}&%=100&days=2-second&customIcon=https%3A%2F%2Fgdbrowser.com%2Ficon%2Ficon%3Ficon%3D30%26form%3Dcube%26col1%3D4%26col2%3D16")
        await ctx.send(c)

def setup(bot):
    bot.add_cog(api(bot))
    print("API file is loaded!")
