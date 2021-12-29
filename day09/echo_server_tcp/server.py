import socket

SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1204

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
accept_socket = socket.socket()

accept_socket.bind(SERVER_ADDRESS)
accept_socket.listen(16)

print("server is listening at {}:{}".format(*accept_socket.getsockname()))

try:
    while True:
        client_socket, client_address = accept_socket.accept()
        print("accepted connection with {}:{}".format(*client_address))

        data = client_socket.recv(BUFFER_SIZE)

        print('request: {}'.format(data.decode()))
        client_socket.send(data)

        client_socket.close()
        print()
finally:
    accept_socket.close()




