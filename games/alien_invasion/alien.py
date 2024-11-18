#!/usr/bin/env python3

"""
This module defines the 'Alien' class to represent individual aliens in the game.
It manages the initialization and movement of alien sprites.
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from settings import Settings


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen: pygame.Surface = ai_game.screen
        self.settings: "Settings" = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image: pygame.Surface = pygame.image.load("images/alien.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x: float = float(self.rect.x)

    def check_edges(self) -> bool:
        """Return True if an alien is at the edge of screen."""
        screen_rect: pygame.Rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self) -> None:  # pylint: disable=W0221
        """Move the alien to the right or left."""
        self.x += self.settings.difficulty_settings.alien_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)
