import discord
from discord.ext import commands

class TicketView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.green, custom_id="create_ticket")
    async def create(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await guild.create_text_channel(f'ticket-{interaction.user.name}', overwrites=overwrites)
        await interaction.response.send_message(f"Ticket created: {channel.mention}", ephemeral=True)
        await channel.send(f"Welcome {interaction.user.mention}, staff will be with you shortly.")

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_tickets(self, ctx):
        embed = discord.Embed(title="Support Center", description="Click the button below to open a ticket.")
        await ctx.send(embed=embed, view=TicketView(self.bot))

async def setup(bot):
    await bot.add_cog(Tickets(bot))
  
