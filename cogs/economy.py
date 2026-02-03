import discord
from discord.ext import commands
import random

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return
        
        # Check for Premium Multiplier
        is_prem = await self.bot.db.premium.find_one({"_id": message.author.id})
        multiplier = 2 if is_prem else 1
        xp_gain = random.randint(5, 15) * multiplier
        
        await self.bot.db.users.update_one(
            {"_id": message.author.id},
            {"$inc": {"xp": xp_gain, "balance": 10 * multiplier}},
            upsert=True
        )

    @commands.command()
    async def balance(self, ctx):
        data = await self.bot.db.users.find_one({"_id": ctx.author.id})
        bal = data.get("balance", 0) if data else 0
        await ctx.send(f"💰 {ctx.author.name}, you have **{bal}** Otaku Coins.")

async def setup(bot):
    await bot.add_cog(Economy(bot))
  
