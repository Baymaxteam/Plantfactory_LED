# Plantfactory_LED

## Environment Setup
nodejs - 

mongoDB - sudo apt-get install mongodb-server

mjpg-stream - 
sudo apt-get install cmake libjpeg8-dev
cd mjpg-streamer-experimental
make
sudo make install


## node-server.service
sudo systemctl start node-server.service
sudo systemctl stop node-server.service
default : http://192.168.0.103:8787
http/streamin port: 8787/8788
SSH port: 21

file path
cd /etc/systemd/system/node-server.service

## how to test 
cd /home/ubuntu/Documents/ShrimpHunter/shrimp-app
nodemon 

## check commend in system
nano /etc/systemd/system/node-server.service


## mjpg-stream
#### ref: https://github.com/jacksonliam/mjpg-streamer

`
git clone https://github.com/jacksonliam/mjpg-streamer
`

### Building & Installation
`
sudo apt-get install cmake libjpeg8-dev
`

`
cd mjpg-streamer-experimental
make
sudo make install
`

### Start Http Server
`
mjpg_streamer -i "input_uvc.so -d /dev/video0 -f 15 -r 640x480" -o "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www/"
`

`
http://192.168.0.103:8080/?action=stream
`


## HW
Logitech C310 HD - usb type 
http://24h.pchome.com.tw/prod/DCAS00-A82845621?q=/S/DCAS4K


## Ref
http://yannickloriot.com/2016/04/install-mongodb-and-node-js-on-a-raspberry-pi/

https://github.com/jperkin/node-rpio


NodeJS PWM
https://www.npmjs.com/package/pi-blaster.js
https://www.npmjs.com/package/pi-gpio