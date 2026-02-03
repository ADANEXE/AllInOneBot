import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- PURGE COMMAND ---
    @app_commands.command(name="purge", description="Bulk delete messages from the channel.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def purge(self, interaction: discord.Interaction, amount: int):
        if amount < 1 or amount > 100:
            return await interaction.response.send_message("Please provide a number between 1 and 100.", ephemeral=True)
        
        await interaction.response.defer(ephemeral=True)
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.followup.send(f"✅ Successfully deleted {len(deleted)} messages.")

    # --- LOCKDOWN COMMAND ---
    @app_commands.command(name="lockdown", description="Lock the current channel so users cannot speak.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lockdown(self, interaction: discord.Interaction):
        overwrite = interaction.channel.overwrites_for(interaction.guild.default_role)
        if overwrite.send_messages is False:
            return await interaction.response.send_message("This channel is already locked!", ephemeral=True)
            
        overwrite.send_messages = False
        await interaction.channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        await interaction.response.send_message(f"🔒 {interaction.channel.mention} has been locked by Otaku Productions.")

    # --- SLOWMODE COMMAND ---
    @app_commands.command(name="slowmode", description="Set a delay between messages for users.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def slowmode(self, interaction: discord.Interaction, seconds: int):
        await interaction.channel.edit(slowmode_delay=seconds)
        await interaction.response.send_message(f"⏳ Slowmode set to **{seconds}** seconds.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
  
