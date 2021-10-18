import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # initializing the ship
        self.screen = screen
        self.ai_settings = ai_settings
        # loading the ship
        self.image = pygame.image.load(
            "C:/Coding/aw5.pt/py/alien_invasion/spaceship.bmp")
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # starting each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ships center;
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # store a decimal value or the ships horizontal and vertical positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        # update the ships position based on the movement flag center value not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor
        # update rect object
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # drawing the ship at its current location
        self.screen.blit(self.image, self.rect)
