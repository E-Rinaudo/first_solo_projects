#!/usr/bin/env python3

"""
This module defines the 'FarmerBullet' class to manage bullets fired by farmers.

It handles the creation and movement of bullets on the screen,
which are selected randomly from a set of images.
Bullets are positioned randomly based on the location of farmers
and move down the screen at a specified speed.
"""

from random import choice

import pygame
from pygame.sprite import Sprite


class FarmerBullet(Sprite):
    """A class to manage the bullets shot by the farmers at random."""

    def __init__(self, h_fox):
        """Create a bullet object and set its position."""
        super().__init__()
        self.screen = h_fox.screen
        self.settings = h_fox.settings

        # Load the bullet's images, choose one random and get the rect.
        image_1 = pygame.image.load("images/fork.bmp")
        image_2 = pygame.image.load("images/shovel.bmp")
        images = [image_1, image_2]
        self.image = choice(images)
        self.rect = self.image.get_rect()

        # Position the bullet using a random generator.
        farmer = choice(h_fox.farmers.sprites())
        self.rect.midbottom = farmer.rect.midbottom

        # Store a float of the bullet's vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet down the screen."""
        self.y += self.settings.farmer_bullet_speed
        # Update the bullet's rect.
        self.rect.y = self.y
