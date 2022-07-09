import pygame


col_dict = {
    'a': 0,
    'b': 1, 
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7

}


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (115, 147, 179)

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



def display_grid(surface):
    x_lines = []
    y_lines = []
    for i in range(8):
        x_line = pygame.Rect(0, 80 * (i + 1), 640, 5)
        x_lines.append(x_line)
    for k in range(8):
        y_line = pygame.Rect(80 * (k + 1), 0, 5, 640)
        y_lines.append(y_line)
    for xl in x_lines:
        pygame.draw.rect(surface, BLACK, xl)
    for yl in y_lines:
        pygame.draw.rect(surface, BLACK, yl)


def show_pieces():
    from chess_setup import p1, p2
    from chess_main import WIN
    for piece in p1.pieces:
        if type(piece) != list:
            WIN.blit(piece.image, (0, 0))







