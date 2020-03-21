class GameStats:
    """track statistics for alien invasion"""

    def __init__(self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # start the game in inactive state
        self.game_active = False

    def reset_stats(self):
        """initialize statistics that change during the game"""
        self.ships_left = self.settings.ship_limit
        
        self.score = 0
        self.level = 1
