import socket
import threading
import time

from client import *


HEADERSIZE = 25
DC_MESSAGE = '!DC'
FORMAT = 'utf-8'

PORT = 5051
IP = socket.gethostbyname(socket.gethostname())


def handle_client(c_socket, c_addr):
    global PLAYERS
    print(f'[NEW CONNECTION DETECTED] {c_addr}')
    
    if len(PLAYERS) == 0:
        sp = SocketPlayer(c_socket, c_addr, 'W')
        PLAYERS.append(sp)
    else:
        sp = SocketPlayer(c_socket, c_addr, 'B')
        PLAYERS.append(sp)

    # while True:
    #     msg_len = c_socket.recv(HEADERSIZE).decode(FORMAT)
    #     if msg_len:
    #         msg_len = int(msg_len)
    #         msg = c_socket.recv(msg_len).decode(FORMAT)
    #         msg = str(msg)

    #         if msg != DC_MESSAGE:
    #             print(f'[NEW MESSAGE FROM] {c_addr}')
    #             print(f'  >{msg}')

def listen():
    global PLAYERS
    print('[SERVER IS LISTENING]')
    while len(PLAYERS) < 2:
        server.listen()
        c_socket, c_addr = server.accept()
        conn = threading.Thread(target=handle_client, args=(c_socket, c_addr))
        conn.start()
        conn.join()
        print(PLAYERS)
        
    print('[BOTH PLAYERS JOINED | GAME STARTS]')


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    print('[SERVER STARTED]')
    listen()
