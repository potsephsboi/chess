import socket

from socket_helper import *

HEADERSIZE = 25
DC_MSG = '!DC'
FORMAT = 'utf-8'
SERVER_PORT = PORT = 5050
SERVER_IP = IP = socket.gethostbyname(socket.gethostname())


def send(raw_msg, c_socket):
    message = raw_msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADERSIZE-len(send_length))
    c_socket.send(send_length)
    c_socket.send(message)


def receive_data(c_socket):
    while True:
        msg_len = c_socket.recv(HEADERSIZE).decode(FORMAT)
        msg_len = int(msg_len)
        msg = c_socket.recv(msg_len).decode(FORMAT)
        print(f'[NEW MESSAGE] {msg}')



