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



def is_row_legal(value_matrix,row_index):
    count = 0
    for square in value_matrix[row_index]: # for each cell in the row of row_index
        if square == 1: # if there is a queen in the cell
            count+=1 # raise the count by 1
    return count<=1# return true if there is one or no queens in the row



def turn_ON_row_alert(redCross_mat,row_index):
    for square in redCross_mat[row_index]: # for each cell in the row
        square.turnOn() # turn on the alert of more than 1 queen in a row.

def turn_OFF_row_alert(redCross_mat,row_index,level_col_index_alert_list):

    row = redCross_mat[row_index] # the row that needs to turn off
    for j in range(len(row)): # run over each index in the row
        if j not in level_col_index_alert_list: # if the index is in another alert, don't turn it off
            if row[j].get_value() == 1: # turn off only if the box is on
                row[j].turnOff()


def check_row_function(value_matrix,row_index,redCross_mat,level_row_index_alert_list,level_col_index_alert_list):
    if not is_row_legal(value_matrix,row_index): # if row is illegal
        turn_ON_row_alert(redCross_mat, row_index) # turn on the alert of the row
        level_row_index_alert_list.append(row_index) # update the indicated row list with row index as an illegal row.
    else:
        if row_index in level_row_index_alert_list:
            level_row_index_alert_list.remove(row_index)  # remove the indicated row from the list. and mark the row index as a legal row.
        turn_OFF_row_alert(redCross_mat, row_index, level_col_index_alert_list) # if there is a box needed to be off


def is_col_legal(value_matrix,col_index):
    count = 0
    for row_idx in range(len(value_matrix)): # for each cell in the column of col_index
        if value_matrix[row_idx][col_index] == 1: # if there is a queen in the cell
            count+=1 # raise the count by 1
    return count<=1 # return true if there is one or no queens in the column

def turn_ON_col_alert(redCross_mat,col_index):
    for row_idx in range(len(redCross_mat)): # for each cell in the column
        redCross_mat[row_idx][col_index].turnOn() # turn on the alert of more than 1 queen in a column

def turn_OFF_col_alert(redCross_mat,col_index,level_row_index_alert_list):
    for row_idx in range(len(redCross_mat)): # for each cell in the column
        if row_idx not in level_row_index_alert_list: # if the cell is not in another alert zone
            if redCross_mat[row_idx][col_index].get_value() == 1: # if there is an alert
                redCross_mat[row_idx][col_index].turnOff() # turn it off
def check_col_function(value_matrix,col_index,redCross_mat,level_row_index_alert_list,level_col_index_alert_list):
    if not is_col_legal(value_matrix,col_index): # if column is  illegal
        turn_ON_col_alert(redCross_mat,col_index)
        level_col_index_alert_list.append(col_index)
    else:
        if col_index in level_col_index_alert_list:
            level_col_index_alert_list.remove(col_index)
        turn_OFF_col_alert(redCross_mat,col_index,level_row_index_alert_list)






def check_event(pos,innerSquare_matrix,value_matrix,redCross_mat,colors,level_row_index_alert_list,level_col_index_alert_list):
    for i in range(len(innerSquare_matrix)):
        for j in range(len(innerSquare_matrix)):
            square = innerSquare_matrix[i][j]
            if mouse_in_button(square, pos):
                square.click()
                if square.val == 2:
                    value_matrix[i][j] = 1
                else:
                    value_matrix[i][j] = 0

                check_row_function(value_matrix, i, redCross_mat, level_row_index_alert_list,
                                   level_col_index_alert_list)
                check_col_function(value_matrix,j,redCross_mat,level_row_index_alert_list,level_col_index_alert_list)




