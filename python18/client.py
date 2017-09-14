#Client side
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
serverIP = "localhost"
serverPort = 3456

print("Connecting to server . . .")
clientSocket.connect((serverIP, serverPort))

print("Connected to server with IP " + serverIP)

#Chat
receiving = True
while True:
	if receiving:
		message = clientSocket.recv(1024).decode()
		message = "Server > " + message
		print(message)
		receiving = False
	else:
		message = input("Input your message : ")
		clientSocket.send(message.encode())
		receiving = True
