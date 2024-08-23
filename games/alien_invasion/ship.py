#!/usr/bin/env python3

"""
This module defines the 'Ship' class to manage the ship in the game.

It handles the initialization, movement, and rendering of the ship sprite.
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from settings import Settings


class Ship(Sprite):  # pylint: disable=R0902
    """A class to manage the ship."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen: pygame.Surface = ai_game.screen
        self.settings: "Settings" = ai_game.settings
        self.screen_rect: pygame.Rect = ai_game.screen.get_rect()

        # Load the ship's image and get its rect.
        self.image: pygame.Surface = pygame.image.load("images/ship.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Start each new ship at the bottom-center of the screen.
        self.center_ship()

        # Movement flags; start with a ship that's not moving.
        self.moving_right: bool = False
        self.moving_left: bool = False

    def center_ship(self) -> None:
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a float for the ship's exact horizontal position.
        self.x: float = float(self.rect.x)

    def get_resized_image(self, width: int, height: int) -> pygame.Surface:
        """Return a resized version of the ship's image."""
        return pygame.transform.scale(self.image, (width, height))

    def update(self) -> None:  # pylint: disable=W0221
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.difficulty_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.difficulty_settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = int(self.x)

    def blitme(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
