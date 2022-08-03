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
        self.legal_moves = -1
        self.moves = []
        Piece.pieces.append(self)
    def __repr__(self):
        return f' -Piece name: {self.name} \n -Piece loc: {self.loc} \n -Piece moves: {self.moves}'

class Pawn(Piece):
    enpassan = None
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
    brooks = []
    wrooks = []

    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
        if self.name[0] == 'B': 
            Rook.brooks.append(self)
        else:
            Rook.wrooks.append(self)
            
        self.has_moved = False 


class Queen(Piece):
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)


class King(Piece):
    kings = []
    def __init__(self, name, value, loc, image):
        super().__init__(name, value, loc, image)
        self.castle = False
        self.has_moved = False
        King.kings.append(self) 