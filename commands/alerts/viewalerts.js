const { SlashCommandBuilder } = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('alerts')
    .setDescription('View recent alerts in your server'),
  async execute(interaction) {
    interaction.reply({ content: `📢 Alerts will appear here whenever Otaku | Adan sends one!`, ephemeral: true });
  }
};
