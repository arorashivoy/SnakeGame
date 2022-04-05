# Snake Game
# Using PyGame
#
# By Shivoy Arora

import pygame
import random
from enum import Enum


class Snake:
    def __init__(self):
        self.positions = [[22, 22], ]  # Position of the body of the snake
        self.dir = Directions.right
        self.score = 1

    def MoveSnake(self):
        """ Move snake with direction """
        global execute, started, lost

        x = self.positions[0][0]
        y = self.positions[0][1]

        # Moving snake
        if self.dir == Directions.left:
            self.positions.insert(0, [x-1, y])
            self.positions.pop(-1)
        elif self.dir == Directions.right:
            self.positions.insert(0, [x+1, y])
            self.positions.pop(-1)
        elif self.dir == Directions.up:
            self.positions.insert(0, [x, y-1])
            self.positions.pop(-1)
        elif self.dir == Directions.down:
            self.positions.insert(0, [x, y+1])
            self.positions.pop(-1)

        # Checking if snake is in border
        if self.positions[0][0] == 45 or self.positions[0][0] == -1:
            execute = False
            started = False
            lost = True
            self.score = 1
        elif self.positions[0][1] == 45 or self.positions[0][1] == -1:
            execute = False
            started = False
            lost = True
            self.score = 1

        # Check if snake hit his own body
        if self.positions[0] in self.positions[1:]:
            execute = False
            started = False
            lost = True
            self.score = 1

    def IncSize(self):
        """ Increase snake size when food is eaten """

        try:
            x = self.positions[-1][0] + \
                (self.positions[-1][0]-self.positions[-2][0])
            y = self.positions[-1][1] + \
                (self.positions[-1][1]-self.positions[-2][1])

        # if the length of the snake is 1 (i.e. in the start)
        except IndexError:
            if self.dir == Directions.right:
                x = self.positions[-1][0] - 1
                y = self.positions[-1][1]
            elif self.dir == Directions.left:
                x = self.positions[-1][0] + 1
                y = self.positions[-1][1]
            elif self.dir == Directions.up:
                x = self.positions[-1][0]
                y = self.positions[-1][1] + 1
            elif self.dir == Directions.down:
                x = self.positions[-1][0]
                y = self.positions[-1][1] - 1

        self.positions.append([x, y])


def Show(positions, food):
    """ PyGame show snake and food when playing """
    global x, y, width
    global scoreText

    win.fill((0, 0, 0))

    # Border
    pygame.draw.rect(win, (42, 157, 143), (x, y, 450, 450))
    pygame.draw.rect(win, (0, 0, 0), (x+2, y+2, 446, 446))

    # Food
    pygame.draw.rect(win, (233, 196, 106),
                     (x+food[0]*width, y+food[1]*width, width, width))

    # Snake
    for i in positions:
        pygame.draw.rect(win, (231, 111, 81),
                         (x+i[0]*width, y+i[1]*width, width, width))

    # Score
    win.blit(scoreText, (25, 500))


def FoodPos(snake):
    """ Choose random food position """
    x = random.randint(0, 44)
    y = random.randint(0, 44)

    if [x, y] in snake.positions:
        x, y = FoodPos(snake)

    return (x, y)


class Directions(Enum):
    """ Enum of the directions snake can move """
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

    # Setting snake object
    snake = Snake()

    startText = titleFont.render("Press Space to Start", True, (42, 157, 143))
    resumeText = titleFont.render(
        "Press Space to Resume", True, (42, 157, 143))

    # initializing when nothing is pressed
    win.fill((0, 0, 0))
    win.blit(startText, (130, 260))
    pygame.display.update()

    food = FoodPos(snake)

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
                    snake.dir = Directions.up
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.dir = Directions.down
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.dir = Directions.left
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.dir = Directions.right
                elif event.key == pygame.K_q:
                    execute = False
                    run = False

        # When lost
        if lost:
            win.fill((0, 0, 0))
            Show(snake.positions, food)

            win.blit(startText, (115, 250))
            pygame.display.update()

        if execute:
            # if the game has not started yet
            if not started:
                scoreText = titleFont.render(
                    "Score: {}".format(snake.score), True, (42, 157, 143))
            # Reseting new game values after losing
            if lost:
                snake.positions = [[22, 22], ]
                snake.dir = Directions.right
                food = FoodPos(snake)

            started = True
            lost = False

            pygame.time.delay(150)

            snake.MoveSnake()

            # Food is eaten
            if snake.positions[0] == list(food):
                snake.score += 1
                scoreText = titleFont.render(
                    "Score: {}".format(snake.score), True, (42, 157, 143))
                food = FoodPos(snake)
                snake.IncSize()

            Show(snake.positions, food)
            pygame.display.update()

        # When game is paused
        else:
            if started:
                win.fill((0, 0, 0))
                Show(snake.positions, food)

                win.blit(resumeText, (115, 250))
                pygame.display.update()
