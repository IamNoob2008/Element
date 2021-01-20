import discord
from discord.ext import commands
from discord.utils import get

class Join(commands.Cog, name="Events"):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.role, name="Verified")
        channel = self.bot.get_channel(797313459523682314)
        embed = discord.Embed(
            title = "Good News",
            description = f"{member.mention} just joined the Server, Welcome him by chatting(Not in DM)",
            color = discord.Color.blue()
        )
        await member.add_role(role)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = self.bot.get_channel(799268264994799667)
        embed = discord.Embed(
            title = "Sad News",
            description = f"{member.name} just left the Server. Everyone is sad now"
        )
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Join(bot))
    print("Join file is loaded!")
