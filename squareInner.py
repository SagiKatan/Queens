import pygame
from helpers import screen
from square import Square


class InnerSquare(Square):
    def __init__(self, x, y,i,j):
        super().__init__(x, y)
        self.row = i
        self.col = j
        self.color = ""
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
    def __str__(self):
        return f"({self.row},{self.col}) "

    def click(self):
        if self.val!=2:
            self.val+=1
        else:
            self.val = 0

    def display(self):
        if self.val == 0:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/BLANK_PIC.png"), (self.width, self.height))

        if self.val == 1:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/x_pic.png"), (self.width, self.height))

        if self.val == 2:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/Crown.png"), (self.width, self.height))


        screen.blit(self.pic, (self.x, self.y))

