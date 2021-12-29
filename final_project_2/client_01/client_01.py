import socket
import json
import time

"""
    client will send data to the server via json format
    if ValueError occurs empty json will be sent to the server
"""

ADDRESS = ("127.0.0.1", 54321)
BUFF_MAX = 1024
FILE_NAME = "status_1.txt"
SLEEP_TIME = 5

try:
    s = socket.socket()
    s.connect(ADDRESS)
    print("client connected to {} successfully...".format(ADDRESS))

    # the value_error_counter will make the client send the ValueError msg only once.
    # station_id must be a positive int. alerts must be 0 or 1 only.
    value_error_counter = 0
    while True:
        time.sleep(SLEEP_TIME)
        try:
            with open(FILE_NAME, "r") as f:
                try:
                    my_dictionary = {
                        "station_id": int(f.readline()),
                        "alert_1": int(f.readline()),
                        "alert_2": int(f.readline())
                    }

                    if (my_dictionary["station_id"] < 0
                            or my_dictionary["alert_1"] > 1 or my_dictionary["alert_1"] < 0
                            or my_dictionary["alert_2"] > 1 or my_dictionary["alert_2"] < 0):
                        raise ValueError
                    data = json.dumps(my_dictionary).encode()
                    value_error_counter = 0
                except ValueError:
                    if value_error_counter == 0:
                        print("You have entered wrong values to the file. Pleas Fix")
                        value_error_counter += 1

                    data = json.dumps({}).encode()  # sending an empty dictionary to server (wrong data type alert)
                # else:
                #     data = json.dumps(my_dictionary).encode()
        # handling file system exceptions
        except FileNotFoundError:
            print("file {} does not exist. pleas create it properly and then start the program".format(FILE_NAME))
            print("program is quitting...")
            time.sleep(3)
            data = json.dumps({"msg": "client dealing with FileNotFoundError"}).encode()
            s.send(data)
            quit()
        try:
            s.send(data)
            response_text = s.recv(BUFF_MAX).decode()
            if value_error_counter == 0:
                print(response_text)
        # Reconnecting Automatically to Server in case of broken communication (Works only after successful initial communication)
        except (ConnectionResetError, OSError) as err:  # TODO: What about OSError, Check about socket.error - Go handle ConnectionResetError and FileNotFoundError at the same time
            print('An existing connection was forcibly closed by the remote host')
            print("Trying to reconnect...")
            print(err)
            s.close()
            s = socket.socket()
            is_connected = False
            while not is_connected:
                try:
                    s.connect(ADDRESS)
                    is_connected = True
                    print("client has reconnected successfully...")
                except OSError as err:
                    print(err)
                    time.sleep(SLEEP_TIME)

# If initially connection was not established the client will not try to reconnect
except ConnectionRefusedError:
    print("The server is not connected/working.")
    print("connection closed.")
    exit()

# TODO: Remove all unneeded notes
# https://instructobit.com/tutorial/101/Reconnect-a-Python-socket-after-it-has-lost-its-connection
