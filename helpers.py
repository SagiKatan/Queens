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


def check_row(matrix, row_idx):
    count = 0
    for val in matrix[row_idx]:
        if val == 1:
            count += 1
    return count <= 1


def check_col(matrix, col_idx):
    count = 0
    for i in range(len(matrix)):
        if matrix[i][col_idx] == 1:
            count += 1
    return count <= 1


def check_frame(matrix, row_idx, col_idx):
    count = 0
    # Check top left
    if row_idx - 1 > -1 and col_idx - 1 > -1:
        if matrix[row_idx - 1][col_idx - 1] == 1:
            count += 1

    # Check top right
    if row_idx - 1 > -1 and col_idx + 1 < len(matrix):
        if matrix[row_idx - 1][col_idx + 1] == 1:
            count += 1
    # Check bottom left
    if row_idx + 1 < len(matrix) and col_idx - 1 > -1:
        if matrix[row_idx + 1][col_idx - 1] == 1:
            count += 1

    # Check bottom right
    if row_idx + 1 < len(matrix) and col_idx + 1 < len(matrix):
        if matrix[row_idx + 1][col_idx + 1] == 1:
            count += 1


    return count == 0

def check_colors(colors):
    for color in colors:
        if colors[color]>1:
            return color

def turnOnAlert_Row(redSquare,row_index):
    for redAlertSquare in redSquare[row_index]:
        redAlertSquare.turnOn()

def turnOffAlert_Row(redSquare,row_index):
    for redAlertSquare in redSquare[row_index]:
        redAlertSquare.turnOff()


def turnOnAlert_Col(redSquare,col_index):
    for i in range(len(redSquare)):
        redSquare[i][col_index].turnOn()

def turnOffAlert_Col(redSquare,col_index):

    for i in range(len(redSquare)):
        redSquare[i][col_index].turnOff()

def turnOnAlert_frame(matrix,row_idx,col_idx,redSquare):
    # Check top left
    if row_idx - 1 > -1 and col_idx - 1 > -1:
        if matrix[row_idx - 1][col_idx - 1] == 1:
            redSquare[row_idx - 1][col_idx - 1].turnOn()

    # Check top right
    if row_idx - 1 > -1 and col_idx + 1 < len(matrix):
        if matrix[row_idx - 1][col_idx + 1] == 1:
            redSquare[row_idx - 1][col_idx + 1].turnOn()
    # Check bottom left
    if row_idx + 1 < len(matrix) and col_idx - 1 > -1:
        if matrix[row_idx + 1][col_idx - 1] == 1:
            redSquare[row_idx + 1][col_idx - 1].turnOn()

    # Check bottom right
    if row_idx + 1 < len(matrix) and col_idx + 1 < len(matrix):
        if matrix[row_idx + 1][col_idx + 1] == 1:
            redSquare[row_idx + 1][col_idx + 1].turnOn()
def turnOffAlert_frame(matrix,row_idx,col_idx,redSquare):
    # Check top left
    if row_idx - 1 > -1 and col_idx - 1 > -1:
        if matrix[row_idx - 1][col_idx - 1] == 1:
            redSquare[row_idx - 1][col_idx - 1].turnOff()

    # Check top right
    if row_idx - 1 > -1 and col_idx + 1 < len(matrix):
        if matrix[row_idx - 1][col_idx + 1] == 1:
            redSquare[row_idx - 1][col_idx + 1].turnOff()

    # Check bottom left
    if row_idx + 1 < len(matrix) and col_idx - 1 > -1:
        if matrix[row_idx + 1][col_idx - 1] == 1:
            redSquare[row_idx + 1][col_idx - 1].turnOff()

    # Check bottom right
    if row_idx + 1 < len(matrix) and col_idx + 1 < len(matrix):
        if matrix[row_idx + 1][col_idx + 1] == 1:
            redSquare[row_idx + 1][col_idx + 1].turnOff()