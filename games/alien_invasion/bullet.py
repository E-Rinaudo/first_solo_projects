#!/usr/bin/env python3

"""
This module defines the 'Bullet' class to manage bullets fired by the ship.

It handles the creation and movement of bullets on the screen.
It initializes bullets at the ship's current position
and updates their vertical position as they move up the screen.
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from settings import Settings


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen: pygame.Surface = ai_game.screen
        self.settings: "Settings" = ai_game.settings
        self.color: tuple[int, int, int] = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect: pygame.Rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y: float = float(self.rect.y)

    def update(self) -> None:  # pylint: disable=W0221
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.difficulty_settings.bullet_speed
        # Update the rect position.
        self.rect.y = int(self.y)

    def draw_bullet(self) -> None:
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
