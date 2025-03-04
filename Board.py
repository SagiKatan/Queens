import pygame

colors = [
    (255, 0, 0),   # Red
    (0, 255, 0),   # Green
    (0, 0, 255),   # Blue
    (255, 255, 0), # Yellow
    (255, 165, 0), # Orange
    (128, 0, 128), # Purple
    (0, 255, 255), # Light bLue
    (192, 192, 192) # Gray

]
board_colors = [[colors[(r + c) % 8] for c in range(8)] for r in range(8)]
