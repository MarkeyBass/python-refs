import socket

SERVER_ADDRESS = ('127.0.0.1', 54322)
BUFFER_SIZE = 1024

with socket.socket() as accept_socket:
    accept_socket.bind(SERVER_ADDRESS)
    accept_socket.listen(16)


    while True:
        print("server is listening at {}:{}".format(*accept_socket.getsockname()))
        c, addr = accept_socket.accept()
        print("accepted connection from {}:{}".format(*addr))

        not_quitting = True
        while not_quitting:
            data = c.recv(BUFFER_SIZE)
            print('{}:{}:"{}"'.format(*addr, data.decode()))

            message = data.decode().lower()

            if message == 'how are you?':
                response = 'Fine, Thank you.'.encode()
            elif message == 'thank you':
                response = 'You are welcome'.encode()
            elif message == 'hello':
                response = 'Welcome!'.encode()
            elif message in ('goodbye', 'quit', 'end', 'q', 'exit', 'bye'):
                response = 'See you later'.encode()
                not_quitting = False

            else:
                response = 'I did not understand that.'.encode()

            print('responding: {}'.format(response.decode()))

            c.send(response)

        c.close()



