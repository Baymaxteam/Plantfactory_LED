import socket
import sys
import time
import RPi.GPIO as GPIO

# PWM GPIO init
PWM_PIN_RED_B1 = 11
PWM_PIN_GREEN_B1 = 13
PWM_PIN_BLUE_B1 = 15
PWM_PIN_RED_B2 = 19
PWM_PIN_GREEN_B2 = 21
PWM_PIN_BLUE_B2 = 23
PWM_FREQ = 500

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWM_PIN_RED_B1, GPIO.OUT)
GPIO.setup(PWM_PIN_GREEN_B1, GPIO.OUT)
GPIO.setup(PWM_PIN_BLUE_B1, GPIO.OUT)
GPIO.setup(PWM_PIN_RED_B2, GPIO.OUT)
GPIO.setup(PWM_PIN_GREEN_B2, GPIO.OUT)
GPIO.setup(PWM_PIN_BLUE_B2, GPIO.OUT)

PWM_Process_RED_B1 = GPIO.PWM(PWM_PIN_RED_B1, PWM_FREQ)  # channel=11 frequency=50Hz
PWM_Process_GREEN_B1 = GPIO.PWM(PWM_PIN_GREEN_B1, PWM_FREQ)  # channel=13 frequency=50Hz
PWM_Process_BLUE_B1 = GPIO.PWM(PWM_PIN_BLUE_B1, PWM_FREQ)  # channel=15 frequency=50Hz
PWM_Process_RED_B1 = GPIO.PWM(PWM_PIN_RED_B2, PWM_FREQ)  # channel=19 frequency=50Hz
PWM_Process_GREEN_B1 = GPIO.PWM(PWM_PIN_GREEN_B2, PWM_FREQ)  # channel=21 frequency=50Hz
PWM_Process_BLUE_B1 = GPIO.PWM(PWM_PIN_BLUE_B2, PWM_FREQ)  # channel=23 frequency=50Hz

# stat PWM with 0 % output
PWM_Process_RED_B1.start(0)
PWM_Process_GREEN_B1.start(0)
PWM_Process_BLUE_B1.start(0)
PWM_Process_RED_B2.start(0)
PWM_Process_GREEN_B2.start(0)
PWM_Process_BLUE_B2.start(0)

PWM_LEDCommend=[0,0,0,0,0,0]

def Set_PWMLED(Value):
	PWM_Process_RED_B1.ChangeDutyCycle(Value[0])
	PWM_Process_GREEN_B1.ChangeDutyCycle(Value[1])
	PWM_Process_BLUE_B1.ChangeDutyCycle(Value[2])
	PWM_Process_RED_B2.ChangeDutyCycle(Value[3])
	PWM_Process_GREEN_B2.ChangeDutyCycle(Value[4])
	PWM_Process_BLUE_B2.ChangeDutyCycle(Value[5])

def Stop_PWMLED():
	PWM_Process_RED_B1.ChangeDutyCycle(0)
	PWM_Process_GREEN_B1.ChangeDutyCycle(0)
	PWM_Process_BLUE_B1.ChangeDutyCycle(0)
	PWM_Process_RED_B2.ChangeDutyCycle(0)
	PWM_Process_GREEN_B2.ChangeDutyCycle(0)
	PWM_Process_BLUE_B2.ChangeDutyCycle(0)

# socket init
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(5)


while True:
	# Wait for a connection
	print(sys.stderr, 'waiting for a connection')
	connection, client_address = sock.accept()
	
	try:
		print(sys.stderr, 'connection from', client_address)
		# Receive the data in small chunks and retransmit it
		bufferdata = ""
		while True:
			data = connection.recv(16).decode("utf-8")
			print(sys.stderr, 'received "%s"' % data)
			# print(data[0:2])
			if data[0:2]=='#!':
				bufferdata = data[2:].split(',')
				# print('buffer:' + bufferdata)
				PWM_LEDCommend = [float(x) for x in bufferdata]
				print('PWM:{}'.format(PWM_LEDCommend))
				Set_PWMLED(PWM_LEDCommend)

			# if data:
			#     print(sys.stderr, 'sending data back to the client')
			#     connection.sendall(data)
			else:
				print(sys.stderr, 'no more data from', client_address)
				break
			
	finally:
		# Clean up the connection
		connection.close()
