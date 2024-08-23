#!/usr/bin/env python3

"""
This module defines the 'AlienBullet' class to manage bullets fired by aliens.

It handles the creation and movement of bullets on the screen,
which are selected randomly from a set of images.
Bullets are positioned randomly based on the location of aliens
and move leftward at a specified speed.
"""

from typing import TYPE_CHECKING
from random import choice

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from sideways_shooter import SidewaysShooter
    from settings import Settings


class AlienBullet(Sprite):
    """A class to manage the bullets shot by the aliens at random."""

    def __init__(self, s_shooter: "SidewaysShooter") -> None:
        """Create a bullet object and set its position."""
        super().__init__()
        self.screen: pygame.Surface = s_shooter.screen
        self.settings: "Settings" = s_shooter.settings

        # Load the bullet's images, choose one random and get the rect.
        images: list[pygame.Surface] = self._aliens_bullet_images()
        self.image: pygame.Surface = choice(images)
        self.rect: pygame.Rect = self.image.get_rect()

        # Set the bullet's position.
        self._set_bullet_position(s_shooter)

        # Store a float for the bullet's horizontal position.
        self.x: float = float(self.rect.x)

    def _set_bullet_position(self, s_shooter: "SidewaysShooter") -> None:
        """
        Position the bullet using a random generator,
        but only if the aliens' ships are generated.
        """
        try:
            alien: Sprite = choice(s_shooter.aliens.sprites())
        except IndexError:
            pass
        else:
            self.rect.midright = alien.rect.midleft  # type: ignore

    def _aliens_bullet_images(self) -> list[pygame.Surface]:
        """Load the bullet's images and return them in a list."""
        image_1: pygame.Surface = pygame.image.load("images/alien_bullet1.bmp")
        image_2: pygame.Surface = pygame.image.load("images/alien_bullet2.bmp")
        images: list[pygame.Surface] = [image_1, image_2]
        return images

    def update(self) -> None:  # pylint: disable=W0221
        """Move the bullet across the screen."""
        self.x -= self.settings.difficulty_settings.alien_bullet_speed
        # Update the bullet's rect.
        self.rect.x = int(self.x)
