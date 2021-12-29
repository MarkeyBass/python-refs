import socket
import re


localhost = '127.0.0.1'
port = 54321
SERVER_ADDRESS = ('127.0.0.1', 54321)
buffer = 1024

rounds = 0


def server():
    global rounds
    server_sock = socket.socket()
    server_sock.bind(SERVER_ADDRESS)
    server_sock.listen(16)

    print("server_sock is listening on port {}...".format(port))

    while True:
        user_score = 0
        my_score = 0
        try:
            client_obj, address = server_sock.accept()
        except (socket.timeout, BlockingIOError):
            pass
        else:
            user_move = client_obj.recv(buffer).decode()
            while True:
                my_move = input("Rock/Paper/Scissors?").lower()
                if my_move != 'rock' or 'paper' or 'scissors' or 'r' or 'p' or 's':
                    print('wrong input type again!')
                else:
                    rounds = rounds + 1
                    break
            if user_move == my_move:
                print("tie on the round")
            elif my_move + " " + user_move == "paper rock" or "p r" \
                    or "scissors paper" or "s p" or "rock scissors" or "r s":
                print("you win this round")
                client_obj.send("you loos this round".encode())
                my_score += 1
            else:
                print("you loos this round")
                client_obj.send("you loos this round".encode())
                user_score += 1

            if user_score == 3 or my_score == 3:
                print("Game Over")
                if my_score > user_score:
                    msg = "You win"
                    msg_to_user = "You loos"
                elif my_score < user_score:
                    msg = "You loos"
                    msg_to_user = "You win"
                else:
                    msg = "Tie"
                    msg_to_user = msg
                print(msg + " goodbye")
                client_obj.send(msg_to_user.encode())
                break


def cli():
    global rounds
    with socket.socket() as client_sock:
        client_sock.connect(SERVER_ADDRESS)
        while True:
            while True:
                clients_move = input("Rock/Paper/Scissors?").lower()
                if clients_move != 'rock' or 'paper' or 'scissors' or 'r' or 'p' or 's':
                    print('wrong input type again!')
                else:
                    rounds += 1
                    break

                client_sock.send(clients_move.encode())
                msg_from_server = client_sock.recv(buffer).decode()

                print(msg_from_server)

                if re.search(" goodbye$", msg_from_server):
                    break


if __name__ == "__main__":
    role = input("Would you like to host the game or connect to a host (host / user)? ").lower()
    if role == "host" or "h":
        server()
    elif role == "user" or "u":
        cli()
    else:
        print("wrong input")
