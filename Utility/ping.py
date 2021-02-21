import discord
import asyncio
from discord.ext import commands

class ping(commands.Cog, name="Utility"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ping(self, ctx):
		msg = await ctx.send("Pinging <a:WindowsDotLoading:809471466311516211>")
		await ctx.send(msg)
		await asyncio.sleep(5)
		embed = discord.Embed(title="Pong!",description=f"Your latency is {round(self.bot.latency * 1000)}ms",color=0x00FF00)
		embed.add_field(name="ㅤ",value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)")
		await msg.edit(content = "",embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))
    print("ping file is loaded!")
