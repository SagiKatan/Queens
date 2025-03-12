import pygame
from helpers import screen
from square import Square


class SquareInner(Square):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = ""
    def set_color(self, color):
        self.color = color

    def display(self):
        if self.val == 0:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/BLANK_PIC.png"), (self.width, self.height))

        if self.val == 1:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/x_pic.png"), (self.width, self.height))

        if self.val == 2:
            self.pic = pygame.transform.scale(self.pic, (self.width, self.height))
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/Crown.png"), (self.width, self.height))


        screen.blit(self.pic, (self.x, self.y))

