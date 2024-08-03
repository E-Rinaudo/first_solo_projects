"""
This module defines the 'OrcaBullet' class to manage bullets fired by orcas.

It handles the creation and movement of bullets on the screen.
Bullets are positioned randomly based on the location of orcas
and move down the screen at a specified speed.
"""

from random import choice

import pygame
from pygame.sprite import Sprite


class OrcaBullet(Sprite):
    """A class to manage the bullets shot by the orcas at random."""

    def __init__(self, s_penguin):
        """Create a bullet object and set its position."""
        super().__init__()
        self.screen = s_penguin.screen
        self.settings = s_penguin.settings

        # Load the image and get its rect.
        self.image = pygame.image.load("images/teeth.bmp")
        self.rect = self.image.get_rect()

        # Position the bullet using a random generator;
        #   only if the orcas are generated.
        try:
            orca = choice(s_penguin.orcas.sprites())
        except IndexError:
            pass
        else:
            self.rect.midleft = orca.rect.midleft

        # Store a float of the bullet's vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet down the screen."""
        self.y += self.settings.orca_bullet_speed
        # Update the bullet's rect.
        self.rect.y = self.y
