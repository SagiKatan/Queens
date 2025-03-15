import pygame

from constants import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def mouse_in_button(square, mouse_pos):
    """
    The function get button and mouse press position on screen and return True
    if mouse click on Square
    :param square: Square object
        square on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """
    if square.x + square.width > mouse_pos[0] > square.x and \
            square.y < mouse_pos[1] < square.y + square.height:
        return True


def display_matrix(matrix):
    """
    a function that prints the level squares matrix to screen
    :param matrix: matrix of squares objects
    :return: None. prints the matrix to screen
    """
    for row in matrix:
        for col in row:
            col.display()


def set_colors_in_matrix(matrix, colors):
    """

    :param matrix: matrix of all board squares
    :param colors: dictionary of color: list of positions indexes. of each color in matrix
    :return: None, update all  colors squares in matrix
    """
    for item in colors:
        set_colors(matrix, colors[item], item)


def set_colors(matrix, colors_list, color):
    """

    :param matrix: matrix of all board squares
    :param colors_list: list of all color positions
    :param color: string of color represent the color value of the square
    :return: None, update all specific colored squares in matrix
    """
    for item in colors_list:
        matrix[item[0]][item[1]].set_color(color)


def is_row_legal(value_matrix, row_index):
    count = 0
    for square in value_matrix[row_index]:  # for each cell in the row of row_index
        if square == 1:  # if there is a queen in the cell
            count += 1  # raise the count by 1
    return count <= 1  # return true if there is one or no queens in the row


def is_col_legal(value_matrix, col_index):
    count = 0
    for row_idx in range(len(value_matrix)):  # for each cell in the column of col_index
        if value_matrix[row_idx][col_index] == 1:  # if there is a queen in the cell
            count += 1  # raise the count by 1
    return count <= 1  # return true if there is one or no queens in the column


def is_frame_legal(value_matrix, redCross_matrix, i, j):
    count = 0
    # Check top right cell
    if i - 1 >= 0 and j + 1 < len(redCross_matrix):
        if value_matrix[i - 1][j + 1] == 1:
            count += 1

    # Check top left cell
    if i - 1 >= 0 and j - 1 >= 0:
        if value_matrix[i - 1][j - 1] == 1:
            count += 1

    # Check bottom left cell
    if i + 1 < len(value_matrix) and j - 1 >= 0:
        if value_matrix[i + 1][j - 1] == 1:
            count += 1

    # Check bottom right cell
    if i + 1 < len(value_matrix) and j + 1 < len(value_matrix):
        if value_matrix[i + 1][j + 1] == 1:
            count += 1

    return count == 0
def turn_OFF_board(redCross_mat):
    for row in redCross_mat:
        for square in row:
            square.turnOff()


def turn_ON_row_alert(redCross_mat, row_index):
    for square in redCross_mat[row_index]:  # for each cell in the row
        square.turnOn()  # turn on the alert of more than 1 queen in a row.


def turn_ON_col_alert(redCross_mat, col_index):
    for row_idx in range(len(redCross_mat)):  # for each cell in the column
        redCross_mat[row_idx ][col_index].turnOn()  # turn on the alert of more than 1 queen in a column
def turn_ON_color_alert(redCross_mat, index_list):
    for tuple_of_index in index_list:
        redCross_mat[tuple_of_index[0]][tuple_of_index[1]].turnOn()

def turn_ON_frame_alert(value_matrix, redCross_matrix, i, j):


    # turn on top right cell
    if i - 1 >= 0 and j + 1 < len(redCross_matrix):
        if value_matrix[i - 1][j + 1] == 1:
            redCross_matrix[i - 1][j + 1].turnOn()

    # turn on top left cell
    if i - 1 >= 0 and j - 1 >= 0:
        if value_matrix[i - 1][j - 1] == 1:
            redCross_matrix[i - 1][j - 1].turnOn()

    # turn on bottom left cell
    if i + 1 < len(value_matrix) and j - 1 >= 0:
        if value_matrix[i + 1][j - 1] == 1:
            redCross_matrix[i + 1][j - 1].turnOn()

    # turn on bottom right cell
    if i + 1 < len(value_matrix) and j + 1 < len(value_matrix):
        if value_matrix[i + 1][j + 1] == 1:
            redCross_matrix[i + 1][j + 1].turnOn()


def check_rows(value_matrix, redCross_matrix):
    for i in range(len(value_matrix)):
        if not is_row_legal(value_matrix, i):
            turn_ON_row_alert(redCross_matrix, i)


def check_columns(value_matrix, redCross_matrix):
    for j in range(len(value_matrix)):
        if not is_col_legal(value_matrix, j):
            turn_ON_col_alert(redCross_matrix, j)

def check_frames(value_matrix,redCross_matrix):
    for i in range(len(value_matrix)):
        for j in range(len(value_matrix)):
            if value_matrix[i][j] == 1:
                if not is_frame_legal(value_matrix,redCross_matrix,i,j):
                    turn_ON_frame_alert(value_matrix,redCross_matrix,i,j)



def zeroing_colors(colors_queens):
    for color in colors_queens:
        colors_queens[color] = 0
def count_colors(level_matrix, value_matrix, colors_queens):
    for i in range(len(value_matrix)):
        for j in range(len(value_matrix)):
            if value_matrix[i][j] == 1:
                color = level_matrix[i][j].get_color()
                colors_queens[color]+=1

def check_colors(colors_queens,colors,redCross_matrix):
    for color in colors_queens:
        if colors_queens[color]>1: # need to alert
            turn_ON_color_alert(redCross_matrix,colors[color])




def check_event(pos, innerSquare_matrix, value_matrix, redCross_mat, colors,level_matrix,colors_queens  ):
    for i in range(len(innerSquare_matrix)):
        for j in range(len(innerSquare_matrix)):
            square = innerSquare_matrix[i][j]
            if mouse_in_button(square, pos):
                square.click()
                if square.val == 2:
                    value_matrix[i][j] = 1
                else:
                    value_matrix[i][j] = 0
                turn_OFF_board(redCross_mat)
                zeroing_colors(colors_queens)
                count_colors(level_matrix, value_matrix, colors_queens)
                check_rows(value_matrix, redCross_mat)
                check_columns(value_matrix, redCross_mat)
                check_frames(value_matrix,redCross_mat)
                check_colors(colors_queens, colors, redCross_mat)
