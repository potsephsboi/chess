#   fix small legal_moves count bugs



from chess_frontend import *
from chess_setup import *
from chess_backend import *

WIDTH = 640
HEIGHT = 640
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (115, 147, 179)
FPS = 30

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_window(piece):
    WIN.fill(GREY)
    display_grid(WIN)
    show_pieces()
    if issubclass(type(piece), Piece):
        show_piece_moves(piece)
    pygame.display.update()



def main():
    
    turn = 1
    temp_piece = piece = None
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
                    temp_piece.moves = find_moves(temp_piece, brq_squares(temp_piece, occupied, False, kings_check), occupied, True, kings_check)

                    
                else:    # var piece behaves as coords list        
                    if temp_piece is not None and can_move(temp_piece, piece, kings_check):
                                        # x, y
                        move(temp_piece, piece, turn)   
                        update_occupied(occupied)

                        if turn == 1:
                            for p in p2.pieces:
                                p.legal_moves = 0
                                p.moves = find_moves(p, brq_squares(p, occupied, True, kings_check), occupied, True, kings_check)
                                print(p.name, ': ', p.legal_moves)
                            print('-----------')
                        if turn == -1:
                            for p in p1.pieces:
                                p.legal_moves = 0
                                p.moves = find_moves(p, brq_squares(p, occupied, True, kings_check), occupied, True, kings_check)

                        kings_check[1] = any(p.moves[-1] for p in p1.pieces)
                        kings_check[0] = any(p.moves[-1] for p in p2.pieces)

                        # for row in occupied:
                        #     for p in row:
                        #         print(turn_id[p], end='')
                        #     print()

                        # print('         ---         ')
                        # for p in p2.pieces:
                        #     print(p.name + ': ' + str(p.legal_moves), end=' | ')
                        # print()
                        # print('---------------------')
                        # print('         ---         ')

                        turn *= -1
                        temp_piece = None
                        
                        if stalemate(kings_check):
                            print('Stalemate')
                            run = False

                        cmate = checkmate(kings_check)
                        if cmate is not None:
                            print(f'{cmate} wins')
                            run = False

                        
                        


        draw_window(temp_piece)
        
            

    pygame.quit()


if __name__ == '__main__':
    main()



