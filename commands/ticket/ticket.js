const { SlashCommandBuilder, PermissionFlagsBits, ActionRowBuilder, ButtonBuilder, ButtonStyle } = require('discord.js');
const Ticket = require('../../models/ticket');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('ticket')
    .setDescription('Setup ticket system in a channel')
    .addChannelOption(option => option.setName('channel').setDescription('Channel to deploy ticket button').setRequired(true))
    .setDefaultMemberPermissions(PermissionFlagsBits.Administrator),
  async execute(interaction) {
    const channel = interaction.options.getChannel('channel');

    const row = new ActionRowBuilder().addComponents(
      new ButtonBuilder().setCustomId('create_ticket').setLabel('🎫 Create Ticket').setStyle(ButtonStyle.Primary)
    );

    await channel.send({ content: 'Click the button below to create a support ticket!', components: [row] });
    interaction.reply({ content: `✅ Ticket system deployed in ${channel}`, ephemeral: true });
  }
};
