#!/usr/bin/env python3

"""
This module defines the 'Farmer' class to represent individual farmers in the game.

It manages the initialization and movement of farmer sprites.
The farmer images are selected randomly from a set of images.
"""

from typing import TYPE_CHECKING
from random import choice

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from hungry_fox import HungryFox
    from settings import Settings


class Farmer(Sprite):
    """A class to represent a single farmer from the fleet."""

    def __init__(self, h_fox: "HungryFox") -> None:
        """Initialize the farmer and set its position."""
        super().__init__()
        self.screen: pygame.Surface = h_fox.screen
        self.settings: "Settings" = h_fox.settings

        # Load the farmer's images, get the rect of one and choose them at random.
        images: list[pygame.Surface] = self._farmers_images()
        self.image: pygame.Surface = choice(images)
        self.rect: pygame.Rect = self.image.get_rect()

        # Store a float for the farmer's horizontal position.
        self.x: float = float(self.rect.x)

    def _farmers_images(self) -> list[pygame.Surface]:
        """Load two images of the same size and return them in a list."""
        image_1: pygame.Surface = pygame.image.load("images/farmer1.bmp")
        image_2: pygame.Surface = pygame.image.load("images/farmer2.bmp")
        images: list[pygame.Surface] = [image_1, image_2]
        return images

    def check_edges(self) -> bool:
        """Return True if the farmer is going over either edges."""
        screen_rect: pygame.Rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self) -> None:  # pylint: disable=W0221
        """Move the farmer to the right or left."""
        self.x += (
            self.settings.difficulty_settings.farmer_speed
            * self.settings.farmer_direction
        )
        # Update the rect.
        self.rect.x = int(self.x)
