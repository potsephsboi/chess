from chess_helper import *
from chess_setup import *

WIDTH = 640
HEIGHT = 640
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (115, 147, 179)
FPS = 30

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_window():
    WIN.fill(GREY)
    display_grid(WIN)
    show_pieces()
    pygame.display.update()



def main():


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
                    print(piece.name)
                    # find_squares(piece)
                    

            
        draw_window()
    pygame.quit()


if __name__ == '__main__':
    main()