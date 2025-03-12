import pygame
from helpers import screen
from constants import *

def main():
    pygame.init()
    # define the screen
    pygame.display.set_caption('Queens')
    clock = pygame.time.Clock()
    level_img =pygame.image.load( "Pictures/level1.png")
    level_img = pygame.transform.scale(level_img, (LEVEL_WIDTH, LEVEL_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        screen.blit(level_img, (LEVEL_POS_X, LEVEL_POS_Y))

        pygame.display.flip()
    pygame.quit()
    quit()



main()