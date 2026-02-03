const mongoose = require('mongoose');

const premiumSchema = new mongoose.Schema({
  guildId: String,
  expires: Date,
});

module.exports = mongoose.model('Premium', premiumSchema);
