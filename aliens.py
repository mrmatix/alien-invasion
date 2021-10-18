import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # load the image
        self.image = pygame.image.load(
            'C:/Coding/zx/py/alien_invasion/spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()

        # start new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store aliens exact decimal position
        self.x = float(self.rect.x)

    def blitme(self):
        # draw the alien at its current location
        self.screen.blit(self.image, self.rect)
