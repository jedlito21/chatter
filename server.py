import socket
import threading

def zpracovat_zpravu(clientsocket, addr):
    while True:
        try:
            data = clientsocket.recv(1024)
            if not data:
                break
            print(f"Zpráva od klienta {addr}: {data.decode('utf-8')}")

            # Poslat zprávu všem připojeným klientům
            for client in klienti:
                client.sendall(data)
        except ConnectionResetError:
            break

    clientsocket.close()
    print(f"Klient {addr} odpojen.")

# Vytvoření serverového socketu
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8008

serversocket.bind((host, port))
print(serversocket.getsockname())

# Seznam pro uchování připojených klientů
klienti = []

while True:
    serversocket.listen()

    clientsocket, addr = serversocket.accept()
    print(f"Nový klient připojen: {addr}")

    # Přidat klienta do seznamu
    klienti.append(clientsocket)

    # Vytvořit samostatné vlákno pro zpracování zpráv od klienta
    thread = threading.Thread(target=zpracovat_zpravu, args=(clientsocket, addr))
    thread.start()
