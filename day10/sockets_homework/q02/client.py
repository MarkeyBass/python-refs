import socket

MIN = 1
MAX = 1000
SERVER_ADDRESS = ('127.0.0.1', 54321)

BYTE_SIZE = 4
BYTE_ORDER = 'little'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    print("I'm thinking of a number between {} and {}".format(MIN, MAX))
    print("can you guess it?")

    while True:
        guess_number = int(input("guess:"))  # TODO: add exception checks

        s.sendto(guess_number.to_bytes(BYTE_SIZE, BYTE_ORDER), SERVER_ADDRESS)

        response_data, addr = s.recvfrom(1024)
        # TODO: check addr == SERVER_ADDRESS
        print(response_data.decode())
