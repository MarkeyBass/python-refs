import socket
import getpass
import json

SERVER_ADDRESS = ('127.0.0.1', 54322)
BUFSIZE = 1024


with socket.socket() as s:
    s.connect(SERVER_ADDRESS)

    while True:
        action = input("enter action (login/register/quit)").lower().strip()

        if action in ('q', 'quit'):
            print('goodbye')
            break
        elif action in ('l', 'login'):
            s.send('login'.encode())
            response_text = s.recv(BUFSIZE).decode()
            if response_text == 'good_action':
                login_cred = {
                    'email': input("enter email:"),
                    'password': getpass.getpass('password:')
                }

                login_cred_data = json.dumps(login_cred).encode()

                s.send(login_cred_data)

                response_text = s.recv(BUFSIZE).decode()
                if response_text == 'good_login':
                    print("connected successfully")
                else:
                    print("bad credentials")

        elif action in ('r', 'register'):
            s.send('register'.encode())
            response_text = s.recv(BUFSIZE).decode()
            if response_text == 'good_action':
                # get email
                while True:
                    email = input("enter email to register:").lower().strip()
                    # TODO: (later) check email valid with regex

                    s.send(email.encode())
                    response_text = s.recv(BUFSIZE)

                    if response_text == 'email_taken':
                        print("this email is already taken")
                    else:
                        break

                # get password
                while True:
                    password = getpass.getpass('enter new password:')
                    password_again = getpass.getpass('enter new password again:')

                    if password != password_again:
                        print("passwords are different")
                    else:
                        break

                s.send(password.encode())
                response_text = s.recv(BUFSIZE).decode()

                print(response_text)

                if response_text == 'good_password':
                    print("registered successfully")
                else:
                    print("register failed?")

        else:
            print("invalid action!")
