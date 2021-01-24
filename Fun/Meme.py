import discord
import requests
from discord.ext import commands

class Meme(commands.Cog, name="Fun"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        r = requests.get('https://memes.blademaker.tv/api/memes')
        res = r.json()
        title = res['title']
        ups = res['ups']
        downs = res['downs']
        sub = res['subreddit']
        author = res['author']
        embed = discord.Embed(
            title = f"{title}\nAuthor: {author}\nSubreddit: {sub}",
            color=0xADD8E6
        )
        embed.set_image(url = res['image'])
        embed.set_footer(text=f"👍: {ups}, 👎: {downs}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Meme(bot))
    print("Meme file is loaded!")
