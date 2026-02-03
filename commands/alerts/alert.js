const { SlashCommandBuilder, PermissionFlagsBits } = require('discord.js');
const Guild = require('../../models/guild');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('alert')
    .setDescription('Send an alert to all servers')
    .addStringOption(option => option.setName('message').setDescription('Alert message').setRequired(true)),
  async execute(interaction) {
    // Only bot owner can send
    if (interaction.user.id !== process.env.OWNER_ID) 
      return interaction.reply({ content: '❌ Only the bot owner can send alerts.', ephemeral: true });

    const message = interaction.options.getString('message');

    // Fetch all guilds from database
    const guilds = await Guild.find({});

    let sent = 0;
    for (const g of guilds) {
      try {
        const guild = await interaction.client.guilds.fetch(g.guildId);
        const channel = guild.channels.cache.find(ch => ch.type === 0 && ch.permissionsFor(guild.members.me).has(PermissionFlagsBits.SendMessages));
        if (channel) {
          channel.send(`📢 **Alert from Otaku | Adan:**\n${message}`);
          sent++;
        }
      } catch (err) {
        console.log(`Failed to send alert to ${g.guildId}: ${err}`);
      }
    }

    interaction.reply({ content: `✅ Alert sent to ${sent} servers.`, ephemeral: true });
  }
};
