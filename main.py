from helpers import *
from redCross import RedCross
from Level1 import level_mat,colors_queens, colors, update_colors

def main():
    pygame.init()
    # define the screen
    pygame.display.set_caption('Queens')
    clock = pygame.time.Clock()
    win_image = pygame.transform.scale(pygame.image.load( "Pictures/you_win.jpg"), (YOU_WIN_WIDTH, YOU_WIN_HEIGHT))

    level_img = pygame.transform.scale(pygame.image.load( "Pictures/level1.png"), (LEVEL_WIDTH, LEVEL_HEIGHT))
    redCross_mat = [[RedCross(SQUARE_POS_X + j * SQUARE_WIDTH, SQUARE_POS_Y + i * SQUARE_HEIGHT) for j in range(7)] for i in range(7)]
    value_matrix = [[0 for j in range(7)] for i in range(7)]

    all_queens_flag = False # a flag for knowing if player finished place all queens.
    error_flag = False # a flag for knowing if there is an alert on board
    # game will be finished if all_queens_flag is True and error_flag is False
    update_colors(colors, level_mat)




    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not all_queens_flag  or error_flag :
                    # Get the position (x,y) of the mouse press
                    pos = event.pos

                    check_event(pos, level_mat, value_matrix) # update the board with the new information

        turn_OFF_board(redCross_mat) # turn off all the red alerts so it could recheck
        zeroing_colors(colors_queens) # zero all the colors count per queen
        count_colors(level_mat, value_matrix, colors_queens) # count for each color, how many queens there are for each color
        row_flag = check_rows(value_matrix, redCross_mat) # Check if there is a one or more rows with wrong placement. If there is at least 1 row - row_flag is True
        column_flag = check_columns(value_matrix, redCross_mat)# Check if there is a one or more columns with wrong placement. If there is at least 1 column - column_flag is True
        frame_flag = check_frames(value_matrix, redCross_mat) # Check for each queen if there is a queen in its frame, if there is at least 1 queen with wrong frame - frame_flag is True.
        color_flag = check_colors(colors_queens, colors, redCross_mat) # Check if there is more than 1 queen in the same color. if there is - color flag is True
        error_flag =  row_flag or column_flag or frame_flag or color_flag
        all_queens_flag = check_all_colors_queens(colors_queens)



        screen.fill(WHITE)
        screen.blit(level_img, (LEVEL_POS_X, LEVEL_POS_Y))

        display_matrix(level_mat)
        display_matrix(redCross_mat)
        if all_queens_flag and not error_flag:
            update_victory_image(value_matrix, level_mat)
            screen.blit(win_image, (YOU_WIN_POS_X, YOU_WIN_POS_Y))

        pygame.display.flip()
    pygame.quit()
    quit()



main()