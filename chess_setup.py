from chess_helper import *

WIDTH = 640
HEIGHT = 640

def init_window():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

                              # y, x
p1 = Player(1, [Piece('K', 99, [7, 4], pygame.image.load('pieces/white/king.png')),
                Piece('Q', 9, [7, 3], pygame.image.load('pieces/white/queen.png')), 
                Piece('B', 3, [7, 2], pygame.image.load('pieces/white/bishop.png')),
                Piece('B', 3, [7, 5], pygame.image.load('pieces/white/bishop.png')), 
                Piece('N', 3, [7, 1], pygame.image.load('pieces/white/knight.png')),
                Piece('N', 3, [7, 6], pygame.image.load('pieces/white/knight.png')), 
                Piece('R', 5, [7, 0], pygame.image.load('pieces/white/rook.png')), 
                Piece('R', 5, [7, 7], pygame.image.load('pieces/white/rook.png')), 
                
            ])
p1pawns = [Pawn('P', 1, [6, i], pygame.image.load('pieces/white/pawn.png')) for i in range(8)] 

p1.pieces += p1pawns


p2 = Player(2, [Piece('K', 99, [0, 4], pygame.image.load('pieces/black/bking.png')),
                Piece('Q', 9, [0, 3], pygame.image.load('pieces/black/bqueen.png')), 
                Piece('B', 3, [0, 2], pygame.image.load('pieces/black/bbishop.png')),
                Piece('B', 3, [0, 5], pygame.image.load('pieces/black/bbishop.png')),
                Piece('N', 3, [0, 1], pygame.image.load('pieces/black/bknight.png')),
                Piece('N', 3, [0, 6], pygame.image.load('pieces/black/bknight.png')),
                Piece('R', 5, [0, 0], pygame.image.load('pieces/black/brook.png')),
                Piece('R', 5, [0, 7], pygame.image.load('pieces/black/brook.png')), 
                 
            ])
p2pawns = [Pawn('P', 1, [1, i], pygame.image.load('pieces/black/bpawn.png')) for i in range(8)]

p2.pieces += p2pawns

