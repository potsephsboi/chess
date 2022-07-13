import pygame
from chess_classes import *

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

name_id = {
    'W': 1, 
    'B': -1, 
    '_': 0

}

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (115, 147, 179)


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


def find_moves(piece, brq):     # bishop rook queen
    
    if piece.name[1] == 'P':
        if is_black(piece):
            if piece.has_moved:
                return [0, 1, 0, 0, 0, 0, 0, 0]
            else:
                return [0, 2, 0, 0, 0, 0, 0, 0]
        else:
            if piece.has_moved:
                return [1, 0, 0, 0, 0, 0, 0, 0]
            else:
                return [2, 0, 0, 0, 0, 0, 0, 0]

    elif piece.name[1] == 'R' or piece.name[1] == 'B' or piece.name[1] == 'Q':
        return brq
    
    elif piece.name[1] == 'K':
        return [1 if brq[i] != 0 else brq[i] for i in range(8)]

    elif piece.name[1] == 'N':
        return knight_squares(piece) # -> int list: [2u_1l, 2u_1r, 1u_2l, 1u_2r, 2d_1l, 2d_1r, 1d_2l, 1d_2r]  



def knight_squares(piece):
    from chess_setup import occupied

    x = piece.loc[1]
    y = piece.loc[0]
    moves = []

    # 2u_1l
    if (y-2 >= 0 and x-1 >= 0) and occupied[y-2][x-1] != name_id[piece.name[0]]:
        moves.append(1)
    else:
        moves.append(0)
    
    # 2u_1r
    if (y-2 >= 0 and x+1 < 8) and occupied[y-2][x+1] != name_id[piece.name[0]]:
        moves.append(1)
    else:
        moves.append(0)

    # 1u_2l
    if (y-1 >= 0 and x-2 >= 0) and occupied[y-1][x-2] != name_id[piece.name[0]]:
        moves.append(1)
    else:
        moves.append(0)

    # 1u_2r
    if (y-1 >= 0 and x+2 < 8) and occupied[y-1][x+2] != name_id[piece.name[0]]:
        moves.append(1)
    else:
        moves.append(0)

    # 2d_1l
    if (y+2 < 8 and x-1 >= 0) and occupied[y+2][x-1] != name_id[piece.name[0]]:
        moves.append(1)
    else:
        moves.append(0)

    # 2d_1r
    if (y+2 < 8 and x+1 < 8) and occupied[y+2][x+1] != name_id[piece.name[0]]:
        moves.append(1)
    else:
        moves.append(0)

    # 1d_2l
    if (y+1 < 8 and x-2 >= 0) and occupied[y+1][x-2] != name_id[piece.name[0]]:
        moves.append(1)
    else:
        moves.append(0)

    # 1d_2r
    if (y+1 < 8 and x+2 < 8) and occupied[y+1][x+2] != name_id[piece.name[0]]:
        moves.append(1)
    else:
        moves.append(0)

    return moves


def brq_squares(piece):
    from chess_setup import occupied
    
    pos = [piece.loc[1], piece.loc[0]]

    # pos[0] == x, pos[1] == y
    def up(pos, n):
        if pos[1]-1 < 0 or occupied[pos[1]-1][pos[0]] == name_id[piece.name[0]]:
            return n
        if occupied[pos[1]-1][pos[0]]*(-1) == name_id[piece.name[0]]:
            return n+1

        n += 1
        return up([pos[0], pos[1]-1], n)
        
            
    def down(pos, n):
        if pos[1]+1 > 7 or occupied[pos[1]+1][pos[0]] == name_id[piece.name[0]]:
            return n
        if occupied[pos[1]+1][pos[0]]*(-1) == name_id[piece.name[0]]:
            return n+1

        n += 1
        return down([pos[0], pos[1]+1], n)

    def left(pos, n):
        if pos[0]-1 < 0 or occupied[pos[1]][pos[0]-1] == name_id[piece.name[0]]:
            return n
        if occupied[pos[1]][pos[0]-1]*(-1) == name_id[piece.name[0]]:
            return n+1

        n += 1
        return left([pos[0]-1, pos[1]], n)

    def right(pos, n):
        if pos[0]+1 > 7 or occupied[pos[1]][pos[0]+1] == name_id[piece.name[0]]:
            return n
        if occupied[pos[1]][pos[0]+1]*(-1) == name_id[piece.name[0]]:
            return n+1

        n += 1
        return right([pos[0]+1, pos[1]], n)

    def upleft(pos, n):
        if (pos[1]-1 < 0 or pos[0]-1 < 0) or occupied[pos[1]-1][pos[0]-1] == name_id[piece.name[0]]:
            return n
        if occupied[pos[1]-1][pos[0]-1]*(-1) == name_id[piece.name[0]]:
            return n+1

        n += 1
        return upleft([pos[0]-1, pos[1]-1], n)
    
    def upright(pos, n):
        if (pos[1]-1 < 0 or pos[0]+1 > 7) or occupied[pos[1]-1][pos[0]+1] == name_id[piece.name[0]]:
            return n
        if occupied[pos[1]-1][pos[0]+1]*(-1) == name_id[piece.name[0]]:
            return n+1

        n += 1
        return upright([pos[0]+1, pos[1]-1], n)

    def downleft(pos, n):
        if (pos[0]-1 < 0 or pos[1]+1 > 7) or occupied[pos[1]+1][pos[0]-1] == name_id[piece.name[0]]:
            return n
        if occupied[pos[1]+1][pos[0]-1]*(-1) == name_id[piece.name[0]]:
            return n+1

        n += 1
        return downleft([pos[0]-1, pos[1]+1], n)

    def downright(pos, n):
        if (pos[0]+1 > 7 or pos[1]+1 > 7) or occupied[pos[1]+1][pos[0]+1] == name_id[piece.name[0]]:
            return n
        if occupied[pos[1]+1][pos[0]+1]*(-1) == name_id[piece.name[0]]:
            return n+1
            
        n += 1
        return downright([pos[0]+1, pos[1]+1], n)


    return [up(pos, 0), down(pos, 0), left(pos, 0), right(pos, 0), 
            upleft(pos, 0), upright(pos, 0), downleft(pos, 0), downright(pos, 0)]



def is_black(piece):
    return piece.name[0] == 'B'