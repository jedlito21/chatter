import socket
from tkinter import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8008

s.connect((host, port))
msg = s.recv(1024)
print(msg.decode('ascii'))
s.close()


def odeslat_data():
    text_send = entry_field.get()
    entry_field.delete(0, END)
    s.send(text_send.encode())
    print(text_send)




#vytvoření okna

root = Tk()
root.title("chatter")
root.geometry('800x1000')

num_rows = 2
num_columns = 6

for i in range(num_rows):
    root.rowconfigure(i, weight=1)
for k in range(num_columns):
    root.columnconfigure(k, weight=1)

name_of_person = Label(root, text="Hello im under da watah", font=('Helvetica', 25))
name_of_person.grid(row=0, column=0, columnspan=6, sticky="nswe")

text_field = Text(root, state="disabled", height=55, width=80, background="light grey", borderwidth=1, relief="solid", foreground="black")
text_field.grid(row=1, column=0, columnspan=6, sticky="nswe")

entry_field = Entry(root, width=80 , background="white", foreground="black")
entry_field.grid(row=2, column=0, columnspan=4)

send_button = Button(root, text="Send", command=odeslat_data)
send_button.grid(row=2, column=4, columnspan=2)


root.mainloop()