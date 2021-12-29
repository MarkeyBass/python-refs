import socket as socket_library
import json as json_library
import select as select_library

# constants
ADDRESS = ('127.0.0.1', 54322)
MAX_SIZE = 1024


# TYPES
class Session:
    def __init__(self, addr):
        self.addr = addr
        self.state = 'begin'  # begin/login/register/register_password
        self.email = None  # to store email for registering


# GLOBALS
accounts = {
    'david@gmail.com': '123456',
    'moshe@walla.co.il': 'moshe123'
}

sessions = {}  # {client: session}

# MAIN
if __name__ == '__main__':

    with socket_library.socket() as accept_socket:

        accept_socket.bind(ADDRESS)
        accept_socket.listen(16)

        while True:

            client_list = list(sessions)

            rlist, _, xlist = select_library.select(
                [accept_socket] + client_list,
                [],
                client_list)

            for client in xlist:
                print("client crashed {}:{}".format(*sessions[client].addr))
                del sessions[client]

            for sock in rlist:
                # print("sock: ",sock)
                print(rlist)
                if sock is accept_socket:
                    new_client, addr = accept_socket.accept()
                    sessions[new_client] = Session(addr)
                    print("client connected {}:{}".format(*addr))

                else:
                    connected_client = sock
                    try:
                        data = connected_client.recv(MAX_SIZE)
                    except ConnectionResetError as error:
                        print("client is ", error)
                        del sessions[connected_client]
                        continue
                    state = sessions[connected_client].state
                    addr = sessions[connected_client].addr

                    if len(data) == 0:
                        print("client disconnect {}:{}".format(*addr))
                        del sessions[connected_client]

                    elif state == 'begin':
                        action = data.decode()  # TODO: (later) check decode errors
                        if action in ('login', 'register'):
                            sessions[connected_client].state = action
                            print("client {} {}:{}".format(action, *addr))
                            connected_client.send('good_action'.encode())

                        else:
                            print("client action error {}:{}".format(*addr))
                            connected_client.send('bad_action'.encode())

                    elif state == 'login':
                        login_cred = json_library.loads(data.decode())
                        # TODO: (later) check login_cred is a dict with keys 'email' 'password'
                        #       and with valid email password values (strings)

                        email = login_cred['email']
                        password = login_cred['password']

                        # if password == accounts.get(email):
                        if email in accounts and password == accounts[email]:
                            print("client successful connection {}:{}".format(*addr))
                            connected_client.send('good_login'.encode())
                        else:
                            print("client bad credentials {}:{}".format(*addr))
                            connected_client.send('bad_login'.encode())

                        sessions[connected_client].state = 'begin'

                    elif state == 'register':
                        email = data.decode()  # TODO: (later) check decode errors

                        if email in accounts:
                            print("client email {} taken {}:{}".format(email, *addr))
                            connected_client.send('email_taken'.encode())
                        else:
                            print("client email {} free {}:{}".format(email, *addr))
                            connected_client.send('email_free'.encode())
                            sessions[connected_client].state = 'register_password'
                            sessions[connected_client].email = email
                            accounts[email] = None

                    elif state == 'register_password':
                        password = data.decode()  # TODO: (later) check decode errors
                        email = sessions[connected_client].email

                        accounts[email] = password

                        print("client register finish {} free {}:{}".format(email, *addr))
                        connected_client.send('good_password'.encode())

                        sessions[connected_client].state = 'begin'

                    # TODO: (later) add else? to check invalid state?
