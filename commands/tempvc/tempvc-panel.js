const { SlashCommandBuilder, PermissionFlagsBits, ActionRowBuilder, ButtonBuilder, ButtonStyle } = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('tempvc')
    .setDescription('Setup Temp VC panel')
    .addChannelOption(option => option.setName('channel').setDescription('Channel to send panel').setRequired(true))
    .setDefaultMemberPermissions(PermissionFlagsBits.Administrator),
  async execute(interaction) {
    const channel = interaction.options.getChannel('channel');

    const row = new ActionRowBuilder().addComponents(
      new ButtonBuilder().setCustomId('join_tempvc').setLabel('🎶 Join Temp VC').setStyle(ButtonStyle.Primary)
    );

    await channel.send({ content: 'Click the button to create a temporary VC!', components: [row] });
    interaction.reply({ content: `✅ Temp VC panel sent in ${channel}`, ephemeral: true });
  }
};
