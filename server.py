import socket
import threading
import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s', encoding="UTF-8")

# získání zprávy od klientů
def zpracovat_zpravu(clientsocket, addr):
    while True:
        try:
            data = clientsocket.recv(1024)
            if not data:
                break
            logging.info(f"Zpráva od klienta {addr}: {data.decode('utf-8')}")

            # posílá zprávu všem připojeným klientům
            for klient in klienti:
                klient.sendall(data)

            # logování zprávy do souboru
            with open("log.txt", "a") as logfile:
                logfile.write(f"Zpráva od klienta {addr}: {data.decode('utf-8')}\n")
        except ConnectionResetError:
            break

    clientsocket.close()
    logging.info(f"Klient {addr} odpojen.")

# vytvoření serverového socketu
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8008

serversocket.bind((host, port))
print(serversocket.getsockname())


klienti = []

while True:
    serversocket.listen()

    clientsocket, addr = serversocket.accept()
    logging.info(f"Nový klient připojen: {addr}")

    # přidání klienta do seznamu
    klienti.append(clientsocket)

    thread = threading.Thread(target=zpracovat_zpravu, args=(clientsocket, addr))
    thread.start()
