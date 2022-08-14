# Run this file to play chess locally 
# Currently testing for bugs ... 

import time


from chess_frontend import *
from chess_setup import *
from chess_backend import *




WIDTH = 640
HEIGHT = 640
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY1 = (115, 147, 179)
GREY2 = (119,136,153)
FPS = 30

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font('freesansbold.ttf', 24)
wait_text1 = font.render('You joined the game', True, BLACK, GREY2)
wait_text2 = font.render('Waiting for black to join...', True, BLACK, GREY2)

def wait_for_opponent(img_id):
    WIN.fill(GREY2)
    WIN.blit(wait_text1, (50, 100))
    WIN.blit(wait_text2, (50, 140))
    WIN.blit(position_imgs[img_id], (70, 250))
    pygame.display.update()


def draw_window(piece):
    WIN.fill(GREY1)
    display_grid(WIN)
    show_pieces()
    if issubclass(type(piece), Piece):
        show_piece_moves(piece)
    pygame.display.update()



def main():

    turn = 1
    temp_piece = piece = None
    t1 = time.time_ns()
    img_id = 0
    kings_check = [False, False]

    clock = pygame.time.Clock()
    run = True
    for p in Piece.pieces:
        p.moves = find_moves(p, brq_squares(p, occupied, False, kings_check), occupied, False, kings_check)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                piece = select_piece(pygame.mouse.get_pos(), turn=turn) # returns either a piece object or matrix coordinates
                
                if issubclass(type(piece), Piece):  # var piece behaves as a Piece instance
                    if piece.name[0] != turn_id[turn]:
                        continue 
                    temp_piece = piece
                else:    # var piece behaves as coords list        
                    if temp_piece is not None and can_move(temp_piece, piece, kings_check):
                        
                                        # x, y
                        move(temp_piece, piece, turn)   
                        update_occupied(occupied)
                        temp_piece.moves = find_moves(temp_piece, brq_squares(temp_piece, occupied, False, kings_check), occupied, True, kings_check)
                        kings_check[1] = any(p.moves[-1] for p in p1.pieces)
                        kings_check[0] = any(p.moves[-1] for p in p2.pieces)

                        if turn == 1:
                            for p in p2.pieces:
                                p.legal_moves = 0
                                p.moves = find_moves(p, brq_squares(p, occupied, True, kings_check), occupied, True, kings_check)

                        if turn == -1:
                            for p in p1.pieces:
                                p.legal_moves = 0
                                p.moves = find_moves(p, brq_squares(p, occupied, True, kings_check), occupied, True, kings_check)

                        turn *= -1
                        temp_piece = None
                        
                        if stalemate(kings_check):
                            print('Stalemate')
                            run = False

                        cmate = checkmate(kings_check)
                        if cmate is not None:
                            print(f'{cmate} wins')
                            run = False
        if 1:
            t2 = time.time_ns()
            if t2 - t1 >= 1000000000:
                t1 = time.time_ns()
                img_id += 1 if img_id < 3 else -3
            
            wait_for_opponent(img_id)
        else:
            draw_window(temp_piece)
        
            

    pygame.quit()







# for row in occupied:
#     for p in row:
#         print(turn_id[p], end='')
#     print()

# print('         ---         ')
# for p in p2.pieces:
#     print(p.name + ': ' + str(p.legal_moves), p.loc, end=' | ')
# print(kings_check)
# print('---------------------')
# print('         ---         ')