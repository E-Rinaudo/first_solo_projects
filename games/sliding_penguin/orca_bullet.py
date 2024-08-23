#!/usr/bin/env python3

"""
This module defines the 'OrcaBullet' class to manage bullets fired by orcas.

It handles the creation and movement of bullets on the screen.
Bullets are positioned randomly based on the location of orcas
and move down the screen at a specified speed.
"""

from typing import TYPE_CHECKING
from random import choice

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from sliding_penguin import SlidingPenguin
    from settings import Settings


class OrcaBullet(Sprite):
    """A class to manage the bullets shot by the orcas at random."""

    def __init__(self, s_penguin: "SlidingPenguin") -> None:
        """Create a bullet object and set its position."""
        super().__init__()
        self.screen: pygame.Surface = s_penguin.screen
        self.settings: "Settings" = s_penguin.settings

        # Load the image and get its rect.
        self.image: pygame.Surface = pygame.image.load("images/teeth.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Set the bullet position.
        self._set_bullet_position(s_penguin)

        # Store a float of the bullet's vertical position.
        self.y: float = float(self.rect.y)

    def _set_bullet_position(self, s_penguin: "SlidingPenguin") -> None:
        """
        Position the bullet using a random generator,
        but only if the orcas are generated.
        """
        try:
            orca: Sprite = choice(s_penguin.orcas.sprites())
        except IndexError:
            pass
        else:
            self.rect.midleft = orca.rect.midleft  # type: ignore

    def update(self) -> None:  # pylint: disable=W0221
        """Move the bullet down the screen."""
        self.y += self.settings.difficulty_settings.orca_bullet_speed
        # Update the bullet's rect.
        self.rect.y = int(self.y)
