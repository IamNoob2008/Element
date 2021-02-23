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

    #Colour

    @commands.command()
    async def colour(self, ctx):
        r = requests.get("http://www.colourlovers.com/api/colors/random")
        res = r.json()
        title = res['title']
        unique_id = res['id']
        hex_code = res['hex']
        red = res['red']
        green = res['green']
        blue = res['blue']
        image = res['imageUrl']
        embed = discord.Embed(
            title=f"About Colours"
        )
        embed.add_field(name=f"{title}", value=f"Unique ID:-{unique_id}")
        embed.add_field(name="Hex Code", value=f"{hex_code}")
        embed.add_field(name="RGB Breakdown", value=f"{hex_code}\nRGB Breckdown:-\nRed:- {red}\nGreen:- {green}\nBlue:- {blue}")
        embed.set_image(url=image)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)

    #Wasted

    @commands.command()
    async def wasted(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.message.author
        r = f"https://some-random-api.ml/canvas/wasted?avatar={user.avatar_url({ format: 'png'})}"
        res = r.json()
        embed = discord.Embed()
        embed.add_field(name=user.name,value=f"[Download]({r})")
        embed.set_image(url=r)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(api(bot))
    print("API file is loaded!")
