import discord
from discord.ext import commands
import time

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command(name="invite")
    async def invite(self, ctx):
        """Get the link to invite Otaku Productions to your server."""
        # Replace 'YOUR_CLIENT_ID' with the ID from your Discord Developer Portal
        invite_url = f"https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands"
        
        embed = discord.Embed(
            title="📩 Invite Otaku Productions",
            description=f"Click [HERE]({invite_url}) to invite the bot to your server!",
            color=0x7289da
        )
        embed.set_footer(text="Managed by Adan | Otaku Productions")
        await ctx.send(embed=embed)

    @commands.command(name="about")
    async def about(self, ctx):
        """Information about the bot and the creator."""
        uptime = str(round((time.time() - self.start_time) / 3600, 2))
        embed = discord.Embed(title="🤖 About Otaku Productions", color=0x9b59b6)
        embed.add_field(name="Creator", value="Adan (Otaku Productions)", inline=True)
        embed.add_field(name="Library", value="Discord.py", inline=True)
        embed.add_field(name="Uptime", value=f"{uptime} Hours", inline=True)
        embed.add_field(name="Support Server", value="[Join Here](YOUR_SUPPORT_SERVER_LINK)", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name="plan")
    async def plan(self, ctx):
        """Comparison between Free and Premium plans."""
        embed = discord.Embed(
            title="💎 Otaku Productions Membership Plans",
            description="Compare our features and find the best fit for your server.",
            color=0xf1c40f
        )
        
        # Creating a comparison table in the embed
        comparison = (
            "**Feature** | **Free** | **Premium**\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "Music Qual. | Standard | **High (24/7)**\n"
            "Economy | 1x XP | **2x Multiplier**\n"
            "Tickets | Public | **Private/Priority**\n"
            "Moderation | Basic | **Anti-Nuke/Backup**\n"
            "Customization | None | **Custom Rank Cards**"
        )
        
        embed.add_field(name="Detailed Comparison", value=comparison, inline=False)
        embed.add_field(name="How to get Premium?", value="Contact **Adan** directly in the support server for manual activation.", inline=False)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
  
