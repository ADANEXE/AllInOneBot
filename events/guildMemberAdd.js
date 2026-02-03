const Guild = require('../models/guild');

module.exports = {
  name: 'guildMemberAdd',
  async execute(client, member) {
    const guildData = await Guild.findOne({ guildId: member.guild.id });
    if (!guildData || !guildData.welcomeChannel) return;
    const channel = member.guild.channels.cache.get(guildData.welcomeChannel);
    if (!channel) return;

    channel.send(guildData.welcomeMessage.replace('{user}', `<@${member.id}>`));
  },
};
