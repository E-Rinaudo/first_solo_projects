#!/usr/bin/env python3

"""
This module defines the 'Bullet' class to manage bullets fired by the penguin.

It handles the creation and movement of bullets on the screen.
It initializes bullets at the penguin's current position
and updates their vertical position as they move up the screen.
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from sliding_penguin import SlidingPenguin
    from settings import Settings


class Bullet(Sprite):
    """A class to manage bullets shot by the penguin."""

    def __init__(self, s_penguin: "SlidingPenguin") -> None:
        """Create a bullet object at the penguin's current location."""
        super().__init__()
        self.screen: pygame.Surface = s_penguin.screen
        self.settings: "Settings" = s_penguin.settings

        # Load the bullet image and get its rect.
        self.image: pygame.Surface = pygame.image.load("images/snowball.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Set the bullet's starting position.
        self.rect.midtop = s_penguin.penguin.rect.midtop

        # Store a float for the bullet's vertical position.
        self.y: float = float(self.rect.y)

    def update(self) -> None:  # pylint: disable=W0221
        """Move the bullet up the screen."""
        self.y -= self.settings.difficulty_settings.bullet_speed
        # Update the rect position.
        self.rect.y = int(self.y)
