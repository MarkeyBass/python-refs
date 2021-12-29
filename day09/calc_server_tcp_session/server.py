import socket

# הגדרה של טיים אאוט אוטומטי עבור סוקט - הסוקט נוצר מלחתיחילה עם הטיים אאוט הזה
#socket.setdefaulttimeout(0.5)
socket.setdefaulttimeout(0)

SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1024

clients = []

with socket.socket() as server:

    server.bind(SERVER_ADDRESS)
    server.listen(16)

    print("server is listening at {}:{}".format(*SERVER_ADDRESS))

    # loop for accepting new clients and receiving responses
    while True:

        try:
            client_sock, client_addr = server.accept()  # this block responsible on accepting new clients
        # <handles timeout error>  <handles immediate mode err>
        except (socket.timeout, BlockingIOError) as e:  # those exceptions mean that we don have a cli that is wy we "pass"
            pass
        else:
            print("connection connected from {}:{}".format(*client_addr))
            # print("Clients socket: {}".format(client_sock))
            # print("Clients peer name: {}".format(client_sock.getpeername()))
            clients.append(client_sock)

        for client in clients.copy():

            try:
                data = client.recv(BUFFER_SIZE)

            except (socket.timeout, BlockingIOError):  # we don't use OSError here because it wii catch other errors as well
                pass

            except OSError:  # here we deal with all OSErrors
                print("connection {}:{} crashed".format(*client.getpeername()))
                clients.remove(client)

            else:
                if len(data) == 0:  # connection closed so we'll remove it from the list ??????
                    # אם ההודעה ריקה זה אומר שהקליינט סגר?
                    print("connection {}:{} closed".format(*client.getpeername()))
                    clients.remove(client)
                else:
                    text = data.decode()
                    n1, op, n2 = text.split()
                    n1 = int(n1)
                    n2 = int(n2)

                    if op == '+':
                        resp = str(n1 + n2)
                    elif op == '-':
                        resp = str(n1 - n2)
                    # ...
                    else:
                        resp = 'operator not supported'

                    client.send(resp.encode())
















