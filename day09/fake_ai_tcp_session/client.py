import socket

SERVER_ADDRESS = ('127.0.0.1', 54322)
BUFFER_SIZE = 1204

s = socket.socket()

s.connect(SERVER_ADDRESS)

while True:
    try:
        message = input("message:")
        s.send(message.encode())
        data = s.recv(BUFFER_SIZE)
        if len(data) == 0:
            print("server closed")
        else:
            print("response: {}".format(data.decode()))

    except OSError:
        print("server crashed/closed")



