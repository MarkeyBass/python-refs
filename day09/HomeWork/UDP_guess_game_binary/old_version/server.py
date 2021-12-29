import socket
import random

SIZE = 4
ORDER = 'little'


def server_guess():
    SERVER_ADDRESS = ('127.0.0.1', 54322)
    BUFFER_SIZE = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_connection:
        socket_connection.bind(SERVER_ADDRESS)
        print("server {} is listening on port {}".format(*socket_connection.getsockname()))

        while True:
            rand_int = random.randint(1, 100)
            rand_int = rand_int.to_bytes(SIZE, ORDER)
            complete = False

            while not complete:
                try:
                    data, address = socket_connection.recvfrom(BUFFER_SIZE)
                    if data.decode() == 'hello':
                        socket_connection.sendto(rand_int, address)
                        while True:
                            data, address = socket_connection.recvfrom(BUFFER_SIZE)
                            if data.decode() == 'win':
                                complete = True
                                break
                    else:
                        complete = True
                except OSError:
                    print('OSError something went wrong cutting communication with cli')
                    complete = True


if __name__ == "__main__":
    server_guess()
