const { SlashCommandBuilder } = require('@discordjs/builders');
const Premium = require('../../models/premium');
const Guild = require('../../models/guild');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('premium')
    .setDescription('Check or assign premium status')
    .addStringOption(option => option.setName('action').setDescription('assign/check').setRequired(true))
    .addStringOption(option => option.setName('guildid').setDescription('Server ID for premium')),
  async execute(interaction) {
    if (interaction.user.id !== process.env.OWNER_ID) return interaction.reply({ content: '❌ Only owner can use this.', ephemeral: true });

    const action = interaction.options.getString('action');
    const guildId = interaction.options.getString('guildid');

    if (action === 'assign') {
      const expires = new Date(); expires.setMonth(expires.getMonth() + 1);
      await Premium.findOneAndUpdate({ guildId }, { expires }, { upsert: true });
      await Guild.findOneAndUpdate({ guildId }, { premium: true, premiumExpires: expires }, { upsert: true });
      interaction.reply({ content: `✅ Premium assigned to ${guildId} until ${expires.toDateString()}` });
    } else if (action === 'check') {
      const premium = await Premium.findOne({ guildId });
      if (!premium) return interaction.reply({ content: '❌ This server is not premium.' });
      interaction.reply({ content: `✅ Premium expires: ${premium.expires.toDateString()}` });
    }
  }
};
