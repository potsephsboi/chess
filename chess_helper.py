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

    for piece in p1.pieces + p2.pieces:
        y = piece.loc[0]
        x = piece.loc[1]
        WIN.blit(piece.image, (80*x, 80*y))
    


def select_piece(mouse):
    from chess_setup import p1, p2
    
    for piece in p1.pieces + p2.pieces:     
        if piece.loc[1]*80 < mouse[0] < (piece.loc[1]+1)*80 and piece.loc[0]*80 < mouse[1] < (piece.loc[0]+1)*80:
            return piece
        

    
            
def find_squares(piece):
    from chess_setup import p1, p2
    
    nbrs = find_nbrs(piece)     # returns [u, d, l, r, ul, ur, dl, dr] 
    print(nbrs)


def find_nbrs(piece):
    from chess_setup import p1, p2

    nbrs = []
    py = piece.loc[0] 
    px = piece.loc[1]
    for test_piece in p1.pieces + p2.pieces:
            y = test_piece.loc[0]
            x = test_piece.loc[1]
            
            if x == px and y == py + 1:     # up
                nbrs.append('u')
            else:
                nbrs.append('-')

            if x == px and y == py - 1:      # down
                nbrs.append('d')
            else:
                nbrs.append('-')

            if x == px - 1 and y == py:     # left    
                nbrs.append('l')
            else:
                nbrs.append('-')

            if x == px + 1 and y == py:     # right    
                nbrs.append('r')
            else:
                nbrs.append('-')

            if x == px - 1 and y == py + 1:     # upleft
                nbrs.append('ul')
            else:
                nbrs.append('-')

            if x == px + 1 and y == py + 1:      # upright
                nbrs.append('ur')
            else:
                nbrs.append('-')

            if x == px - 1 and y == py - 1:     # downleft    
                nbrs.append('dl')
            else:
                nbrs.append('-')

            if x == px - 1 and y == py - 1:     # downright    
                nbrs.append('dr')
            else:
                nbrs.append('-')
