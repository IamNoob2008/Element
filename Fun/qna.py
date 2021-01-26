import discord
import random
from discord.ext import commands


class qna(commands.Cog, name="Fun"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qna(self, ctx, *, question):
        response = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.",
            "Better not tell you now.", "Cannot predict now.",
            "Concentrate and ask again.", "Don't count on it.",
            "My reply is no.", "My sources say no.", "Outlook not so good.",
            "Very doubtful."
        ]
        embed = discord.Embed(
            title="Q&A",
            description=
            f"Question: {question}\nAnswer: {random.choice(response)}")
        embed.add_field(
            name="ㅤ",
            value=
            f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)"
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(qna(bot))
    print("qna file is loaded!")
