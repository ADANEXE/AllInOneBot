import discord
from discord.ext import commands

class Premium(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def givepremium(self, ctx, member: discord.Member):
        if ctx.author.id != self.bot.owner_id:
            return await ctx.send("❌ Only Adan can use this command.")
        
        await self.bot.db.premium.update_one(
            {"_id": member.id}, {"$set": {"is_premium": True}}, upsert=True
        )
        await ctx.send(f"🌟 **{member.name}** is now a Premium member of Otaku Productions!")

    @commands.command()
    async def plans(self, ctx):
        embed = discord.Embed(title="💎 Otaku Productions Plans", color=0x7289da)
        embed.add_field(name="Free Plan", value="• Basic Moderation\n• Standard Economy\n• Public Tickets", inline=True)
        embed.add_field(name="Premium Plan", value="• 2x Economy Boost\n• 24/7 Music\n• Priority Tickets\n• Custom Rank Cards", inline=True)
        embed.set_footer(text="Contact Adan for Manual Activation")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Premium(bot))
  
