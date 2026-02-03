import discord
from discord.ext import commands
import datetime

class Security(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.action_log = {} # Track actions: {user_id: [timestamp, count]}

    async def check_nuke(self, user, guild):
        # Premium Bypass or Adan Bypass
        if user.id == self.bot.owner_id: return
        
        now = datetime.datetime.now()
        data = self.action_log.get(user.id, [now, 0])
        
        # If last action was within 10 seconds, increase count
        if (now - data[0]).total_seconds() < 10:
            data[1] += 1
        else:
            data = [now, 1]
        
        self.action_log[user.id] = data

        if data[1] > 3: # Threshold: 4 actions in 10 seconds
            await guild.ban(user, reason="Otaku Productions Anti-Nuke: Mass Action Detected")
            return True
        return False

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete):
            if await self.check_nuke(entry.user, channel.guild):
                # Optionally recreate the channel logic here
                pass

async def setup(bot):
    await bot.add_cog(Security(bot))
  
