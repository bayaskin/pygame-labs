__author__ = 'bayaskin'

import pygame
import math


# --- Define colors
BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
GREEN     = (  0, 255,   0)
RED       = (255,   0,   0)
BLUE      = (  0,   0, 255)
LILAC     = (300, 100, 100)
YELLOW    = (255, 255,   0)
TURQUOISE = (  0, 255, 215)
BRICK     = (255, 110,   0)
PURPLE    = (120,   0, 255)
BROWN     = (100,  40,   0)
SKY       = (  0, 160, 255)
CERISE    = (155,  30, 115)

pygame.init()

# --- Setting the screen (width, height)
size = (1200, 850)
screen = pygame.display.set_mode(size)

# --- Screen title
pygame.display.set_caption('My picture')

# --- Loop until user closes the screen
done = False

# --- Setting offsets
y_offset = 0
x_offset = 0

# --- Used to manage how fast the screen updates
clock = pygame.time.Clock()


# --- Main programm loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# --- Setting background color
    screen.fill(WHITE)


# --- Drawing code below
    pygame.draw.rect(screen, BLUE, [40, 40, 800, 800])  # --- Drawing border
    pygame.draw.rect(screen, TURQUOISE, [50, 50, 780, 780])  # --- Drawing inner field

    pygame.draw.rect(screen, RED, [170, 140 ,60, 30])
    pygame.draw.rect(screen, RED, [290, 140, 120, 30])
    pygame.draw.rect(screen, YELLOW, [470, 140, 120, 30])
    pygame.draw.rect(screen, YELLOW, [650, 140, 60, 30])
    pygame.draw.rect(screen, SKY, [170, 710, 120, 30])
    pygame.draw.rect(screen, SKY, [350, 710, 60, 30])
    pygame.draw.rect(screen, BROWN, [530, 710, 60, 30])
    pygame.draw.rect(screen, BROWN, [650, 710, 60, 30])

    pygame.draw.rect(screen, BRICK, [140, 170, 30, 120])
    pygame.draw.rect(screen, BRICK, [140, 350, 30, 60])
    pygame.draw.rect(screen, CERISE, [140, 470, 30, 120])
    pygame.draw.rect(screen, CERISE, [140, 650, 30, 60])
    pygame.draw.rect(screen, GREEN, [710, 170, 30, 120])
    pygame.draw.rect(screen, GREEN, [710, 350, 30, 60])
    pygame.draw.rect(screen, PURPLE, [710, 530, 30, 60])
    pygame.draw.rect(screen, PURPLE, [710, 650, 30, 60])

    pygame.draw.line(screen, BLACK, [170, 50], [170, 830], 1)
    pygame.draw.line(screen, BLACK, [710, 50], [710, 830], 1)
    pygame.draw.line(screen, BLACK, [50, 170], [830, 170], 1)
    pygame.draw.line(screen, BLACK, [50, 710], [830, 710], 1)




    for x_offset in range(170, 710, 60):
        pygame.draw.line(screen, BLACK, [x_offset, 50],[x_offset, 170], 1)
        pygame.draw.line(screen, BLACK, [x_offset, 710], [x_offset, 830], 1)

    for y_offset in range(170, 710, 60):
        pygame.draw.line(screen, BLACK, [50, y_offset], [170, y_offset], 1)
        pygame.draw.line(screen, BLACK, [710, y_offset], [830, y_offset], 1)









    pygame.display.flip()


pygame.quit()




