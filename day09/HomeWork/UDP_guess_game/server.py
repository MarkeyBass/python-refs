import socket
import random


SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1024

socket_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


socket_connection.bind(SERVER_ADDRESS)
print("server {} is listening on port {}".format(*socket_connection.getsockname()))

while True:
    rand_int = random.randint(1, 100)
    complete = False
    while not complete:
        try:
            msg = ''
            data, address = socket_connection.recvfrom(BUFFER_SIZE)
            users_guess = int(data.decode())
            print('user {} started made a guess'.format(address))
            if users_guess == rand_int:
                complete = True
                msg = "Congrats Your guess is right!!! Let's play again.."
            elif users_guess > rand_int:
                msg = "Too Big"
            else:
                msg = "Too small"
            socket_connection.sendto(msg.encode(), address)
        except OSError:
            print('OSError something went wrong cutting communication with cli')
            socket_connection.close()
            break
