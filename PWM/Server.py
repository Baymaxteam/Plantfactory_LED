import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(5)

PWM_LEDCommend=[0,0,0]

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()

    try:
    	print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        bufferdata = ''
        while True:
            data = connection.recv(16)
            print(sys.stderr, 'received "%s"' % data)
            print(data[0:2])
            if data[0:2]=='#!':
            	bufferdata = data[2:].split(',')
            	print(bufferdata)
            	PWM_LEDCommend = [float(x) for x in bufferdata]
            	print(PWM_LEDCommend)

            if data:
                print(sys.stderr, 'sending data back to the client')
                connection.sendall(data)
            else:
                print(sys.stderr, 'no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()
