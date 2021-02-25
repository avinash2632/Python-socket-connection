
import socket               # Import socket module

s = socket.socket()         # Create a socket object
port = 1235                # Reserve a port for your service.

s.connect(('', port))
print(s.recv(1024))
s.close()                     # Close the socket when done
