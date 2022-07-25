# TODO: implement castling, en croissant, checkmate, stalemate


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
    clock = pygame.time.Clock()
    run = True
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
                    piece.moves = find_moves(piece, brq_squares(piece))

                else:    # var piece behaves as coords list        
                    if temp_piece is not None and can_move(temp_piece, piece):
                                        # x, y
                        move(temp_piece, piece, turn)
                        update_occupied(occupied)

                        for p in Piece.pieces:
                            p.moves = find_moves(p, brq_squares(p))
                        
                        turn *= -1
                        temp_piece = None
                        
        draw_window(temp_piece)
        
            

    pygame.quit()


if __name__ == '__main__':
    main()
