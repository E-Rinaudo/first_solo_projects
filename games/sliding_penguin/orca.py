#!/usr/bin/env python3

"""
This module defines the 'Orca' class to represent individual orcas in the game.

It manages the initialization and movement of orca sprites.
Orcas are placed randomly at the top of the screen and move downwards at a set speed.
"""

from typing import TYPE_CHECKING
from random import randint

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from sliding_penguin import SlidingPenguin
    from settings import Settings


class Orca(Sprite):
    """A class to represent a single orca from the fleet."""

    def __init__(self, s_penguin: "SlidingPenguin") -> None:
        """Initialize the orca and set its position."""
        super().__init__()
        self.screen: pygame.Surface = s_penguin.screen
        self.settings: "Settings" = s_penguin.settings

        # Load the image and get its rect.
        self.image: pygame.Surface = pygame.image.load("images/orca.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Set the orca position.
        self._set_orca_position()

        # Store a float for the orca's vertical position.
        self.y: float = float(self.rect.y)

    def _set_orca_position(self) -> None:
        """Set the orca on the top of the screen, outside of view."""
        self.rect.bottom = self.screen.get_rect().top
        # Orcas will be generated randomly and will be placed at a maximum
        #   distance from the screen.
        orca_left_max: int = self.settings.screen_width - self.rect.width
        self.rect.left = randint(0, orca_left_max)

    def update(self) -> None:  # pylint: disable=W0221
        """Move the orca down the screen."""
        self.y += self.settings.difficulty_settings.orca_speed
        # Update the rect.
        self.rect.y = int(self.y)
