import socket

SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1204

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("message:")
    s.sendto(message.encode(), SERVER_ADDRESS)
    data, addr = s.recvfrom(BUFFER_SIZE)
    print("response: {}".format(data.decode()))


