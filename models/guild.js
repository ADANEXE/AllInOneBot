const mongoose = require('mongoose');

const guildSchema = new mongoose.Schema({
  guildId: String,
  prefix: { type: String, default: '/' },
  welcomeChannel: String,
  welcomeMessage: String,
  leaveChannel: String,
  leaveMessage: String,
  tempVCCategory: String,
  premium: { type: Boolean, default: false },
  premiumExpires: Date,
});

module.exports = mongoose.model('Guild', guildSchema);
