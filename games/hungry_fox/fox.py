#!/usr/bin/env python3

"""
This module defines the 'Fox' class to manage the fox character in the game.

It handles the initialization, movement, and rendering of the fox sprite.
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from hungry_fox import HungryFox
    from settings import Settings


class Fox(Sprite):  # pylint: disable=R0902
    """Class to manage the fox."""

    def __init__(self, h_fox: "HungryFox") -> None:
        """Initialize the fox and set its starting position."""
        super().__init__()
        self.screen: pygame.Surface = h_fox.screen
        self.settings: "Settings" = h_fox.settings
        self.screen_rect: pygame.Rect = self.screen.get_rect()

        # Load the fox's image and get its rect.
        self.image: pygame.Surface = pygame.image.load("images/fox.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Set the fox starting position at the bottom-center of the screen.
        self.center_fox()

        # Movement flags; start with the fox that's not moving.
        self.moving_right: bool = False
        self.moving_left: bool = False

    def center_fox(self) -> None:
        """Center the fox on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a float for the fox's horizontal position.
        self.x: float = float(self.rect.x)

    def get_resized_image(self, width: int, height: int) -> pygame.Surface:
        """Return a resized version of the fox's image."""
        return pygame.transform.scale(self.image, (width, height))

    def update(self) -> None:  # pylint: disable=W0221
        """Update the position of the fox based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.difficulty_settings.fox_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.difficulty_settings.fox_speed

        # Update the fox's rect from self.x.
        self.rect.x = int(self.x)

    def blitme(self) -> None:
        """Draw the fox on the screen."""
        self.screen.blit(self.image, self.rect)
