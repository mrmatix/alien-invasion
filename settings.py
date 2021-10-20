class Settings():
    # its a class to store settings for aliens

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship speed
        self.ship_speed_factor = 1.5
        # bullet setts
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 10
        self.alien_speed_factor = 0.7
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right, -1 left
        self.fleet_direction = 1
