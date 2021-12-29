from socket import *
from select import *
import threading
#
class ShellServer:
    def __init__(self):
        self.__socket = socket()
        self.__addr = ('127.0.0.1',61111)
        self.__socket.bind(self.__addr)
        self.__socket.listen(8)
        self.conarr = []
        self.start()

    def broadcast(self):
        for con in self.conarr:
            con.send("broadcast")

    def start(self):
        print('listening')
        while True:
            con, addr = self.__socket.accept()
            self.conarr.append(con)
            threading.Thread(target=self.listen,args=[con,addr]).start()
            # self.listen(con)

    def listen(self,con,addr):
        while True:
            # try:
            data = con.recv(1024)
            # if len(data) == 0:
            #     pass
            # else:
            print(data.decode())
            con.send(data)

            con.send("test".encode())
            # if data == "quit":
            #     self.conarr.remove(con)
            #     break
            # except Exception as e:
            #     print(f"disconnected {addr}")
            #     self.conarr.remove(con)
            #     break


serv = ShellServer()
serv.broadcast()



