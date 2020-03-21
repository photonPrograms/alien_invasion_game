import pygame.font

class Scoreboard:
    """a class to report scoring information"""

    def __init__(self, ai_game):
        """initiliaze scorekeeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for score report
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        # prepare the initial score and level images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """turn the score into a rendered image"""
        score_str = f"Score: {'{:,}'.format(self.stats.score)}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """turn the high score into a renderend image"""
        high_score_str = f"Best: {'{:,}'.format(self.stats.high_score)}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """turn the level into a rendered image"""
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, False, self.text_color, self.settings.bg_color)

        # position the evel below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """draw scores and level to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        """check to see if there is a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
