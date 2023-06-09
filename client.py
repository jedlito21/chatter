import socket
import threading
import tkinter as tk

host = socket.gethostname()

# z entry fieldu pošlu zprávu na server
def poslat_zpravu():
    message = entry_field.get()
    client_socket.sendall(message.encode('utf-8'))
    entry_field.delete(0, tk.END)


# přijímám zprávu ze serveru
def prijmout_zpravu():
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            break
        text_field.insert(tk.END, msg.decode('utf-8') + '\n')

# připojení k serveru
server_address = host
port = 8008
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, port))

# okno tkinter
root = tk.Tk()
root.title("Chattovací aplikace")

# tkinter
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

text_field = tk.Text(root, height=30, width=80, background="light grey", borderwidth=1, relief="solid", foreground="black")
text_field.grid(row=0, column=0, sticky="nsew")

entry_field = tk.Entry(root, width=60, background="white", foreground="black")
entry_field.grid(row=1, column=0, sticky="we")

send_button = tk.Button(root, text="Send", command=poslat_zpravu)
send_button.grid(row=1, column=1, sticky="we")

# spuštění příjmu zpráv ve vlákně
receive_thread = threading.Thread(target=prijmout_zpravu)
receive_thread.start()

root.mainloop()

# ukončení spojení
client_socket.close()
