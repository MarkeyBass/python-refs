import socket

SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_connection:

    do_play = True

    while do_play:
        my_guess = str(input("Guess A number between 1 and 100: "))
        socket_connection.sendto(my_guess.encode(), SERVER_ADDRESS)
        data, address = socket_connection.recvfrom(BUFFER_SIZE)
        print(data.decode())

        if my_guess == '-1':
            do_play = False
            break



