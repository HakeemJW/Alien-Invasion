import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen #Inializes ship and sets starting point

        #Load ship image
        self.image = pygame.image.load('images/rocket2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Movement Flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1

        if self.moving_left:
            self.rect.centerx -= 1


   #Draw ship at current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)