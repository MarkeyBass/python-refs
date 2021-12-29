from socket import *

s = socket(AF_INET, SOCK_DGRAM)

# AF_INET (Adrees Family, Internet Protocol) -> means use IP4
# SOCK_DGRAM (Socket Protocol) means use UDP/IP
# Python uses an API of BSD SOCKETS

# SERVER SOCKET
#          <IP>     <PORT>
s.bind(('127.0.0.1', 54321))
#      <max msg size>
s.recvfrom(1024)

# CLIENT SOCKET

s.sendto(b'HELLO', ('127.0.0.1', 54321))




