# Run this file to play chess locally 
# Currently testing for bugs ... 


import threading
import time
import socket

from chess_frontend import *
from chess_setup import *
from chess_backend import *
from socket_helper import SocketPlayer
from client import *


WIDTH = 640
HEIGHT = 640
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY1 = (115, 147, 179)
GREY2 = (119,136,153)
FPS = 30

SERVER_PORT = 5050
SERVER_IP = socket.gethostbyname(socket.gethostname())

def wait_for_opponent(img_id, surface, txt1, txt2):
    surface.fill(GREY2)
    surface.blit(txt1, (50, 100))
    surface.blit(txt2, (50, 140))
    surface.blit(position_imgs[img_id], (70, 250))
    pygame.display.update()


def draw_window(piece, surface):
    surface.fill(GREY1)
    display_grid(surface)
    show_pieces(surface)
    if issubclass(type(piece), Piece):
        show_piece_moves(piece, surface)
    pygame.display.update()



def main(cur_player):
    pygame.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT))

    font = pygame.font.Font('freesansbold.ttf', 24)
    wait_txt1 = font.render('You joined the game', True, BLACK, GREY2)
    wait_txt2 = font.render('Waiting for black to join...', True, BLACK, GREY2)

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
                return

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
        
        if len(SocketPlayer.Players) < 2:
            t2 = time.time_ns()
            if t2 - t1 >= 1000000000:
                t1 = time.time_ns()
                img_id += 1 if img_id < 3 else -3
            wait_for_opponent(img_id, win, wait_txt1, wait_txt2)
        else:
            if cur_player.color == 'W':
                draw_window(temp_piece, win)
            

    

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))
    time.sleep(1)
    cur_sock = None
    
    for p in SocketPlayer.Players:
        if p.socket == client:
            cur_sock = p

    if cur_sock is not None:
        main_thread = threading.Thread(target=main, args=(cur_sock,))
        main_thread.start()
        rev_thread = threading.Thread(target=receive_data, args=(cur_sock,))
    




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