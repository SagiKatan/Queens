
from squareInner import InnerSquare
from helpers import *


level_mat = [[InnerSquare(SQUARE_POS_X + i * SQUARE_WIDTH, SQUARE_POS_Y + j * SQUARE_HEIGHT,i,j) for i in range(7)] for j in
             range(7)]

purple_index_list = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                     (6, 0), (1, 1), (1, 3), (1, 6), (4, 1), (5, 1), (6, 1), (4, 2), (6, 2)]
orange_index_list = [(1, 2), (2, 2), (2, 1), (3, 1)]
blue_index_list = [(2, 6), (3, 6), (4, 6), (5, 6), (1, 5), (2, 5), (4, 5), (1, 4)]
green_index_list = [(2, 3), (2, 4), (3, 4), (3, 5)]
lime_index_list = [(5, 4), (5, 5), (6, 5), (6, 6)]
grey_index_list = [(3, 2), (3, 3), (4, 3), (4, 4)]
red_index_list = [(5, 2), (5, 3), (6, 3), (6, 4)]


colors = {"purple": purple_index_list, "orange": orange_index_list, "blue": blue_index_list,
          "green": green_index_list, "lime": lime_index_list, "grey": grey_index_list, "red": red_index_list}
colors_queens = {"purple": 0, "orange": 0, "blue": 0, "green": 0, "lime": 0, "grey": 0, "red": 0}
def update_colors(colors,level_mat):
    for key in colors:
            for item in colors[key]:
                level_mat[item[0]][item[1]].set_color(key)



