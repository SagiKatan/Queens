import pygame
from helpers import screen
from constants import SQUARE_WIDTH, SQUARE_HEIGHT

class Square:
    def __init__(self, x, y,i,j):
        self.x = x
        self.y = y
        self.row = i
        self.col = j
        self.val = 0
        self.error_val = 0
        self.color = ""
        self.width = SQUARE_WIDTH
        self.height = SQUARE_HEIGHT
        self.pic = pygame.transform.scale(pygame.image.load( "Pictures/BLANK_PIC.png"), (self.width, self.height))
        self.error_pic = pygame.transform.scale(pygame.image.load("Pictures/BLANK_PIC.png"), (self.width, self.height))

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"({self.row},{self.col}) "

    def click(self):
        if self.val != 2:
            self.val += 1
        else:
            self.val = 0

    def turnOn(self):
        self.error_val = 1

    def turnOff(self):
        self.error_val = 0

    def display(self):

        if self.val == 0:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/BLANK_PIC.png"), (self.width, self.height))

        if self.val == 1:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/x_pic.png"), (self.width, self.height))

        if self.val == 2:
            self.pic = pygame.transform.scale(pygame.image.load("Pictures/Crown.png"), (self.width, self.height))

        if self.error_val == 0:
            self.error_pic = pygame.transform.scale(pygame.image.load("Pictures/BLANK_PIC.png"),
                                                    (self.width, self.height))
        if self.error_val == 1:
            self.error_pic = pygame.transform.scale(pygame.image.load("Pictures/red_cross.png"),
                                                    (self.width, self.height))

        screen.blit(self.pic, (self.x, self.y))
        screen.blit(self.error_pic, (self.x, self.y))

    def set_win_crown(self):
        self.pic = pygame.transform.scale(pygame.image.load("Pictures/win_crown.png"), (self.width, self.height))
        screen.blit(self.pic, (self.x, self.y))
