from socket import *

s = socket(AF_INET, SOCK_DGRAM)

# CLIENT SOCKET

s.sendto(b'HELLO', ('127.0.0.1', 54321))



