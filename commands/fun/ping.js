const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('ping')
    .setDescription('Check bot latency!'),
  async execute(interaction) {
    const msg = await interaction.reply({ content: '🏓 Pinging...', fetchReply: true });
    interaction.editReply(`🏓 Pong! Latency is ${msg.createdTimestamp - interaction.createdTimestamp}ms.`);
  }
};
