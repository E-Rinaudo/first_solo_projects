#!/usr/bin/env python3

"""
This module defines the 'Bullet' class to manage bullets fired by the hero.

It handles the creation and movement of bullets on the screen.
It initializes bullets at the hero's current position
and updates their horizontal position as they move rightward across the screen.
"""

from random import choice

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the hero."""

    def __init__(self, s_shooter):
        """Create the bullet at the hero's starting position."""
        super().__init__()
        self.screen = s_shooter.screen
        self.settings = s_shooter.settings

        # Load the bullet's images, choose one random and get the rect.
        image_1 = pygame.image.load("images/bullet1.bmp")
        image_2 = pygame.image.load("images/bullet2.bmp")
        image_3 = pygame.image.load("images/bullet3.bmp")
        image_4 = pygame.image.load("images/bullet4.bmp")
        images = [image_1, image_2, image_3, image_4]
        self.image = choice(images)
        self.rect = self.image.get_rect()

        # Position the bullet based on the hero's position.
        self.rect.midleft = s_shooter.hero.rect.midright

        # Store a float for the bullet's horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen."""
        self.x += self.settings.bullet_speed
        # Update the bullet's rect.
        self.rect.x = self.x
