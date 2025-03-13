import pygame
from helpers import screen
from constants import SQUARE_WIDTH, SQUARE_HEIGHT

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.val = 0
        self.width = SQUARE_WIDTH
        self.height = SQUARE_HEIGHT
        self.pic = pygame.transform.scale(pygame.image.load( "Pictures/BLANK_PIC.png"), (self.width, self.height))


