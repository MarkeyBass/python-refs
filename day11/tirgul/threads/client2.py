from socket import *
import time
import threading
import random
class ShellClient:
    def __init__(self,name):
        self.__socket = socket()
        self.__name = name
        self.__addr = gethostbyname(gethostname())
        self.__port = 61111
        self.__socket.connect(('127.0.0.1',self.__port))

    def send_msg(self,msg):
        self.__socket.send(msg.encode())
        data = self.__socket.recv(1024)
        print(self.__name ,data.decode())
        # while True:
        data = self.__socket.recv(1024)
        print(self.__name ,data.decode())

        self.__socket.close()
            # break

client = ShellClient("Client1")
client2 = ShellClient("Client2")
# threading.Thread(target=client.send_msg,args=["msg1"]).start()
# threading.Thread(target=client2.send_msg,args=["msg2"]).start()

client.send_msg("Client1")
client2.send_msg("Client2")
# time.sleep(1)
# client.send_msg("Client1 second msg")

