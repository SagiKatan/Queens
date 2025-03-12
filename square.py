import pygame
from helpers import screen


class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.val = 0 # 0 is blank, -1 is X 1 is queen
        self.pic = "Pictures/BLANK_PIC.png"
    def display(self):
        screen.blit(self.pic,(self.x,self.y))
