import socket

SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER = 1024

with socket.socket() as client_sock:
    client_sock.connect(SERVER_ADDRESS)
    count = 0
    while True:
        if count < 3:
            no_input = True
            while no_input:
                clients_move = input("Rock/Paper/Scissors?").lower()
                if clients_move in ['rock', 'paper', 'scissors', 'r', 'p', 's']:
                    no_input = False
                else:
                    print('wrong input try again!')
                count += 1

        try:
            client_sock.send(clients_move.encode())
            print("waiting for server to play")
            msg_from_server = client_sock.recv(BUFFER).decode()

            print(msg_from_server)
        except ConnectionResetError:
            print("server shut down")
            break

