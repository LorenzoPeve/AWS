from socket import *

SERVER_IP = '3.144.236.101' # Your EC2 instance public IP address
SERVER_PORT = 12000 # The port where server is listening

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_IP, SERVER_PORT))


message = input("Input lowercase sentence: ")
clientSocket.send(message.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
