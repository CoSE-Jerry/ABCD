import socket

HOST = '192.168.0.138' # Enter IP or Hostname of your server
PORT = 5560 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
	command = input('Enter your command: ')
	s.send(str.encode(command))
	reply = s.recv(1024)
	print (reply.decode('utf-8'))
s.close()
s2.close()
