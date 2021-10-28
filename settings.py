class Settings():
    # its a class to store settings for aliens

    def __init__(self):
        # initialize the game's static settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)
        # ship speed
        self.ship_speed_factor = 1
        # bullet setts
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 10
        self.alien_speed_factor = 0.55
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right, -1 left
        self.fleet_direction = 1
        self.ship_limit = 3
        # how quickly the alien point values increase
        self.score_scale = 1.5

        # how quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # increase speed seetings and alien points
        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction of 1 represents right and -1 left
        self.fleet_direction = 1
        self.alien_points = 50
        self.alien_points = int(self.alien_points * self.score_scale)
        # scoring

    def increase_speed(self):
        # increase speed settings
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
