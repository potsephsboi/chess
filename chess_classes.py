class Player:
    def __init__(self, identity, pieces):
        self.identity = identity
        self.pieces = pieces

    def __repr__(self) -> str:
        return f'Player {self.identity} - {len(self.pieces)} pieces remaining {[p for p in self.pieces]}'


class Piece:

    pieces = []
    def __init__(self, name, value, loc, image):
        self.name = name 
        self.value = value 
        self.loc = loc
        self.image = image
        self.moves = []
        Piece.pieces.append(self)
    def __repr__(self):
        return f'Piece name: {self.name} -- Piece moves: {self.moves}'

class Pawn(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
        self.has_moved = False

class Knight(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)

class Bishop(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)



class Rook(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
        


class Queen(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)


class King(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
