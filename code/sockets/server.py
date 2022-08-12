import socket
import threading


HEADERSIZE = 25
DC_MESSAGE = '!DC'
FORMAT = 'utf-8'

PORT = 5051
IP = socket.gethostbyname(socket.gethostname())


def handle_client(c_socket, c_addr):
    print(f'[NEW CONNECTION DETECTED] {c_addr}')
    print(f'[ACTIVE CONNECTIONS] {threading.active_count()-1}')

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
    server.listen()
    print('[SERVER IS LISTENING]')
    while True:
        c_socket, c_addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(c_socket, c_addr))
        thread.start()


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    print('[SERVER STARTED]')
    listen()
