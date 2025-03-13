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






    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position (x,y) of the mouse press
                pos = event.pos
                for i in range(len(level_mat)):
                    for j in range(len(level_mat)):
                        square = level_mat[i][j]
                        if mouse_in_button(square, pos):
                            square.click()
                            if square.val == 2:
                                value_matrix[i][j] = 1
                                colors[square.color]+=1
                                if not check_row(value_matrix, i):
                                    turnOnAlert_Row(redCross_mat,i)
                                if not check_row(value_matrix, j):
                                    turnOnAlert_Col(redCross_mat, j)
                                if not check_frame(value_matrix, i, j):
                                    pass
                            else:
                                value_matrix[i][j] = 0
                                colors[square.color] -= 1
                                if  check_row(value_matrix, i):
                                    turnOffAlert_Row(redCross_mat,i)
                                if check_row(value_matrix, j):
                                    turnOffAlert_Col(redCross_mat, j)

                                if check_frame(value_matrix, i, j):
                                    pass




        screen.fill(WHITE)
        screen.blit(level_img, (LEVEL_POS_X, LEVEL_POS_Y))

        display_matrix(level_mat)
        display_matrix(redCross_mat)
        pygame.display.flip()
    pygame.quit()
    quit()



main()