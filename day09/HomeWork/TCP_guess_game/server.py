import socket
from random import randint

socket.setdefaulttimeout(0.5)

SEVER_ADDRESS = ('127.0.0.1', 55555)
BUFFER_SIZE = 1025

clients = []

with socket.socket() as server:
    server.bind(SEVER_ADDRESS)
    server.listen(16)

    print("server is listening on port {}...".format(SEVER_ADDRESS[1]))

    while True:
        try:
            client, address = server.accept()
        except (socket.timeout, BlockingIOError) as err:
            # print(err)
            pass
        else:
            if client not in clients:
                print(f"cli {address[0]}:{address[1]} connected")
                clients.append({
                    "address": address,
                    "obj": client,
                    "tries": 5,
                    "rand": randint(1, 30)
                })
                print(clients[-1]['rand'])

        for i in range(len(clients)):
            try:
                data = clients[i]["obj"].recv(BUFFER_SIZE).decode()

            except (socket.timeout, BlockingIOError):
                pass
            else:
                if len(data) == 0:
                    print("connection {}:{} closed".format(*client.getpeername()))
                    del clients[i]
                    break
                else:
                    data = int(data)
                if clients[i]["tries"] == 0:
                    res = "No tries left"
                    clients[i]["obj"].send(res.encode())
                    clients[i]["rand"] = randint(1, 30)
                    clients[i]["tries"] = 5
                    break
                if data == clients[i]["rand"]:
                    res = 'You won!!! lets play again...'
                    clients[i]["tries"] = 5
                    clients[i]["rand"] = randint(1, 30)
                elif data > clients[i]["rand"]:
                    res = "Too big"
                else:
                    res = "Too small"

                clients[i]["tries"] -= 1
                clients[i]["obj"].send(res.encode())
