import discord
from discord.ext import commands

class Custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addcmd(self, ctx, name: str, *, response: str):
        # Check if they have Premium
        is_prem = await self.bot.db.premium.find_one({"_id": ctx.author.id})
        if not is_prem:
            return await ctx.send("❌ Custom commands are an **Otaku Productions Premium** feature!")

        await self.bot.db.custom_cmds.update_one(
            {"guild_id": ctx.guild.id, "name": name.lower()},
            {"$set": {"response": response, "creator": ctx.author.id}},
            upsert=True
        )
        await ctx.send(f"✅ Created custom command: `!{name.lower()}`")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not message.content.startswith("!"): return
        
        cmd_name = message.content[1:].split()[0].lower()
        cmd_data = await self.bot.db.custom_cmds.find_one({"guild_id": message.guild.id, "name": cmd_name})
        
        if cmd_data:
            await message.channel.send(cmd_data["response"])

async def setup(bot):
    await bot.add_cog(Custom(bot))
          
