import socket


HEADERSIZE = 25
DC_MSG = '!DC'
FORMAT = 'utf-8'
SERVER_PORT = PORT = 5051
SERVER_IP = IP = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_IP, SERVER_PORT))


def send(raw_msg):
    message = raw_msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADERSIZE-len(send_length))
    client.send(send_length)
    client.send(message)


def receive_data():
    while True:
        msg_len = client.recv(HEADERSIZE).decode(FORMAT)
        msg_len = int(msg_len)
        msg = client.recv(msg_len).decode(FORMAT)
        print(f'[NEW MESSAGE] {msg}')


send('testing server recv')
receive_data()

