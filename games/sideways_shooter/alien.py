#!/usr/bin/env python3

"""
This module defines the 'Alien' class to represent individual aliens in the game.

It manages the initialization and movement of alien sprites.
Aliens are placed randomly at the right side of the screen
and move leftward at a set speed.
"""

from typing import TYPE_CHECKING
from random import randint

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from sideways_shooter import SidewaysShooter
    from settings import Settings
    from scoreboard import Scoreboard


class Alien(Sprite):
    """A class to represent a single alien from the fleet."""

    def __init__(self, s_shooter: "SidewaysShooter") -> None:
        """Initialize the alien and set its position."""
        super().__init__()
        self.screen: pygame.Surface = s_shooter.screen
        self.settings: "Settings" = s_shooter.settings
        self.sb: "Scoreboard" = s_shooter.sb

        # Load the image and get its rect.
        self.image: pygame.Surface = pygame.image.load("images/alien.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Set the aline position.
        self._set_alien_position()

        # Store a float for the alien's horizontal position.
        self.x: float = float(self.rect.x)

    def _set_alien_position(self) -> None:
        """Set the alien on the right side of the screen, outside of view."""
        self.rect.left = self.screen.get_rect().right
        # Aliens will be generated randomly and placed at a maximum height
        #   from the bottom and top of the screen.
        alien_top_max: int = self.settings.screen_height - self.rect.height
        self.rect.top = randint(self.sb.scores_images.score_rect.height * 3, alien_top_max)

    def update(self) -> None:  # pylint: disable=W0221
        """Move the alien across the screen."""
        self.x -= self.settings.difficulty_settings.alien_speed
        # Update the rect.
        self.rect.x = int(self.x)
