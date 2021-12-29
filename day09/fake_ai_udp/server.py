import socket


# get request data, returns response data
def compute(req):
    message = req.decode().lower()

    if message == 'how are you?':
        response = 'Fine, Thank you.'.encode()
    elif message == 'thank you':
        response = 'You are welcome'.encode()
    elif message == 'goodbye':
        response = 'See you later'.encode()
    elif message == 'hello':
        response = 'Welcome!'.encode()
    else:
        response = 'I did not understand that.'.encode()

    return response


SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1204

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(SERVER_ADDRESS)

print("server is listening at {}:{}".format(*s.getsockname()))
# print(s.getsockname())

while True:
    data, address = s.recvfrom(BUFFER_SIZE)
    print('{}:{}:"{}"'.format(address[0], address[1], data.decode()))

    r = compute(data)
    print('responding: {}'.format(r.decode()))

    s.sendto(r, address)



