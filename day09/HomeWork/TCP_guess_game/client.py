import socket

SEVER_ADDRESS = ('127.0.0.1', 55555)
BUFFER_SIZE = 1025

with socket.socket() as s:

    s.connect(SEVER_ADDRESS)

    print("guess a number (1-30) you have 5 guesses in each round, type -1 to quit.")
    guess = -10
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Input must be an integer !!!")

        if guess == -1:
            print("goodbye!!!")
            s.close()
            break

        data = str(guess).encode()
        s.send(data)
        resp = s.recv(BUFFER_SIZE).decode()
        print(resp)

        if resp == 'You won!!! lets play again...' or resp == "No tries left":
            play_again = input("Would you like to play again? (Y/N)? ").lower()
            if play_again == 'n':
                print("goodbye!!!")
                break


