import pygame
import sys
from pygame.locals import *

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((340, 340))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("tick tac toe")

# Creating Lines and Shapes
one = pygame.draw.rect(DISPLAYSURF, WHITE, (10, 10, 100, 100))
two = pygame.draw.rect(DISPLAYSURF, WHITE, (120, 10, 100, 100))
three = pygame.draw.rect(DISPLAYSURF, WHITE, (230, 10, 100, 100))

four = pygame.draw.rect(DISPLAYSURF, WHITE, (10, 120, 100, 100))
five = pygame.draw.rect(DISPLAYSURF, WHITE, (120, 120, 100, 100))
six = pygame.draw.rect(DISPLAYSURF, WHITE, (230, 120, 100, 100))

seven = pygame.draw.rect(DISPLAYSURF, WHITE, (10, 230, 100, 100))
eight = pygame.draw.rect(DISPLAYSURF, WHITE, (120, 230, 100, 100))
nine = pygame.draw.rect(DISPLAYSURF, WHITE, (230, 230, 100, 100))

one_open = True
two_open = True
three_open = True
four_open = True
five_open = True
six_open = True
seven_open = True
eight_open = True
nine_open = True

is_rectangle = True

# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if K_SPACE:
            one = pygame.draw.rect(DISPLAYSURF, WHITE, (10, 10, 100, 100))
            two = pygame.draw.rect(DISPLAYSURF, WHITE, (120, 10, 100, 100))
            three = pygame.draw.rect(DISPLAYSURF, WHITE, (230, 10, 100, 100))
            four = pygame.draw.rect(DISPLAYSURF, WHITE, (10, 120, 100, 100))
            five = pygame.draw.rect(DISPLAYSURF, WHITE, (120, 120, 100, 100))
            six = pygame.draw.rect(DISPLAYSURF, WHITE, (230, 120, 100, 100))
            seven = pygame.draw.rect(DISPLAYSURF, WHITE, (10, 230, 100, 100))
            eight = pygame.draw.rect(DISPLAYSURF, WHITE, (120, 230, 100, 100))
            nine = pygame.draw.rect(DISPLAYSURF, WHITE, (230, 230, 100, 100))

            one_open = True
            two_open = True
            three_open = True
            four_open = True
            five_open = True
            six_open = True
            seven_open = True
            eight_open = True
            nine_open = True

            is_rectangle = True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if one.collidepoint(pos) and one_open:
                one_open = False
                if is_rectangle:
                    pygame.draw.rect(DISPLAYSURF, RED, (20, 20, 80, 80))
                    is_rectangle = False
                else:
                    pygame.draw.circle(DISPLAYSURF, GREEN, (60, 60), 40)
                    is_rectangle = True
            if two.collidepoint(pos) and two_open:
                two_open = False
                if is_rectangle:
                    pygame.draw.rect(DISPLAYSURF, RED, (130, 20, 80, 80))
                    is_rectangle = False
                else:
                    pygame.draw.circle(DISPLAYSURF, GREEN, (170, 60), 40)
                    is_rectangle = True
            if three.collidepoint(pos) and three_open:
                three_open = False
                if is_rectangle:
                    pygame.draw.rect(DISPLAYSURF, RED, (240, 20, 80, 80))
                    is_rectangle = False
                else:
                    pygame.draw.circle(DISPLAYSURF, GREEN, (280, 60), 40)
                    is_rectangle = True

            if four.collidepoint(pos) and four_open:
                four_open = False
                if is_rectangle:
                    pygame.draw.rect(DISPLAYSURF, RED, (20, 130, 80, 80))
                    is_rectangle = False
                else:
                    pygame.draw.circle(DISPLAYSURF, GREEN, (60, 170), 40)
                    is_rectangle = True
            if five.collidepoint(pos) and five_open:
                five_open = False
                if is_rectangle:
                    pygame.draw.rect(DISPLAYSURF, RED, (130, 130, 80, 80))
                    is_rectangle = False
                else:
                    pygame.draw.circle(DISPLAYSURF, GREEN, (170, 170), 40)
                    is_rectangle = True
            if six.collidepoint(pos) and six_open:
                six_open = False
                if is_rectangle:
                    pygame.draw.rect(DISPLAYSURF, RED, (240, 130, 80, 80))
                    is_rectangle = False
                else:
                    pygame.draw.circle(DISPLAYSURF, GREEN, (280, 170), 40)
                    is_rectangle = True

            if seven.collidepoint(pos) and seven_open:
                seven_open = False
                if is_rectangle:
                    pygame.draw.rect(DISPLAYSURF, RED, (20, 240, 80, 80))
                    is_rectangle = False
                else:
                    pygame.draw.circle(DISPLAYSURF, GREEN, (60, 280), 40)
                    is_rectangle = True
            if eight.collidepoint(pos) and eight_open:
                eight_open = False
                if is_rectangle:
                    pygame.draw.rect(DISPLAYSURF, RED, (130, 240, 80, 80))
                    is_rectangle = False
                else:
                    pygame.draw.circle(DISPLAYSURF, GREEN, (170, 280), 40)
                    is_rectangle = True

            if nine.collidepoint(pos) and nine_open:
                nine_open = False
                if is_rectangle:
                    pygame.draw.rect(DISPLAYSURF, RED, (240, 240, 80, 80))
                    is_rectangle = False
                else:
                    pygame.draw.circle(DISPLAYSURF, GREEN, (280, 280), 40)
                    is_rectangle = True

    FramePerSec.tick(FPS)
