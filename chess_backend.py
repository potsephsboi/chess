import math
from chess_classes import *
import pygame

name_id = {
    'W': 1, 
    'B': -1, 
    '_': 0

}


def is_black(piece):
    return piece.name[0] == 'B'


def select_piece(mouse, turn):
    from chess_setup import p1, p2
    

    if turn == -1:
        for piece in p2.pieces:     
            if piece.loc[1]*80 < mouse[0] < (piece.loc[1]+1)*80 and piece.loc[0]*80 < mouse[1] < (piece.loc[0]+1)*80:
                return piece

    if turn == 1:
        for piece in p1.pieces:     
            if piece.loc[1]*80 < mouse[0] < (piece.loc[1]+1)*80 and piece.loc[0]*80 < mouse[1] < (piece.loc[0]+1)*80:
                return piece

    return list(map(lambda x: x // 80, list(mouse)))


def find_moves(piece, brq):     # bishop rook queen
    from chess_setup import occupied

    if piece.name[1] == 'P':
        if is_black(piece):
            if piece.has_moved:
                
                return [0, 1 if brq[1] >= 1 else 0, 0, 0, 0, 0,

                # left enpassan
                (1 if occupied[piece.loc[0]+1][piece.loc[1]-1] == 1 or
                
                (True if Pawn.enpassan is not None and Pawn.enpassan.loc == [piece.loc[0], piece.loc[1]-1] else False)

                else 0)
                
                if piece.loc[1] > 0 and piece.loc[0] < 7 else 0,

                # right enpassan
                (1 if occupied[piece.loc[0]+1][piece.loc[1]+1] == 1 or
                
                (True if Pawn.enpassan is not None and Pawn.enpassan.loc == [piece.loc[0], piece.loc[1]+1] else False)
                
                else 0)
                
                if piece.loc[1] < 7 and piece.loc[0] < 7 else 0]
            else:
                return [0, 2 if brq[1] >= 2 else brq[1], 0, 0, 0, 0,
                (1 if occupied[piece.loc[0]+1][piece.loc[1]-1] == 1 else 0)
                 if piece.loc[1] > 0 and piece.loc[0] < 7 else 0,
                (1 if occupied[piece.loc[0]+1][piece.loc[1]+1] == 1 else 0) if piece.loc[1] < 7 and piece.loc[0] < 7 else 0]

                 
        else:
            if piece.has_moved:
                return [1 if brq[0] >= 1 else 0, 0, 0, 0,
                # left enpassan
                (1 if occupied[piece.loc[0]-1][piece.loc[1]-1] == -1 or
                
                (True if Pawn.enpassan is not None and Pawn.enpassan.loc == [piece.loc[0], piece.loc[1]-1] else False)

                else 0)
                
                if piece.loc[1] > 0 and piece.loc[0] < 7 else 0,

                # right enpassan
                (1 if occupied[piece.loc[0]-1][piece.loc[1]+1] == -1 or
                
                (True if Pawn.enpassan is not None and Pawn.enpassan.loc == [piece.loc[0], piece.loc[1]+1] else False)
                
                else 0)
                
                if piece.loc[1] < 7 and piece.loc[0] < 7 else 0
                
                ,0, 0]

            else:
                return [2 if brq[0] >= 2 else brq[0], 0, 0, 0,
                (1 if occupied[piece.loc[0]-1][piece.loc[1]-1] == -1 else 0) if piece.loc[1] > 0 and piece.loc[0] > 0 else 0,
                (1 if occupied[piece.loc[0]-1][piece.loc[1]+1] == -1 else 0) if piece.loc[1] < 7 and piece.loc[0] > 0 else 0,
                0, 0]

    elif piece.name[1] == 'R' or piece.name[1] == 'B' or piece.name[1] == 'Q':
        return brq
    
    elif piece.name[1] == 'K':    
        can_castle = check_castling_rights(piece)                                                       
        return [1 if brq[i] != 0 else brq[i] for i in range(8)] + [can_castle[0], can_castle[1]]
                                                                    # ^short        ^long
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
            if piece.name[1] != 'P':
                return n+1
            else:
                return n

        n += 1
        return up([pos[0], pos[1]-1], n)
        
            
    def down(pos, n):
        if pos[1]+1 > 7 or occupied[pos[1]+1][pos[0]] == name_id[piece.name[0]]:
            return n
        if occupied[pos[1]+1][pos[0]]*(-1) == name_id[piece.name[0]]:
            if piece.name[1] != 'P':
                return n+1
            else:
                return n

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


def can_move(piece, coords):
    x, y = piece.loc[1], piece.loc[0]
    dx = coords[0] - x  
    dy = coords[1] - y
    dist = math.sqrt(dx**2+dy**2)

    # piece is knight
    if dist == math.sqrt(5) and piece.name[1] == 'N':    
        return True

    if not (abs(dy) == abs(dx) or (dx == 0 or dy == 0)):
        return False

    if piece.name[1] != 'N':
        # dx == 0 or dy == 0
        if piece.name[1] in {'R', 'Q', 'P', 'K'}:
            if piece.name[1] == 'K':
                                        # short ---- long

                if (abs(dx) == 2 and piece.moves[-2]) or (abs(dx) == 2 and piece.moves[-1]):
                    return True
                

            if dy < 0 and dx == 0:  # up
                return True if piece.moves[0] >= abs(dy) else False
            if dy > 0 and dx == 0:  # down
                return True if piece.moves[1] >= abs(dy) else False
            if dy == 0 and dx < 0:  # left
                return True if piece.moves[2] >= abs(dx) else False
            if dy == 0 and dx > 0:  # right
                return True if piece.moves[3] >= abs(dx) else False

        # dy == dx
        if piece.name[1] in {'B', 'Q', 'P', 'K'}:    
            if dy < 0 and dx < 0:  # upleft
                return True if piece.moves[4] >= abs(dy) else False

            if dy < 0 and dx > 0:  # upright
                return True if piece.moves[5] >= abs(dy) else False

            if dy > 0 and dx < 0:  # downleft
                return True if piece.moves[6] >= abs(dy) else False

            if dy > 0 and dx > 0:  # downright
                return True if piece.moves[7] >= abs(dy) else False

def check_castling_rights(king):
    from chess_setup import occupied

    if king.has_moved:
        return [0, 0]
    
    kingx = king.loc[1]
    kingy = king.loc[0]
    castle = [0, 0]

    
    # short
    if occupied[kingy][kingx+1] == 0 and occupied[kingy][kingx+2] == 0:
        for r in Rook.brooks + Rook.wrooks:
            if not r.has_moved and [r.loc[0], r.loc[1]] == [kingy, kingx+3]:
                castle[0] = 1
            
    # long
    if occupied[kingy][kingx-1] == 0 and occupied[kingy][kingx-2] == 0 and occupied[kingy][kingx-3] == 0:
        for r in Rook.brooks + Rook.wrooks:
            if not r.has_moved and [r.loc[0], r.loc[1]] == [kingy, kingx-4]:
                castle[1] = 1

    return castle
   
                # x, y
def move(piece, coords, turn):
    from chess_setup import occupied

    temp_enpassan = Pawn.enpassan
    Pawn.enpassan = None
    
    if type(piece) in {Pawn, King, Rook}:
        if type(piece) == Pawn and not piece.has_moved and abs(coords[1] - piece.loc[0]) == 2:
            Pawn.enpassan = piece
            
        piece.has_moved = True
    
    # castling
    if type(piece) == King:
        # short
        if coords[0] - piece.loc[1] == 2:
            for r in Rook.wrooks + Rook.brooks:
                if r.loc == [piece.loc[0], piece.loc[1]+3]:
                    move(r, [piece.loc[1]+1, piece.loc[0]], turn)
                    break

        # long
        elif coords[0] - piece.loc[1] == -2:
            for r in Rook.wrooks + Rook.brooks:
                if r.loc == [piece.loc[0], piece.loc[1]-4]:
                    move(r, [piece.loc[1]-1, piece.loc[0]], turn)
                    break


    if occupied[coords[1]][coords[0]] == turn * -1:
        remove_piece(coords, turn)
    
    if type(piece) == Pawn:
        if temp_enpassan is not None and coords[0] == temp_enpassan.loc[1] and abs(coords[1] - temp_enpassan.loc[0]) == 1:
            occupied[temp_enpassan.loc[0]][temp_enpassan.loc[1]] = 0
            remove_piece([temp_enpassan.loc[1], temp_enpassan.loc[0]], turn)
            

    occupied[piece.loc[0]][piece.loc[1]] = 0
    piece.loc[0], piece.loc[1] = coords[1], coords[0]
    
    # queening
    if not is_black(piece) and type(piece) is Pawn:
        if piece.loc[0] == 0:
            make_queen(piece, 1)
    if is_black(piece) and type(piece) is Pawn:
        if piece.loc[0] == 7:
            make_queen(piece, -1)


def remove_piece(piece_coords, turn):
    from chess_setup import p1, p2

    if turn == 1:
        for p in p2.pieces:
            if [p.loc[1], p.loc[0]] == [piece_coords[0], piece_coords[1]]:
                p2.pieces.remove(p)
    elif turn == -1:
        for p in p1.pieces:
            if [p.loc[1], p.loc[0]] == [piece_coords[0], piece_coords[1]]:
                p1.pieces.remove(p)


def make_queen(pawn, turn):
    from chess_setup import p1, p2

    if turn == 1:
        p1.pieces.remove(pawn)
        p1.pieces.append(Piece('WQ', 9, [pawn.loc[0], pawn.loc[1]], pygame.image.load('assets/pieces/white/queen.png')))
    
    elif turn == -1:
        p2.pieces.remove(pawn)
        p2.pieces.append(Piece('BQ', 9, [pawn.loc[0], pawn.loc[1]], pygame.image.load('assets/pieces/black/bqueen.png')))


