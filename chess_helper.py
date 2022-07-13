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
        
            
def available_moves(piece):
    print(piece.name)
    sqrs = find_squares(piece)     # returns [n(u), n(d), n(l), n(r), n(ul), n(ur), n(dl), n(dr)]
    print(sqrs)                    # where n(x)  == num of available squares in x direction
    
    return find_moves(piece, sqrs)


    
        

def find_moves(piece, sqrs):
    from chess_setup import occupied

    y = piece.loc[0]
    x = piece.loc[1]
    moves = [0 for _ in range(8)]
    if is_black(piece):
        if piece.name[1] == 'P':    # pawn
            if occupied[y+1][x+1] == 'W' and (x < 7 and y < 7):    # downright
                moves[7] += 1
            if occupied[y+1][x-1] == 'W' and (x > 0 and y < 7):    # downleft
                moves[6] += 1  
            
            if piece.has_moved:
                moves[1] += 1
            else:
                moves[1] += 2
    
    else:
        if piece.name[1] == 'P':    # pawn
            if occupied[y-1][x+1] == 'B' and (x < 7 and y > 0):    # upright
                moves[5] += 1
            if occupied[y-1][x-1] == 'B' and (x > 0 and y > 0):    # upleft
                moves[4] += 1  
            
            if piece.has_moved:
                moves[0] += 1
            else:
                moves[0] += 2

    # add functionality for rooks

def find_squares(piece):
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