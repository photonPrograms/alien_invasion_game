class Settings:
    """a class to store all settings for Alien Invasion"""

    def __init__(self):
        """initialize the game's static settings"""
        # screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 300 #3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # maximum number of bullets on screen
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

        # how quickly the game speeds up and scores up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """inintialize the game's dynamic settings"""
        # element speeds
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        #scoring
        self.alien_points = 10

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)

