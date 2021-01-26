import discord
from discord.ext import commands

class Clear(commands.Cog, name="Moderation"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount: int):
		embed = discord.Embed(
			title="Clear News",
			description="Message has been succesfully clear",
			color=0xE67E22
		)
		embed.add_field(name="ㅤ", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)")
		await ctx.channel.purge(limit=amount + 1)
		await ctx.send(embed=embed)

	@clear.error
	async def clear_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			EN = discord.Embed(
				description=f"{ctx.author.mention}, you have to  specify the amount of message to delete."
			)
			EN.add_field(name="ㅤ", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)")
			await ctx.send(embed=EN)
		elif isinstance(error, commands.MissingPermissions):
			EP = discord.Embed(
				description=f"{ctx.author.mention}, you don't have the 'Manage Message' permision to use this command."
			)
			EP.add_field(name="ㅤ", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)")
			await ctx.send(embed=EP)

def setup(bot):
	bot.add_cog(Clear(bot))
	print("Clear file is loaded!")
