import pygame


class Settings:
    """A class to store settings for Hungry Fox."""

    def __init__(self):
        """Initialize the game's static settings."""
        self._screen_settings()
        self._farmer_settings()
        self._farmer_bullet_settings()

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        # Initialize the game dynamic settings.
        self._game_settings_flags()
        self.initialize_dynamic_settings()

    def _screen_settings(self):
        """Initialize the screen's settings."""
        self.screen_width = 1280
        self.screen_height = 750
        self.background = pygame.image.load("images/background.bmp")

    def _farmer_settings(self):
        """Initialize the farmer's settings."""
        self.farmer_drop_speed = 10

    def _farmer_bullet_settings(self):
        """Initialize the farmers' bullet settings."""
        self.shooting_frequency = 0.009

    def _game_settings_flags(self):
        """Store the settings flags."""
        self.easy_settings = False
        self.medium_settings = True
        self.hard_settings = False

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self._easy_difficulty_settings()
        self._medium_difficulty_settings()
        self._hard_difficulty_settings()

        # Farmer direction of 1 represents right; -1 represents left.
        self.farmer_direction = 1

    def _easy_difficulty_settings(self):
        """Initialize easy settings."""
        if self.easy_settings:
            self.fox_limit = 5
            self.bullets_allowed = 6
            self.fox_speed = 3.0
            self.bullet_speed = 2.5
            self.farmer_speed = 0.75
            self.farmer_bullets_allowed = 2
            self.farmer_bullet_speed = 1.0
            self.farmer_points = 40
            self.score_scale = 1.5

    def _medium_difficulty_settings(self):
        """Initialize medium settings."""
        if self.medium_settings:
            self.fox_limit = 4
            self.bullets_allowed = 5
            self.fox_speed = 4.0
            self.bullet_speed = 3.5
            self.farmer_speed = 1.0
            self.farmer_bullets_allowed = 3
            self.farmer_bullet_speed = 1.5
            self.farmer_points = 50
            self.score_scale = 1.7

    def _hard_difficulty_settings(self):
        """Initialize hard settings."""
        if self.hard_settings:
            self.fox_limit = 3
            self.bullets_allowed = 4
            self.fox_speed = 5.0
            self.bullet_speed = 4.5
            self.farmer_speed = 1.25
            self.farmer_bullets_allowed = 3
            self.farmer_bullet_speed = 2.0
            self.farmer_points = 60
            self.score_scale = 1.9

    def increase_speed(self):
        """Increase speed settings."""
        self.fox_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.farmer_speed *= self.speedup_scale
        self.farmer_bullet_speed *= self.speedup_scale
        self.farmer_points = int(self.farmer_points * self.score_scale)
