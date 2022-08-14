import socket
import threading

from socket_helper import *


HEADERSIZE = 25
DC_MESSAGE = '!DC'
FORMAT = 'utf-8'

PORT = 5051
IP = socket.gethostbyname(socket.gethostname())


def handle_client(c_socket, c_addr):
    print(f'[NEW CONNECTION DETECTED] {c_addr}')
    
    if len(SocketPlayer.Players) == 0:
        SocketPlayer.Players.append(SocketPlayer(c_socket, c_addr, 'white'))
        current_player = SocketPlayer.Players[0]
        import chess_main 
    else:
        SocketPlayer.Players.append(SocketPlayer(c_socket, c_addr, 'black'))
        current_player = SocketPlayer.Players[1]


    while True:
        msg_len = c_socket.recv(HEADERSIZE).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = c_socket.recv(msg_len).decode(FORMAT)
            msg = str(msg)

            if msg != DC_MESSAGE:
                print(f'[NEW MESSAGE FROM] {c_addr}')
                print(f'  >{msg}')

def listen():
    print('[SERVER IS LISTENING]')
    while len(SocketPlayer.Players) < 2:
        server.listen()
        c_socket, c_addr = server.accept()
        conn = threading.Thread(target=handle_client, args=(c_socket, c_addr))
        conn.start()
    print('[BOTH PLAYERS JOINED | GAME STARTS]')


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    print('[SERVER STARTED]')
    listen()
