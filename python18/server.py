#Server side
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverIP = "localhost"
serverPort = 3456

serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)

print("Waiting for a client is connecting to server")
connectedSocket, address = serverSocket.accept()
print("A client is connected with IP = " + address[0])

#Chat
receiving = False
while True:
	if receiving:
		message = connectedSocket.recv(1024).decode()
		message = "Client > " + message
		print(message)
		receiving = False
	else:
		message = input("Input message : ")
		connectedSocket.send(message.encode())
		receiving = True
