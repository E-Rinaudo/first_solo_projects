#!/usr/bin/env python3

"""
This module defines the 'Bullet' class to manage bullets fired by the fox.

It handles the creation and movement of bullets on the screen.
It initializes bullets at the fox's current position
and updates their vertical position as they move up the screen.
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from hungry_fox import HungryFox
    from settings import Settings


class Bullet(Sprite):
    """A class to manage bullets shot by the fox."""

    def __init__(self, h_fox: "HungryFox") -> None:
        """Create a bullet object at the fox position."""
        super().__init__()
        self.screen: pygame.Surface = h_fox.screen
        self.settings: "Settings" = h_fox.settings

        # Load the bullet's image and get its rect.
        self.image: pygame.Surface = pygame.image.load("images/acorn.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Set the bullet's starting position.
        self.rect.midtop = h_fox.fox.rect.midtop

        # Store a float for the bullet's vertical position.
        self.y: float = float(self.rect.y)

    def update(self) -> None:  # pylint: disable=W0221
        """Move the bullet up the screen."""
        self.y -= self.settings.difficulty_settings.bullet_speed
        # Update the rect position.
        self.rect.y = int(self.y)
