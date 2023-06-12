import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8008

serversocket.bind((host, port))
print(serversocket.getsockname())


while True:
    serversocket.listen()
    clientsocket, addr = serversocket.accept()
    print(clientsocket.getpeername())
    clientsocket.sendall(b'Hello world!')
    mess = clientsocket.recv(1024)
    clientsocket.close()