from socket import *
import time
class ShellClient:
    def __init__(self):
        self.__socket = socket()
        self.__addr = gethostbyname(gethostname())
        self.__port = 61111
        self.__socket.connect(('127.0.0.1',self.__port))

    def send_msg(self,msg):
        self.__socket.send(msg.encode())
        data = self.__socket.recv(1024)
        print(data.decode())
        # self.__socket.close()

client = ShellClient()
client2 = ShellClient()

client.send_msg("Client1")
client2.send_msg("Client2")
time.sleep(1)
client.send_msg("Client1 second msg")

