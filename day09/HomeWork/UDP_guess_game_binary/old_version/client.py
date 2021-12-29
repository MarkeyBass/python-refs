import socket

SIZE = 4
ORDER = 'little'

SERVER_ADDRESS = ('127.0.0.1', 54322)
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_connection:
    do_play = True

    while do_play:
        try:
            socket_connection.sendto('hello'.encode(), SERVER_ADDRESS)
            data, address = socket_connection.recvfrom(1024)
            data = int.from_bytes(data, ORDER)
            print(data, address)
            while True:
                my_guess = int(input("Guess A number between 1 and 100:  "))
                if my_guess == -1:
                    do_play = False
                    break
                if my_guess == data:
                    msg = "Congrats Your guess is right!!! Let's play again..."
                    print(msg)
                    socket_connection.sendto('win'.encode(), SERVER_ADDRESS)
                    break
                elif my_guess > data:
                    msg = "Too Big"
                    print(msg)
                else:
                    msg = "Too small"
                    print(msg)
        except OSError:
            print('OSError something went wrong cutting communication with cli')
            do_play = False






