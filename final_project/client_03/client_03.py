import socket
import json
import time

"""
    client will send data to the server via json format
    if ValueError occurs empty json will be sent to the server
"""

ADDRESS = ("127.0.0.1", 54321)
BUFF_MAX = 1024

display_connection_msg = True
display_connection_closed_msg = True
display_value_error_msg = True

try:
    with socket.socket() as s:
        s.connect(ADDRESS)
        while True:
            if display_connection_msg is True:
                print("client connected to {} successfully...".format(ADDRESS))
                display_connection_msg = False
                display_connection_closed_msg = True
            time.sleep(10)
            with open("status.txt", "r") as f:
                try:
                    my_dictionary = {
                        "station_id": int(f.readline()),
                        "alert_1": int(f.readline()),
                        "alert_2": int(f.readline())
                    }
                except ValueError:
                    if display_value_error_msg is True:
                        print("You have entered wrong values to the file. Pleas Fix")
                    display_value_error_msg = False
                    data = json.dumps({}).encode()  # sending an empty dictionary to server (wrong data type alert)

                else:
                    display_value_error_msg = True
                    data = json.dumps(my_dictionary).encode()
            try:
                s.send(data)
                response_text = s.recv(BUFF_MAX).decode()
                print(response_text)
            except ConnectionResetError:
                print('An existing connection was forcibly closed by the remote host')
                print("Trying to reconnect...")
                display_connection_closed_msg = False
                display_connection_msg = True
except ConnectionRefusedError:
    print("The server is not connected/working.")
    exit()

