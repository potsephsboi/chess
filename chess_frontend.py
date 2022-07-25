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

turn_id = {
    1: 'W', 
    -1: 'B'
}

DOT_SIZE = 30


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
    

def show_piece_moves(piece):
    from chess_main import WIN
    from chess_setup import av_move
    
    y = piece.loc[0]
    x = piece.loc[1]

    if piece.name[1] in {'K', 'Q', 'P'}:
        for i in range(piece.moves[0]):
            WIN.blit(av_move, (80*x+DOT_SIZE, 80*(y-i-1)+DOT_SIZE)) # up

        for i in range(piece.moves[1]):
            WIN.blit(av_move, (80*x+DOT_SIZE, 80*(y+i+1)+DOT_SIZE)) # down

        for i in range(piece.moves[2]):
            WIN.blit(av_move, (80*(x-i-1)+DOT_SIZE, 80*y+DOT_SIZE)) # left

        for i in range(piece.moves[3]):
            WIN.blit(av_move, (80*(x+i+1)+DOT_SIZE, 80*y+DOT_SIZE)) # right

        for i in range(piece.moves[4]):
            WIN.blit(av_move, (80*(x-i-1)+DOT_SIZE, 80*(y-i-1)+DOT_SIZE)) # upleft

        for i in range(piece.moves[5]):
            WIN.blit(av_move, (80*(x+i+1)+DOT_SIZE, 80*(y-i-1)+DOT_SIZE)) # upright

        for i in range(piece.moves[6]):
            WIN.blit(av_move, (80*(x-i-1)+DOT_SIZE, 80*(y+i+1)+DOT_SIZE)) # downleft

        for i in range(piece.moves[7]):
            WIN.blit(av_move, (80*(x+i+1)+DOT_SIZE, 80*(y+i+1)+DOT_SIZE)) #downright

        # handle castling
        if piece.name[1] == 'K':
            if piece.moves[-2]:
                for i in range(2):
                    WIN.blit(av_move, (80*(x+i+1)+DOT_SIZE, 80*y+DOT_SIZE))
            if piece.moves[-1]:
                for i in range(2):
                    WIN.blit(av_move, (80*(x-i-1)+DOT_SIZE, 80*y+DOT_SIZE))



    elif piece.name[1] == 'B':
        for i in range(piece.moves[4]):
            WIN.blit(av_move, (80*(x-i-1)+DOT_SIZE, 80*(y-i-1)+DOT_SIZE)) # upleft

        for i in range(piece.moves[5]):
            WIN.blit(av_move, (80*(x+i+1)+DOT_SIZE, 80*(y-i-1)+DOT_SIZE)) # upright

        for i in range(piece.moves[6]):
            WIN.blit(av_move, (80*(x-i-1)+DOT_SIZE, 80*(y+i+1)+DOT_SIZE)) # downleft

        for i in range(piece.moves[7]):
            WIN.blit(av_move, (80*(x+i+1)+DOT_SIZE, 80*(y+i+1)+DOT_SIZE)) #downright
   
    
    elif piece.name[1] == 'R':
        for i in range(piece.moves[0]):
            WIN.blit(av_move, (80*x+DOT_SIZE, 80*(y-i-1)+DOT_SIZE)) # up

        for i in range(piece.moves[1]):
            WIN.blit(av_move, (80*x+DOT_SIZE, 80*(y+i+1)+DOT_SIZE)) # down

        for i in range(piece.moves[2]):
            WIN.blit(av_move, (80*(x-i-1)+DOT_SIZE, 80*y+DOT_SIZE)) # left

        for i in range(piece.moves[3]):
            WIN.blit(av_move, (80*(x+i+1)+DOT_SIZE, 80*y+DOT_SIZE)) # right
    
    # knight
    else:
        if piece.moves[0]:
            WIN.blit(av_move, (80*(x-1)+DOT_SIZE, 80*(y-2)+DOT_SIZE))
        if piece.moves[1]:
            WIN.blit(av_move, (80*(x+1)+DOT_SIZE, 80*(y-2)+DOT_SIZE))
        if piece.moves[2]:
            WIN.blit(av_move, (80*(x-2)+DOT_SIZE, 80*(y-1)+DOT_SIZE))
        if piece.moves[3]:
            WIN.blit(av_move, (80*(x+2)+DOT_SIZE, 80*(y-1)+DOT_SIZE))
        if piece.moves[4]:
            WIN.blit(av_move, (80*(x-1)+DOT_SIZE, 80*(y+2)+DOT_SIZE))
        if piece.moves[5]:
            WIN.blit(av_move, (80*(x+1)+DOT_SIZE, 80*(y+2)+DOT_SIZE))
        if piece.moves[6]:
            WIN.blit(av_move, (80*(x-2)+DOT_SIZE, 80*(y+1)+DOT_SIZE))
        if piece.moves[7]:
            WIN.blit(av_move, (80*(x+2)+DOT_SIZE, 80*(y+1)+DOT_SIZE))

        # [2u_1l, 2u_1r, 1u_2l, 1u_2r, 2d_1l, 2d_1r, 1d_2l, 1d_2r] 