import socket
import json
import datetime
import select
import sqlite3 as sql

DB_FILE = "all_stations.sqlite"
JSON_FILE = "all_stations.json"
ADDRESS = ("127.0.0.1", 54321)
BUFF_MAX = 1024

with socket.socket() as server_socket:
    server_socket.bind(ADDRESS)
    server_socket.listen(16)
    print("Server listening on port {}...".format(ADDRESS[1]))

    client_diction = {}  # {client : address}

    while True:
        client_list = list(client_diction)

        # working with select API to allow multiple clients to work simultaneously with server:
        r_list, _, x_list = select.select(
            [server_socket] + client_list,
            [],
            client_list
        )

        for client in x_list:
            print("client {}:{} crashed".format(*client_diction[client]))
            del client_diction[client]

        for sock in r_list:
            # Handling actions for server in r_list
            if sock is server_socket:
                new_client, address = server_socket.accept()
                client_diction[new_client] = address
                print("client connected {}:{}".format(*address))
            # Handling actions for server in r_list
            else:
                client = sock
                try:
                    # RECEIVING DATA FROM CLIENT
                    data = client.recv(BUFF_MAX)
                    if len(data) == 0:
                        print("client {}:{} disconnected".format(*client_diction[client]))
                        del client_diction[client]
                    else:
                        data_dic = json.loads(data.decode())
                except json.decoder.JSONDecodeError:
                    print(f"client {client_diction[client]} sent wrong data format!")
                    client.send("SERVER MSG: you attempted to send data in wrong format. json is expected".encode())
                except ConnectionResetError:
                    print("ConnectionResetError: client {}:{} unexpectedly disconnected".format(*client_diction[client]))
                    del client_diction[client]
                else:
                    if data_dic == {}:
                        print(f"client {client_diction[client]} sent wrong data!")
                        client.send("SERVER MSG: you attempted to send wrong data".encode())
                    elif data_dic == {"msg": "client dealing with FileNotFoundError"}:
                        print(f"client {client_diction[client]} dealing with FileNotFoundError")
                        client.send("SERVER MSG: got that you are dealing with FileNotFoundError".encode())
                    else:
                        last_update = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(f"{last_update} client {client_diction[client]} sent {data_dic}")
                        client.send(f"Server received data at {last_update}".encode())

                        # Database implementation
                        with sql.connect(DB_FILE) as conn:
                            cur = conn.cursor()
                            cur.execute(
                                """
                                    CREATE TABLE IF NOT EXISTS station_status(
                                        station_id STRING PRIMARY KEY,
                                        alert_1 INT NOT NULL,
                                        alert_2 INT NOT NULL,
                                        update_time TEXT
                                    ) 
                                """
                            )
                            conn.commit()

                            cur.execute(
                                """SELECT * FROM station_status WHERE station_id = ? """,
                                (data_dic['station_id'],)
                            )
                            # print(cur.fetchall())
                            # print(cur.rowcount)
                            if len([cur.fetchall()]) == 0:
                                cur.execute(
                                    """INSERT INTO station_status VALUES (?,?,?,?)""",
                                    (data_dic["station_id"], data_dic["alert_1"], data_dic["alert_2"], str(last_update))
                                )
                                conn.commit()
                            elif len([cur.fetchall()]) > 0:
                                cur.execute(
                                    """
                                    UPDATE station_status 
                                    SET alert_1 = ?, alert_2 = ?, update_time = ?
                                    WHERE station_id = ?
                                    """,
                                    (data_dic['alert_1'], data_dic['alert_2'], str(last_update), data_dic['station_id'])
                                )
                                conn.commit()
                            # else:
                            #     # case of attack on the database
                            #     print("CRITICAL PROBLEM in the database pleas make validations!!!\n Server closing..")
                            #     print("cursor row count", cur)
                            #     break

                            # creating json file with data from the database
                            cur.execute("SELECT * FROM station_status")
                            all_stations_dic = {}
                            for line in cur:
                                # print(list(line))
                                all_stations_dic[line[0]] = {
                                    "alert_1": line[1],
                                    "alert_2": line[2],
                                    "update_time": line[3]
                                }

                            stations_json = json.dumps(all_stations_dic)
                            with open(JSON_FILE, "w+") as f:
                                json.dump(all_stations_dic, f)
                                # f.write(stations_json)
                                f.flush()



