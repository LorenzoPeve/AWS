import os
import socket
from datetime import datetime

server_ip = "172.31.25.238"
port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen()
print(f"Listening on {server_ip}:{port}")

def handle_request(s: str):
    
    filename = s.split(" ")[1]
    filename = filename.replace('/', '') 

    if filename not in os.listdir():
        with open('404.html', 'r') as file:
            body = file.read()

        return 'HTTP/1.1 404 NotFound\r\nContent-Type: text/html\r\n\r\n' + body

    with open(filename, 'r') as file:
        body = file.read()

    return 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + body


while True:

    conn_socket, cl_addr = server.accept()
    print(f'Accepted connection from {cl_addr} at {datetime.now().strftime("%H:%M:%S")}')

    request = conn_socket.recv(1024).decode()
    print(request)
    response = handle_request(request)
    conn_socket.send(response.encode())
    conn_socket.close()