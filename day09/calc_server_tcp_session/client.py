import socket

SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1024

s = socket.socket()

s.connect(SERVER_ADDRESS)

while True:

    text = input("message:").lower()

    if text in ('q', 'quit', 'exit'):
        s.close()  # סוגרים את הקליינט
        break

    data = text.encode()
    s.send(data)
    resp = s.recv(BUFFER_SIZE)
    print(resp.decode())



