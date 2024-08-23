#!/usr/bin/env python3

"""
This module defines the 'Explosion' class to manage explosion effects in the game.

It handles the initialization and display of explosion sprites,
including managing their duration on the screen before removal.
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from sideways_shooter import SidewaysShooter


class Explosion(Sprite):
    """A Class to manage the explosion of the game."""

    def __init__(self, s_shooter: "SidewaysShooter") -> None:
        """Initialize the explosion."""
        super().__init__()
        self.screen: pygame.Surface = s_shooter.screen

        # Load the image and get its rect.
        self.image: pygame.Surface = pygame.image.load("images/explosion.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Initialize the frame count that defines how long the explosion
        #   stays on the screen.
        self.frame_count: int = 0
        self.max_frames: int = 20

    def update(self) -> None:  # pylint: disable=W0221
        """Update the explosion using the frame count."""
        if self.frame_count > self.max_frames:
            # Remove the explosion sprite from the group.
            self.kill()
        self.frame_count += 1
