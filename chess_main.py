# TODO: in chess_helper in func show piece moves implement rest of moves




from cmath import pi
from chess_helper import *
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
    if piece is not None:
            show_piece_moves(piece)
    pygame.display.update()


def main():

    piece = None
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                piece = select_piece(pygame.mouse.get_pos())
                if piece is not None:
                    piece.moves = find_moves(piece, brq_squares(piece))
                    print(piece.moves)


        draw_window(piece)
        
            

    pygame.quit()


if __name__ == '__main__':
    main()
