#!/usr/bin/env python3

"""
This module defines the 'Settings' class to store and manage game settings.

It includes static and dynamic settings for the game, such screen dimensions,
fox settings, farmer settings, bullet settings, and difficulty levels.
"""

import pygame


class Settings:  # pylint: disable=R0902
    """A class to store settings for Hungry Fox."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        self._screen_settings()
        self._farmer_settings()
        self._farmer_bullet_settings()

        # How quickly the game speeds up.
        self.speedup_scale: float = 1.1

        # Initialize the difficulty-related settings.
        self.difficulty_settings: DifficultySettings = DifficultySettings()
        self.initialize_dynamic_settings()

    def _screen_settings(self) -> None:
        """Initialize the screen's settings."""
        self.screen_width: int = 1280
        self.screen_height: int = 750
        self.background: pygame.Surface = pygame.image.load("images/background.bmp")

    def _farmer_settings(self) -> None:
        """Initialize the farmer's settings."""
        self.farmer_drop_speed: int = 10

    def _farmer_bullet_settings(self) -> None:
        """Initialize the farmers' bullet settings."""
        self.shooting_frequency: float = 0.009

    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change throughout the game."""
        self.difficulty_settings.easy_difficulty_settings()
        self.difficulty_settings.medium_difficulty_settings()
        self.difficulty_settings.hard_difficulty_settings()

        # Farmer direction of 1 represents right; -1 represents left.
        self.farmer_direction: int = 1

    def increase_speed(self) -> None:
        """Increase speed settings."""
        self.difficulty_settings.fox_speed *= self.speedup_scale
        self.difficulty_settings.bullet_speed *= self.speedup_scale
        self.difficulty_settings.farmer_speed *= self.speedup_scale
        self.difficulty_settings.farmer_bullet_speed *= self.speedup_scale
        self.difficulty_settings.farmer_points = int(
            self.difficulty_settings.farmer_points * self.difficulty_settings.score_scale
        )


class DifficultySettings:  # pylint: disable=R0902
    """A class to store all the difficulty-related attributes."""

    def __init__(self) -> None:
        """Initialize difficulties settings."""
        self.fox_limit: int = 0
        self.bullets_allowed: int = 0
        self.fox_speed: float = 0.0
        self.bullet_speed: float = 0.0
        self.farmer_speed: float = 0.0
        self.farmer_bullets_allowed: int = 0
        self.farmer_bullet_speed: float = 0.0
        self.farmer_points: int = 0
        self.score_scale: float = 0.0

        # Initialize the game dynamic settings.
        self._game_settings_flags()

    def _game_settings_flags(self) -> None:
        """Store the settings flags."""
        self.easy_settings: bool = False
        self.medium_settings: bool = True
        self.hard_settings: bool = False

    def easy_difficulty_settings(self) -> None:
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

    def medium_difficulty_settings(self) -> None:
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

    def hard_difficulty_settings(self) -> None:
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
