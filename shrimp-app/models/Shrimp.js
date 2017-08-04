var mongoose = require('mongoose');
var uniqueValidator = require('mongoose-unique-validator');


var ShrimpSchema = new mongoose.Schema({
  ID: { type:Number, required: true, unique: true},
  NAME: { type:String, required: true},
  Motor1: { type: Number, min: 0, max: 100 , required: true},
  Motor2: { type: Number, min: 0, max: 100 , required: true},
  Motor3: { type: Number, min: 0, max: 100 , required: true},
  Motor4: { type: Number, min: 0, max: 100 , required: true},
  Motor5: { type: Number, min: 0, max: 100 , required: true},
  Motor6: { type: Number, min: 0, max: 100 , required: true},
});

ShrimpSchema.set('toJSON', {
     transform: function (doc, ret, options) {
         delete ret._id;
         delete ret.__v;
     }
}); 


ShrimpSchema.plugin(uniqueValidator);
module.exports = mongoose.model('Shrimp', ShrimpSchema);
