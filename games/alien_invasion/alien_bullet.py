#!/usr/bin/env python3

"""
This module defines the 'AlienBullet' class to manage bullets fired by aliens.

It handles the creation and movement of bullets on the screen.
Bullets are positioned randomly based on the location of aliens
and move down the screen at a specified speed.
"""

from typing import TYPE_CHECKING
from random import choice

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from settings import Settings


class AlienBullet(Sprite):
    """A class to manage bullets fired from the alien's ship at random."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Create a bullet object at the alien's current position."""
        super().__init__()
        self.screen: pygame.Surface = ai_game.screen
        self.settings: "Settings" = ai_game.settings
        self.color: tuple[int, int, int] = self.settings.alien_bullet_color

        # Create a bullet rect at (0, 0).
        self.rect: pygame.Rect = pygame.Rect(
            0, 0, self.settings.alien_bullet_width, self.settings.alien_bullet_height
        )
        # Set the bullet position.
        self._set_bullet_position(ai_game)

        # Store the bullet's position as a float.
        self.y: float = float(self.rect.y)

    def _set_bullet_position(self, ai_game: "AlienInvasion") -> None:
        """Set the bullet position using a random generator."""
        alien: Sprite = choice(ai_game.aliens.sprites())
        self.rect.midbottom = alien.rect.midbottom  # type: ignore

    def update(self) -> None:  # pylint: disable=W0221
        """Move the bullet down the screen."""
        # Update the exact position of the bullet.
        self.y += self.settings.difficulty_settings.alien_bullet_speed
        # Update the rect position.
        self.rect.y = int(self.y)

    def draw_alien_bullet(self) -> None:
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
