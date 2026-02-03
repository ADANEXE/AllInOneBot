const { SlashCommandBuilder, PermissionFlagsBits } = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('kick')
    .setDescription('Kick a member')
    .addUserOption(option => option.setName('target').setDescription('User to kick').setRequired(true))
    .addStringOption(option => option.setName('reason').setDescription('Reason for kick'))
    .setDefaultMemberPermissions(PermissionFlagsBits.KickMembers),
  async execute(interaction) {
    const user = interaction.options.getUser('target');
    const reason = interaction.options.getString('reason') || 'No reason';

    const member = interaction.guild.members.cache.get(user.id);
    if (!member) return interaction.reply({ content: '❌ Member not found', ephemeral: true });

    await member.kick(reason);
    interaction.reply({ content: `✅ ${user.tag} kicked. Reason: ${reason}` });
  }
};
