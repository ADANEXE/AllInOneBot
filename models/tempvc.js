const mongoose = require('mongoose');

const tempVCSchema = new mongoose.Schema({
  guildId: String,
  userId: String,
  channelId: String,
});

module.exports = mongoose.model('TempVC', tempVCSchema);
