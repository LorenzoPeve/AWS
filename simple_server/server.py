from socket import *

IP = '172.31.36.202' # Your EC2 instance private IP
PORT = 12000 # Your port of choice

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((IP, PORT))
print(serverSocket)
serverSocket.listen(1)
print('The server is ready to receive')
      
while True:

    connectionSocket, addr = serverSocket.accept()
    print(f'Received connection from {addr}')
    sentence = connectionSocket.recv(1024).decode()       
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
