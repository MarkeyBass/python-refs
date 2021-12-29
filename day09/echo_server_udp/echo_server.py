import socket

SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1204

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(SERVER_ADDRESS)

print("server is listening at {}:{}".format(*s.getsockname()))

while True:
    data, addr = s.recvfrom(BUFFER_SIZE)
    print('{}:{}:"{}"'.format(addr[0], addr[1], data.decode()))
    s.sendto(data, addr)



