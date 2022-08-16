import socket

HEADERSIZE = 25
DC_MSG = '!DC'
FORMAT = 'utf-8'
SERVER_PORT = PORT = 5051
SERVER_IP = IP = socket.gethostbyname(socket.gethostname())


PLAYERS = []
class SocketPlayer:
    
    def __init__(self, socket, addr, color) -> None:
        self.socket = socket
        self.addr = addr
        self.color = color
        self.connected = True
        
    def __repr__(self) -> str:
        return f'[{self.color}] // [SOCKET INFO]{self.addr} // [CONN STATUS] {self.connected}'



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



