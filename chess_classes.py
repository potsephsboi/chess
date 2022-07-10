class Player:
    def __init__(self, identity, pieces):
        self.identity = identity
        self.pieces = pieces

    def __repr__(self) -> str:
        return f'Player {self.identity} - {len(self.pieces)} pieces remaining {[p for p in self.pieces]}'


class Piece:
    def __init__(self, name, value, loc, image):
        self.name = name 
        self.value = value 
        self.loc = loc
        self.image = image
    def __repr__(self):
        return f'Piece name: {self.name}'

class Pawn(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
        self.motion = '1u'  # one up
        self.take = '1ud'   # one up diagonally

        

class Knight(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)

class Bishop(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
        self.motion = '-d'  # unrestricted diagonally 
        self.take = '-d'    # unrestricted diagonall


class Rook(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
        self.motion = '-c'  # unrestricted cross
        self.take = '-c'    # unrestricted cross


class Queen(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
        self.motion = '-a'  # unrestricted all
        self.take = '-a'    # unrestricted all


class King(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
        self.motion = '1a'  # one all
        self.take = '1a'    # one all