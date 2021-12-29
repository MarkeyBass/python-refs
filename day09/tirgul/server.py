import socket
from copy import copy
import os


SERVER_ADDRESS = ('127.0.0.1', 54322)
BUFFER_SIZE = 1024
W_LIST = [
    {
        "name": "user1", "password": "123456"
    },
    {
        "name": "user2", "password": "654321"
    }
]


class MySocket:
    def __init__(self, ip_port=SERVER_ADDRESS, b_size=BUFFER_SIZE, users_num=16, w_list=W_LIST):
        self.ip_port = ip_port
        self.b_size = b_size
        self.users_num = users_num
        self.w_list = w_list

    def login(self, connection):
        while True:
            # connection.send("Enter username:".encode())
            # username = connection.recv(self.b_size).decode()
            # connection.send("Enter password:".encode())
            # password = connection.recv(self.b_size).decode()
            data = connection.recv(self.b_size).decode()
            username, password = data.split()
            for usr in self.w_list:
                if usr['name'] == username and usr['password'] == password:
                    connection.send('success'.encode())
                    return True
                    # return f"fHello {username} welcome aboard!!!"
            connection.send("Wrong credentials!!! sign in again".encode())

    def open_socket(self):
        with socket.socket() as accept_socket:
            accept_socket.bind(self.ip_port)
            accept_socket.listen(self.users_num)

            while True:
                print("server is listening at {}:{}".format(*accept_socket.getsockname()))
                c, address = accept_socket.accept()
                print("accepted connection from {}:{}".format(*address))

                self.login(c)

                not_quitting = True
                while not_quitting:
                    try:
                        data = c.recv(self.b_size)
                        print('{}:{}:"{}"'.format(*address, data.decode()))

                        message = data.decode().lower()

                        if message in ('goodbye', 'quit', 'end', 'q', 'exit', 'bye'):
                            response = 'See you later'.encode()
                            not_quitting = False
                        else:
                            user_command = os.popen(message).read()
                            response = user_command.encode()

                            # user_command = os.system(message)
                            # response = user_command.encode()
                            # response = 'I did not understand that.'.encode()

                        print('responding: {}'.format(response.decode()))

                        c.send(response)
                    except(Exception, OSError):
                        print("Illegal command")
                        break

                c.close()


if __name__ == '__main__':
    mySock = MySocket()
    mySock.open_socket()
