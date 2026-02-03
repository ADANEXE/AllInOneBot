const Ticket = require('../models/ticket');
const TempVC = require('../models/tempvc');

module.exports = {
  name: 'interactionCreate',
  async execute(client, interaction) {

    // Slash Commands
    if (interaction.isChatInputCommand()) {
      const command = client.commands.get(interaction.commandName);
      if (!command) return;
      try {
        await command.execute(interaction);
      } catch (error) {
        console.error(error);
        await interaction.reply({ content: '❌ Error executing command!', ephemeral: true });
      }

    // Button interactions
    } else if (interaction.isButton()) {

      // Ticket button
      if (interaction.customId === 'create_ticket') {
        const existing = await Ticket.findOne({ guildId: interaction.guild.id, userId: interaction.user.id, status: 'open' });
        if (existing) return interaction.reply({ content: '❌ You already have an open ticket!', ephemeral: true });

        const ticketChannel = await interaction.guild.channels.create({
          name: `ticket-${interaction.user.username}`,
          type: 0,
          permissionOverwrites: [
            { id: interaction.guild.roles.everyone, deny: ['ViewChannel'] },
            { id: interaction.user.id, allow: ['ViewChannel', 'SendMessages'] }
          ]
        });

        const newTicket = new Ticket({
          guildId: interaction.guild.id,
          channelId: ticketChannel.id,
          userId: interaction.user.id
        });

        await newTicket.save();
        interaction.reply({ content: `✅ Ticket created: ${ticketChannel}`, ephemeral: true });
        ticketChannel.send(`Hello ${interaction.user}, a staff member will assist you soon!`);
      }

      // Temp VC button
      if (interaction.customId === 'join_tempvc') {
        interaction.reply({ content: `🎶 Join any temp VC by connecting to the voice channel!`, ephemeral: true });
      }

    }
  },
};
