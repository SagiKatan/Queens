import pygame
from helpers import screen
from constants import SQUARE_WIDTH, SQUARE_HEIGHT
from square import Square

class RedCross(Square):
    def __init__(self, x, y):
        super().__init__(x,y)


    def display(self):
        if self.val == 0:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/BLANK_PIC.png"), (self.width, self.height))

        if self.val == 1:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/red_cross.png"), (self.width, self.height))

        screen.blit(self.pic, (self.x, self.y))

