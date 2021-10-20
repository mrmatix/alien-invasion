import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from aliens import Alien
import game_functions as gf


def run_game():
    # initializing game and creating a screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # making the ship
    ship = Ship(ai_settings, screen)
    # making a group to store the bullets
    bullets = Group()

    alien = Alien(ai_settings, screen)
    aliens = Group()

    # create the fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Starting the main loop for the game
    while True:
        # game_funcitons.py
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
