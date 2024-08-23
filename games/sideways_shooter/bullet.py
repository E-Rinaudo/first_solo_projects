#!/usr/bin/env python3

"""
This module defines the 'Bullet' class to manage bullets fired by the hero.

It handles the creation and movement of bullets on the screen.
It initializes bullets at the hero's current position
and updates their horizontal position as they move rightward across the screen.
"""

from typing import TYPE_CHECKING
from random import choice

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from sideways_shooter import SidewaysShooter
    from settings import Settings


class Bullet(Sprite):
    """A class to manage bullets fired from the hero."""

    def __init__(self, s_shooter: "SidewaysShooter") -> None:
        """Create the bullet at the hero's starting position."""
        super().__init__()
        self.screen: pygame.Surface = s_shooter.screen
        self.settings: "Settings" = s_shooter.settings

        # Load the bullet's images, choose one random and get the rect.
        images: list[pygame.Surface] = self._hero_bullets_images()
        self.image: pygame.Surface = choice(images)
        self.rect: pygame.Rect = self.image.get_rect()

        # Position the bullet based on the hero's position.
        self.rect.midleft = s_shooter.hero.rect.midright

        # Store a float for the bullet's horizontal position.
        self.x: float = float(self.rect.x)

    def _hero_bullets_images(self) -> list[pygame.Surface]:
        """Load four images of the same size and return them in a list."""
        image_1: pygame.Surface = pygame.image.load("images/bullet1.bmp")
        image_2: pygame.Surface = pygame.image.load("images/bullet2.bmp")
        image_3: pygame.Surface = pygame.image.load("images/bullet3.bmp")
        image_4: pygame.Surface = pygame.image.load("images/bullet4.bmp")
        images: list[pygame.Surface] = [image_1, image_2, image_3, image_4]
        return images

    def update(self) -> None:  # pylint: disable=W0221
        """Move the bullet across the screen."""
        self.x += self.settings.difficulty_settings.bullet_speed
        # Update the bullet's rect.
        self.rect.x = int(self.x)
