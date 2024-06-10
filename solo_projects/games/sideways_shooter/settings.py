import pygame


class Settings:
    """A class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's static settings."""
        self._screen_settings()
        self._alien_settings()
        self._alien_bullet_settings()

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        
        # Initialize the game dynamic settings.
        self._game_settings_flags()
        self.initialize_dynamic_settings()
       
    def _screen_settings(self):
        """Initialize the screen's settings."""
        self.screen_width = 1280
        self.screen_height = 750    
        self.background = pygame.image.load('images/space.bmp')

    def _alien_settings(self):
        """Initialize the alien's settings."""
        # How many aliens to hit before leveling up
        #   and maximum number of aliens generated each time.
        self.max_aliens = 10

    def _alien_bullet_settings(self):
        """Initialize the aliens' bullet settings."""
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

        # Count how many aliens get hit to increase speed.
        self.alien_hit = 0
    
    def _easy_difficulty_settings(self):
        """Initialize easy settings."""
        if self.easy_settings:
            self.hero_limit = 5
            self.bullets_allowed = 6
            self.hero_speed = 3.0
            self.bullet_speed = 2.5
            self.alien_speed = 0.6
            self.alien_bullets_allowed = 2
            self.alien_bullet_speed = 1.0
            self.alien_frequency = 0.008
            self.alien_points = 40
            self.score_scale = 1.5
        
    def _medium_difficulty_settings(self):
        """Initialize medium settings."""
        if self.medium_settings:
            self.hero_limit = 4
            self.bullets_allowed = 5
            self.hero_speed = 4.0
            self.bullet_speed = 3.5
            self.alien_speed = 0.8
            self.alien_bullets_allowed = 3
            self.alien_bullet_speed = 1.5
            self.alien_frequency = 0.009
            self.alien_points = 50
            self.score_scale = 1.7

    def _hard_difficulty_settings(self):
        """Initialize hard settings."""
        if self.hard_settings:
            self.hero_limit = 3
            self.bullets_allowed = 4
            self.hero_speed = 5.0
            self.bullet_speed = 4.5
            self.alien_speed = 1.0
            self.alien_bullets_allowed = 3
            self.alien_bullet_speed = 2.0
            self.alien_frequency = 0.01
            self.alien_points = 60
            self.score_scale = 1.9
    
    def increase_speed(self):
        """Increase speed settings."""
        self.hero_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_bullet_speed *= self.speedup_scale
        self.alien_frequency *= (self.speedup_scale - 0.05)
        self.alien_points = int(self.alien_points * self.score_scale)