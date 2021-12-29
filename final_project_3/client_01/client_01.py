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


def reconnecting_to_server(client_socket, err):
    print('An existing connection was forcibly closed by the remote host')
    print("Trying to reconnect...")
    print(err)
    client_socket.close()
    client_socket = socket.socket()
    # is_connected = False
    not_connected = True
    # while not is_connected:
    while not_connected:
        try:
            client_socket.connect(ADDRESS)
            # is_connected = True
            not_connected = False
            print("client has reconnected successfully...")
            return client_socket
        except OSError as err:
            print(err)
            time.sleep(SLEEP_TIME)


def read_data_file(file_name, value_error_counter):
    try:
        with open(file_name, "r") as f:
            try:

                my_dictionary = {
                    "station_id": int(f.readline()),
                    "alert_1": int(f.readline()),
                    "alert_2": int(f.readline())
                }
                # TODO: remove this debugging line
                my_dictionary = {}
                if (my_dictionary["station_id"] < 0
                        or my_dictionary["alert_1"] > 1 or my_dictionary["alert_1"] < 0
                        or my_dictionary["alert_2"] > 1 or my_dictionary["alert_2"] < 0):
                    raise ValueError
                data = json.dumps(my_dictionary).encode()
                # data = my_dictionary
                value_error_counter = 0
                return [data, value_error_counter]
            except ValueError:
                if value_error_counter == 0:
                    print("You have entered wrong values to the file. Pleas Fix")
                    value_error_counter += 1

                # sending an empty dictionary to server (wrong data type alert)
                # the empty {} will be sent first to the father function "main_flow", it will send it to the server
                data = json.dumps({}).encode()
                # data = {}
                return [data, value_error_counter]
    # handling file system exceptions
    except FileNotFoundError:
        # time.sleep(3)
        data = json.dumps({"msg": "client dealing with FileNotFoundError"}).encode()
        # data = {"msg": "client dealing with FileNotFoundError"}
        if value_error_counter == 0:
            print("file {} does not exist. pleas create it properly. Restart the process if needed".format(FILE_NAME))
        value_error_counter += 1
        return [data, value_error_counter]


def main_flow():
    try:
        s = socket.socket()
        s.connect(ADDRESS)
        print("client connected to {} successfully...".format(ADDRESS))

        # the value_error_counter variable will make the client send the ValueError msg only once.
        # station_id must be a positive int. alerts must be 0 or 1 only.
        value_error_counter = 0
        while True:
            [data, value_error_counter] = read_data_file(FILE_NAME, value_error_counter)
            try:
                # sending the data to the server in json format and encoded
                # s.send(json.dumps(data).encode())
                s.send(data)
                response_text = s.recv(BUFF_MAX).decode()

                if value_error_counter == 0:
                    print(response_text)
                # if data == {"msg": "client dealing with FileNotFoundError"}:
                # if value_error_counter == 0 and json.loads(data) == {"msg": "client dealing with FileNotFoundError"}:
                    # print("file {} does not exist. pleas create it properly and then start the program".format(FILE_NAME))
                    # print("file {} does not exist. pleas create it properly.".format(FILE_NAME))
                    # print("program is quitting...")
                    # exit()
                    # quit()
                time.sleep(SLEEP_TIME)
            # Reconnecting Automatically to Server in case of broken communication (Works only after successful initial communication)
            except (ConnectionResetError,
                    OSError) as err:  # TODO: What about OSError, Check about socket.error - Go handle ConnectionResetError and FileNotFoundError at the same time
                s = reconnecting_to_server(s, err)
                time.sleep(SLEEP_TIME)

    # If initially connection was not established the client will not try to reconnect and process will exit.
    except ConnectionRefusedError:
        print("The server is not connected/working.")
        print("connection closed.")
        exit()


if __name__ == "__main__":
    main_flow()
