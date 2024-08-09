"""
This module defines the 'AlienBullet' class to manage bullets fired by aliens.

It handles the creation and movement of bullets on the screen.
Bullets are positioned randomly based on the location of aliens
and move down the screen at a specified speed.
"""

from random import choice

import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    """A class to manage bullets fired from the alien's ship at random."""

    def __init__(self, ai_game):
        """Create a bullet object at the alien's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color

        # Create a bullet rect at (0, 0).
        self.rect = pygame.Rect(
            0, 0, self.settings.alien_bullet_width, self.settings.alien_bullet_height
        )

        # Set bullet position using a random generator.
        alien = choice(ai_game.aliens.sprites())
        self.rect.midbottom = alien.rect.midbottom

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet down the screen."""
        # Update the exact position of the bullet.
        self.y += self.settings.alien_bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_alien_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
