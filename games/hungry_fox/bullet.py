#!/usr/bin/env python3

"""
This module defines the 'Bullet' class to manage bullets fired by the fox.

It handles the creation and movement of bullets on the screen.
It initializes bullets at the fox's current position
and updates their vertical position as they move up the screen.
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets shot by the fox."""

    def __init__(self, h_fox):
        """Create a bullet object at the fox position."""
        super().__init__()
        self.screen = h_fox.screen
        self.settings = h_fox.settings

        # Load the bullet's image and get its rect.
        self.image = pygame.image.load("images/acorn.bmp")
        self.rect = self.image.get_rect()

        # Set the bullet's starting position.
        self.rect.midtop = h_fox.fox.rect.midtop

        # Store a float for the bullet's vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
