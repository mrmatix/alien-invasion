import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from aliens import Alien
from game_stats import GameStats
import game_functions as gf


def run_game():
    # initializing game and creating a screen object
    pygame.init()
    ai_settings = Settings()

    stats = GameStats(ai_settings)

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
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == "__main__":
    run_game()
