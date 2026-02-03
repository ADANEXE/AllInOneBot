import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel # Or find a specific ID
        if channel:
            embed = discord.Embed(
                title=f"Welcome to {member.guild.name}!",
                description=f"Hello {member.mention}, we're glad you're here!",
                color=0x00ff00
            )
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text="Powered by Otaku Productions")
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))
  
