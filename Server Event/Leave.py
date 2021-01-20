import discord
from discord.ext import commands
from discord.utils import get

class Leave(commands.Cog, name="Events"):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = self.bot.get_channel(799268264994799667)
        embed = discord.Embed(
            title = "Sad News",
            description = f"{member.name} just left the Server. Everyone is sad now"
        )
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Leave(bot))
    print("Leave file is loaded!")
