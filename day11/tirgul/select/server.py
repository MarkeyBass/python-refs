from socket import *
from select import *

#
class ShellServer:
    def __init__(self):
        self.__socket = socket()
        self.__addr = ('127.0.0.1',61111)
        self.__socket.bind(self.__addr)
        self.__socket.listen(8)
        self.conarr = [ self.__socket]
        self.start()


    def start(self):
        print('listening')
        while True:
            rlist, _,xlist = select(self.conarr,[],self.conarr)
            for soc in xlist:
                print("err")
            for soc in rlist:
                if soc is self.__socket:
                    con,addr = self.__socket.accept()
                    self.conarr.append(con)
                else:
                    self.listen(soc)

    def listen(self,con):
        # while True:
        data = con.recv(1024)
        if len(data) == 0:
            # con.close()
            pass
        else:
            print(data.decode())
            con.send(data)

serv = ShellServer()




