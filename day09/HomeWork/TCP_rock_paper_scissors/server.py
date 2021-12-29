import socket
from common import Options

SERVER_ADDRESS = ('127.0.0.1', 54321)
buffer = 1024


with socket.socket() as server_sock:
    server_sock.bind(SERVER_ADDRESS)
    server_sock.listen(16)
    rounds = 0
    user_score = 0
    my_score = 0

    print("server_sock is listening on port {}...".format(SERVER_ADDRESS[1]))

    try:
        client_obj, address = server_sock.accept()
    except (socket.timeout, BlockingIOError):
        pass

    while True:
        print("waiting for cli to play")
        user_move = client_obj.recv(buffer).decode()
        user_move = Options.from_string(user_move)
        while True:
            my_move = input("Rock/Paper/Scissors?").lower()
            if my_move in ['rock', 'paper', 'scissors', 'r', 'p', 's']:
                my_move = Options.from_string(my_move)
                break
            else:
                print('wrong input type again!')
        rounds = rounds + 1
        round_winner = Options.is_winner(my_move, user_move)
        if round_winner:
            print("you win this round")
            client_obj.send("you loos this round".encode())
            my_score += 1
        elif not round_winner:
            print("you loos this round")
            client_obj.send("you win this round".encode())
            user_score += 1
        elif round_winner is None:
            print("tie on the round")
            client_obj.send("tie on the round".encode())

        if rounds != 0 and rounds % 3 == 0:
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



        # if user_move == my_move:
        #     print("tie on the round")
        #     client_obj.send("tie on the round".encode())
        # elif my_move + " " + user_move in ["paper rock", "p r", "scissors paper", "s p", "rock scissors", "r s"]:
        #     print("you win this round")
        #     client_obj.send("you loos this round".encode())
        #     my_score += 1
        # else:
        #     print("you loos this round")
        #     client_obj.send("you win this round".encode())
        #     user_score += 1
