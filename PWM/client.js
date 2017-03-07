var net = require('net');

var client = new net.Socket();
var PWM_Commend = [20,20,20];

client.connect(10000, '127.0.0.1', function() {
	console.log('Connected');
	// client.write('Hello, server! Love, Client.');
  var msg = '#!' + String(PWM_Commend[0]) + ',' + String(PWM_Commend[1]) + ',' + String(PWM_Commend[2]);
	client.write(msg)
  //client.write('#!10,20,30')
	client.destroy();
});

client.on('data', function(data) {
	console.log('Received: ' + data);
	client.destroy(); // kill client after server's response
});

client.on('close', function() {
	console.log('Connection closed');
});