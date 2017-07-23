import socket

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
# this would be an ip address, for example, but
# here we're going to connect to the same machine
host = socket.gethostname()

port = 9999

# connect to the server
s.connect((host, port))

# Receive 1024 bytes
response = s.recv(1024)

s.close()

print("The time got from the server is %s" % response.decode('ascii'))
