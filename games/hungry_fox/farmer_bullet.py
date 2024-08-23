#!/usr/bin/env python3

"""
This module defines the 'FarmerBullet' class to manage bullets fired by farmers.

It handles the creation and movement of bullets on the screen,
which are selected randomly from a set of images.
Bullets are positioned randomly based on the location of farmers
and move down the screen at a specified speed.
"""

from typing import TYPE_CHECKING
from random import choice

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from hungry_fox import HungryFox
    from settings import Settings


class FarmerBullet(Sprite):
    """A class to manage the bullets shot by the farmers at random."""

    def __init__(self, h_fox: "HungryFox") -> None:
        """Create a bullet object and set its position."""
        super().__init__()
        self.screen: pygame.Surface = h_fox.screen
        self.settings: "Settings" = h_fox.settings

        # Load the bullet's images, choose one random and get the rect.
        images: list[pygame.Surface] = self._farmers_bullets_images()
        self.image: pygame.Surface = choice(images)
        self.rect: pygame.Rect = self.image.get_rect()

        # Position the bullet using a random generator.
        farmer: Sprite = choice(h_fox.farmers.sprites())
        self.rect.midbottom = farmer.rect.midbottom  # type: ignore

        # Store a float of the bullet's vertical position.
        self.y: float = float(self.rect.y)

    def _farmers_bullets_images(self) -> list[pygame.Surface]:
        """Load two images of the same size and return them in a list."""
        image_1: pygame.Surface = pygame.image.load("images/fork.bmp")
        image_2: pygame.Surface = pygame.image.load("images/shovel.bmp")
        images: list[pygame.Surface] = [image_1, image_2]
        return images

    def update(self) -> None:  # pylint: disable=W0221
        """Move the bullet down the screen."""
        self.y += self.settings.difficulty_settings.farmer_bullet_speed
        # Update the bullet's rect.
        self.rect.y = int(self.y)
