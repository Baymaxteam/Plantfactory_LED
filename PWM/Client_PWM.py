import socket
import sys

# argument
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# PWM_ReceivedCommend = sys.argv
# message = '#!' + str(PWM_ReceivedCommend[1] + str(PWM_ReceivedCommend[2] + str(PWM_ReceivedCommend[3]
# print('get pwm "%s"' % str(PWM_ReceivedCommend[1])

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)


try:    
    print('Argument List:', str(sys.argv))
    PWM_ReceivedCommend = sys.argv
    message = '#!' + str(PWM_ReceivedCommend[1] + str(PWM_ReceivedCommend[2] + str(PWM_ReceivedCommend[3]
    # Send data
    # message = '#!10,20,30'
    print('sending "%s"' % message)
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)

    print(sys.stderr, 'received "%s"' % data) 

finally:
    print( sys.stderr, 'closing socket')
    sock.close()