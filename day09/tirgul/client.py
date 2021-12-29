import socket
import sys

SERVER_ADDRESS = ('127.0.0.1', 54322)
BUFFER_SIZE = 1204

s = socket.socket()

s.connect(SERVER_ADDRESS)

while True:
    try:
        # data = s.recv(BUFFER_SIZE)
        message = input("Enter uname and password: ")
        s.send(message.encode())
        data = s.recv(BUFFER_SIZE).decode()
        print(data)
        # message = input()
        # s.send(message.encode())
        # data = s.recv(BUFFER_SIZE)
        if data == 'success':
            print("Hello welcome aboard")
            break
    except OSError:
        print("server crashed/closed")


while True:
    try:
        message = input("enter command $")
        s.send(message.encode())
        data = s.recv(BUFFER_SIZE)
        if len(data) == 0:
            print("server closed")
        else:
            print("response: {}".format(data.decode()))

        if message in ('goodbye', 'quit', 'end', 'q', 'exit', 'bye'):
            break
    except OSError:
        print("server crashed/closed")
    except (Exception,):
        print("Wrong command, " + str(sys.exc_info()[0]))
        break


