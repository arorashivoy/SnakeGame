# Snake Game
# Using PyGame
#
# By Shivoy Arora

import pygame
import random
from enum import Enum

""" Move snake with direction """
def MoveSnake():
    global positions, dir
    global execute, started, lost
    global score

    x = positions[0][0]
    y = positions[0][1]

    # Moving snake
    if dir == Directions.left:
        pass
        positions.insert(0,[x-1, y])
        positions.pop(-1)
    elif dir == Directions.right:
        positions.insert(0,[x+1, y])
        positions.pop(-1)
    elif dir == Directions.up:
        positions.insert(0,[x, y-1])
        positions.pop(-1)
    elif dir == Directions.down:
        positions.insert(0,[x, y+1])
        positions.pop(-1)

    # Checking if snake is in border 
    if positions[0][0] == 45 or positions[0][0] == -1:
        execute = False
        started = False
        lost = True
        score = 1
    elif positions[0][1] == 45 or positions[0][1] == -1:
        execute = False
        started = False
        lost = True
        score = 1

    # Check if snake hit his own body
    if positions[0] in positions[1:]:
        execute = False
        started = False
        lost = True
        score = 1

""" Increase snake size when food is eaten """
def IncSize():
    global positions, dir
    try:
        x = positions[-1][0] + (positions[-1][0]-positions[-2][0])
        y = positions[-1][1] + (positions[-1][1]-positions[-2][1])

    # if the length of the snake is 1 (i.e. in the start)
    except IndexError:
        if dir == Directions.right:
            x = positions[-1][0] - 1
            y = positions[-1][1]
        elif dir == Directions.left:
            x = positions[-1][0] + 1
            y = positions[-1][1]
        elif dir == Directions.up:
            x = positions[-1][0]
            y = positions[-1][1] + 1
        elif dir == Directions.down:
            x = positions[-1][0]
            y = positions[-1][1] - 1
        

    positions.append([x,y])

""" PyGame show snake and food when playing """
def Show(positions, food):
    global x, y, width
    global scoreText

    win.fill((0,0,0))

    # Border
    pygame.draw.rect(win, (42,157,143), (x,y,450,450))
    pygame.draw.rect(win, (0,0,0), (x+2,y+2,446, 446))

    # Food
    pygame.draw.rect(win, (233, 196, 106), (x+food[0]*width, y+food[1]*width, width, width))

    # Snake
    for i in positions:
        pygame.draw.rect(win, (231, 111, 81), (x+i[0]*width, y+i[1]*width, width, width))
    
    # Score
    win.blit(scoreText, (25,500))

""" Choose random food position """
def FoodPos():
    x = random.randint(0,44)
    y = random.randint(0,44)

    return (x, y)

""" Enum of the directions snake can move """
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
    width = 10

    # initializing when nothing is pressed
    startText = titleFont.render("Press Space to Start", True, (42,157,143))
    resumeText = titleFont.render("Press Space to Resume", True, (42,157,143))

    win.fill((0,0,0))
    win.blit(startText, (130,260))
    pygame.display.update()

    positions = [[22,22],]
    dir = Directions.right
    food = FoodPos()
    score = 1

    execute = False
    run = True
    started = False
    lost = False

    # Running loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            # Checking key presses
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
                elif event.key == pygame.K_q:
                    execute = False
                    run = False
        
        # When lost
        if lost:
            win.fill((0,0,0))
            Show(positions, food)

            win.blit(startText, (115,250))
            pygame.display.update()

        if execute:
            # if the game has not started yet
            if not started:
                scoreText = titleFont.render("Score: {}".format(score), True, (42,157,143))
            # Reseting new game values after losing
            if lost:
                positions = [[22,22],]
                dir = Directions.right
                food = FoodPos()

            started = True
            lost = False

            pygame.time.delay(150)
            
            MoveSnake()

            # Food is eaten
            if positions[0] == list(food):
                score += 1
                scoreText = titleFont.render("Score: {}".format(score), True, (42,157,143))
                food = FoodPos()
                IncSize()

            Show(positions, food)
            pygame.display.update()

        # When game is paused
        else:
            if started:
                win.fill((0,0,0))
                Show(positions, food)

                win.blit(resumeText, (115,250))
                pygame.display.update()
