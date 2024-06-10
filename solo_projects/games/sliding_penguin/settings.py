import pygame


class Settings:
    """A class to store all settings for Sliding Penguin."""

    def __init__(self):
        """Initialize game's static settings."""
        self._screen_settings()
        self._orca_settings()
        self._orca_bullet_settings()

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        # Initialize the game dynamic settings.
        self._game_settings_flags()
        self.initialize_dynamic_settings()
    
    def _screen_settings(self):
        """Initialize the screen's settings."""
        self.screen_width = 1280
        self.screen_height = 750
        self.background = pygame.image.load('images/ocean.bmp')
    
    def _orca_settings(self):
        """Initialize the orca's settings."""
        # How many orcas to hit before leveling up
        #   and maximum number of orcas generated each time.
        self.max_orcas = 10
    
    def _orca_bullet_settings(self):
        """Initialize the orcas' bullet settings."""
        self.shooting_frequency = 0.009
        self.shooting_cooldown = 0

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

        # Count how many orcas get hit to increase speed.
        self.orca_hit = 0
    
    def _easy_difficulty_settings(self):
        """Initialize easy settings."""
        if self.easy_settings:
            self.penguin_limit = 5
            self.bullets_allowed = 6
            self.penguin_speed = 3.0
            self.bullet_speed = 2.5
            self.orca_speed = 0.6
            self.orca_bullets_allowed = 2
            self.orca_bullet_speed = 1.0
            self.orca_frequency = 0.008
            self.orca_points = 40
            self.score_scale = 1.5
        
    def _medium_difficulty_settings(self):
        """Initialize medium settings."""
        if self.medium_settings:
            self.penguin_limit = 4
            self.bullets_allowed = 5
            self.penguin_speed = 4.0
            self.bullet_speed = 3.5
            self.orca_speed = 0.8
            self.orca_bullets_allowed = 3
            self.orca_bullet_speed = 1.5
            self.orca_frequency = 0.009
            self.orca_points = 50
            self.score_scale = 1.7

    def _hard_difficulty_settings(self):
        """Initialize hard settings."""
        if self.hard_settings:
            self.penguin_limit = 3
            self.bullets_allowed = 4
            self.penguin_speed = 5.0
            self.bullet_speed = 4.5
            self.orca_speed = 1.0
            self.orca_bullets_allowed = 3
            self.orca_bullet_speed = 2.0
            self.orca_frequency = 0.01
            self.orca_points = 60
            self.score_scale = 1.9
    
    def increase_speed(self):
        """Increase speed settings."""
        self.penguin_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.orca_speed *= self.speedup_scale
        self.orca_bullet_speed *= self.speedup_scale
        self.orca_frequency *= (self.speedup_scale - 0.05)
        self.orca_points = int(self.orca_points * self.score_scale)