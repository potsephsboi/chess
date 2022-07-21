from chess_frontend import *
from chess_backend import *

WIDTH = 640
HEIGHT = 640

      
av_move = pygame.image.load('assets/del.png')

                              # y, x
p1 = Player(1, [Piece('WK', 99, [7, 4], pygame.image.load('assets/pieces/white/king.png')),
                Piece('WQ', 9, [7, 3], pygame.image.load('assets/pieces/white/queen.png')), 
                Piece('WB', 3, [7, 2], pygame.image.load('assets/pieces/white/bishop.png')),
                Piece('WB', 3, [7, 5], pygame.image.load('assets/pieces/white/bishop.png')), 
                Piece('WN', 3, [7, 1], pygame.image.load('assets/pieces/white/knight.png')),
                Piece('WN', 3, [7, 6], pygame.image.load('assets/pieces/white/knight.png')), 
                Piece('WR', 5, [7, 0], pygame.image.load('assets/pieces/white/rook.png')), 
                Piece('WR', 5, [7, 7], pygame.image.load('assets/pieces/white/rook.png')), 
                
            ])
p1pawns = [Pawn('WP', 1, [6, i], pygame.image.load('assets/pieces/white/pawn.png')) for i in range(8)] 

p1.pieces += p1pawns


p2 = Player(2, [Piece('BK', 99, [0, 4], pygame.image.load('assets/pieces/black/bking.png')),
                Piece('BQ', 9, [0, 3], pygame.image.load('assets/pieces/black/bqueen.png')), 
                Piece('BB', 3, [0, 2], pygame.image.load('assets/pieces/black/bbishop.png')),
                Piece('BB', 3, [0, 5], pygame.image.load('assets/pieces/black/bbishop.png')),
                Piece('BN', 3, [0, 1], pygame.image.load('assets/pieces/black/bknight.png')),
                Piece('BN', 3, [0, 6], pygame.image.load('assets/pieces/black/bknight.png')),
                Piece('BR', 5, [0, 0], pygame.image.load('assets/pieces/black/brook.png')),
                Piece('BR', 5, [0, 7], pygame.image.load('assets/pieces/black/brook.png')), 
                 
            ])
p2pawns = [Pawn('BP', 1, [1, i], pygame.image.load('assets/pieces/black/bpawn.png')) for i in range(8)]

p2.pieces += p2pawns

occupied = [[-1 for i in range(8)] for _ in range(2)] + [[0 for _ in range(8)] for _ in range(4)] + [[1 for _ in range(8)] for _ in range(2)]
        



def update_occupied(occ):
    for piece in p1.pieces + p2.pieces:
        if is_black(piece):
            occ[piece.loc[0]][piece.loc[1]] = -1
        else:
            occ[piece.loc[0]][piece.loc[1]] = 1


update_occupied(occupied)


