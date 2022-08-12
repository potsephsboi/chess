from this import d


class SocketPlayer:
    Players = []
    
    def __init__(self, socket, addr, color) -> None:
        self.socket = socket
        self.addr = addr
        self.color = color
        self.connected = True
        SocketPlayer.Players.append(self)
    def __repr__(self) -> str:
        return f'[{self.color.upper()}] // [CONN STATUS] {self.connected}'
