# Snake Game
# Using PyGame
#
# By Shivoy Arora

import pygame
from enum import Enum

""" PyGame show snake and food when playing """
def show(positions, food):
    win.fill((0,0,0))

    # Border
    pygame.draw.rect(win, (42,157,143), (x,y,450,450))
    pygame.draw.rect(win, (0,0,0), (x+2,y+2,446, 446))

class Directions(Enum):
    right = 1
    left = 2
    up = 3
    down = 4

""" Main Function """
if __name__ == "__main__":
    # Pygame setup
    pygame.init()

    win = pygame.display.set_mode((500, 550))
    pygame.display.set_caption("Snake Game")
    titleFont = pygame.font.SysFont(None, 35)

    x = 25
    y = 25
    width = 20

    # initializing when nothing is pressed
    startText = titleFont.render("Press Space to Start", True, (42,157,143))

    win.fill((0,0,0))
    win.blit(startText, (130,260))
    pygame.display.update()

    positions = [[225,225],]
    dir = Directions.right

    execute = False
    run = True
    started = False

    # Running loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    execute = not execute
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    dir = Directions.up
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    dir = Directions.down
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    dir = Directions.left
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    dir = Directions.right

        if execute:
            started = True
            show(positions, (300,300))

            pygame.display.update()
        else:
            if started:
                win.fill((0,0,0))
                resumeText = titleFont.render("Press Space to Resume", True, (42,157,143))
                win.blit(resumeText, (125,260))
                pygame.display.update()