#!/usr/bin/env python3

"""
This module defines the 'Penguin' class to manage the penguin character in the game.

It handles the initialization, movement, and rendering of the penguin sprite.
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from sliding_penguin import SlidingPenguin
    from settings import Settings


class Penguin(Sprite):  # pylint: disable=R0902
    """Class to manage the penguin."""

    def __init__(self, s_penguin: "SlidingPenguin") -> None:
        """Initialize the penguin and set its starting position."""
        super().__init__()
        self.screen: pygame.Surface = s_penguin.screen
        self.settings: "Settings" = s_penguin.settings
        self.screen_rect: pygame.Rect = self.screen.get_rect()

        # Load the penguin's image and get its rect.
        self.image: pygame.Surface = pygame.image.load("images/penguin.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Set the penguin starting position at the bottom-center of the screen.
        self.center_penguin()

        # Movement flags; start with the penguin that's not moving.
        self.moving_right: bool = False
        self.moving_left: bool = False

    def center_penguin(self) -> None:
        """Center the penguin on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        # The Penguin is placed above the Scoreboard.
        self.rect.bottom = self.screen_rect.height - self.rect.height + 5
        # Store a float for the penguin's horizontal position.
        self.x: float = float(self.rect.x)

    def get_resized_image(self, width: int, height: int) -> pygame.Surface:
        """Return a resized version of the penguin's image."""
        return pygame.transform.scale(self.image, (width, height))

    def update(self) -> None:  # pylint: disable=W0221
        """Update the position of the penguin based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.difficulty_settings.penguin_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.difficulty_settings.penguin_speed

        # Update the penguin's rect from self.x.
        self.rect.x = int(self.x)

    def blitme(self) -> None:
        """Draw the peguin on the screen."""
        self.screen.blit(self.image, self.rect)
