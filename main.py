from helpers import *
from redCross import RedCross
from Level1 import *

def main():
    pygame.init()
    # define the screen
    pygame.display.set_caption('Queens')
    clock = pygame.time.Clock()
    level_img = pygame.transform.scale(pygame.image.load( "Pictures/level1.png"), (LEVEL_WIDTH, LEVEL_HEIGHT))
    redCross_mat = [[RedCross(SQUARE_POS_X + i*SQUARE_WIDTH, SQUARE_POS_Y + j*SQUARE_HEIGHT) for j in range(7)] for i in range(7)]
    value_matrix = [[0 for _ in range(7)] for _ in range(7)]



    colors = {"purple":0,"orange":0,"blue":0,"green":0,"lime":0,"grey":0,"red":0}
    colors_flag = False
    no_error_flag = True


    pygame.font.init()
    debug_font = pygame.font.SysFont('Arial', 15)
    def value_matrix_print(screen, matrix, pos=(50, 1)):
        x, y = pos
        title_surface = debug_font.render("Values matrix", True, BLACK)
        screen.blit(title_surface, (x, y))
        y += debug_font.get_height()
        for row in matrix:
            row_str = " ".join(str(item) for item in row)
            text_surface = debug_font.render(row_str, True, BLACK)
            screen.blit(text_surface, (x, y))
            y += debug_font.get_height()
    def colors_dict_print(screen,colors,pos = (150,1)):
        x, y = pos
        title_surface = debug_font.render("colors dict", True, BLACK)
        screen.blit(title_surface, (x, y))
        y += debug_font.get_height()
        for key, value in colors.items():
            text_line = f"{key}: {value}"
            text_surface = debug_font.render(text_line, True, BLACK)
            screen.blit(text_surface, (x, y))
            y += debug_font.get_height()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position (x,y) of the mouse press
                pos = event.pos
                # Check legal index - show red alerts on screen if a position is Illegal
                check_event(pos, level_mat, value_matrix, redCross_mat, colors,level_row_index_alert_list,level_col_index_alert_list)





        screen.fill(WHITE)
        screen.blit(level_img, (LEVEL_POS_X, LEVEL_POS_Y))

        # debug section prints
        value_matrix_print(screen, value_matrix)
        colors_dict_print(screen, colors)

        display_matrix(level_mat)
        display_matrix(redCross_mat)
        pygame.display.flip()
    pygame.quit()
    quit()



main()