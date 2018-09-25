
import sys

import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800)) #Dimensions of the game window
    pygame.display.set_caption("Alien Invasion")

    #Set the color background
    bg_color = (230, 230, 230)

    while True:
        
        #This is an event loop that responds to user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redraw the screen during each pass through the loop
        screen.fill(bg_color)

        #Make the recently drawn screen visible
        pygame.display.flip()

run_game() 
