import socket
import random

MIN = 1
MAX = 1000
ADDRESS = ('127.0.0.1', 54321)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(ADDRESS)

    secret = random.randint(MIN, MAX)

    while True:
        data, addr = s.recvfrom(1024)

        number = int(data.decode())  # TODO: check for UnicodeDecodeError / ValueError

        if number < secret:
            response_text = "too low"
        elif number > secret:
            response_text = "too high"
        else:
            secret = random.randint(MIN, MAX)
            response_text = "success"

        s.sendto(response_text.encode(), addr)
