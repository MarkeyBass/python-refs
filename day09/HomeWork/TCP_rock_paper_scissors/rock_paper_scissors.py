from socket import socket
from socket import timeout


class RPS:
    count = 0
    localhost = '127.0.0.1'
    port_init = 54321
    buffer = 1024

    def __init__(self):

        self.rounds = 0
        RPS.count += 1

        role = input("Would you like to host the game or connect to a host (host / user)? ").lower()
        self.role = role

        if role == "host" or "h":
            self.server()
        elif role == "user" or "u":
            self.cli()

    def server(self):
        server = socket()
        port = RPS.port_init
        server.bind((RPS.localhost, port))
        server.listen(16)

        print("server is listening on port {}...".format(port))

        while True:
            user_score = 0
            my_score = 0
            try:
                client, address = server.accept()
            except (timeout, BlockingIOError):
                pass
            else:
                user_move = client.recv(RPS.buffer).decode()
                while True:
                    my_move = input("Rock/Paper/Scissors?").lower()
                    if my_move != 'rock' or 'paper' or 'scissors' or 'r' or 'p' or 's':
                        print('wrong input type again!')
                    else:
                        self.rounds += 1
                        break
                if user_move == my_move:
                    print("tie on the round")
                elif my_move + " " + user_move == "paper rock" or "p r" \
                        or "scissors paper" or "s p" or "rock scissors" or "r s":
                    print("you win this round")
                    my_score += 1
                else:
                    print("you loos this round")
                    user_score += 1

                if user_score == 3 or my_score == 3:
                    print("Game Over")
                    if my_score > user_score:
                        msg = "You win"
                    elif my_score < user_score:
                        msg = "You loos"
                    else:
                        msg = "Tie"
                    print(msg + " goodbye")
                    break

    def cli(self):
        client = socket()
        client.connect((RPS.localhost, RPS.port_init))
        while True:
            user_score = 0
            my_score = 0

            while True:
                my_move = input("Rock/Paper/Scissors?").lower()
                if my_move != 'rock' or 'paper' or 'scissors' or 'r' or 'p' or 's':
                    print('wrong input type again!')
                else:
                    self.rounds += 1
                    break

            client.send(my_move.encode())
            user_move = client.recv(RPS.buffer).decode()

            if user_move == my_move:
                print("tie on the round")
            elif my_move + " " + user_move == "paper rock" or "p r" \
                    or "scissors paper" or "s p" or "rock scissors" or "r s":
                print("you win this round")
                my_score += 1
            else:
                print("you loos this round")
                user_score += 1

            if user_score == 3 or my_score == 3:
                print("Game Over")
                if my_score > user_score:
                    msg = "You win"
                elif my_score < user_score:
                    msg = "You loos"
                else:
                    msg = "Tie"
                print(msg + " goodbye")
                break


if __name__ == "__main__":
    RPS()


#
# def get_free_port():
#
#     # closing automatically
#     with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
#
#         # ask system to find free port
#         s.bind(('', 0))
#
#         # set socket to be reusable
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#         # return port
#         return s.getsockname()[1]
