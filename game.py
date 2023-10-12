import pygame
import sys

#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600

BLUE = (0,0,255)
BROWN = (204,129,43)

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Blue Background with Brown floor')

#Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   # makes background blue
    screen.fill(BLUE)

    rectangle_height = 100
    pygame.draw.rect(screen, BROWN, (0,screen_height-rectangle_height, screen_width, rectangle_height))
    #update display
    pygame.display.flip()

pygame.quit()

