import socket

SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1204



while True:
    message = input("message : ")
    s = socket.socket()
    s.connect(SERVER_ADDRESS)
    s.send(message.encode())
    data, addr = s.recv(BUFFER_SIZE)
    print("response: {}".format(data.decode()))
    s.close()


