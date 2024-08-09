"""
This module defines the 'Explosion' class to manage explosion effects in the game.

It handles the initialization and display of explosion sprites,
including managing their duration on the screen before removal.
"""

import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """A Class to manage the explosion of the game."""

    def __init__(self, s_shooter):
        """Initialize the explosion."""
        super().__init__()
        self.screen = s_shooter.screen

        # Load the image and get its rect.
        self.image = pygame.image.load("images/explosion.bmp")
        self.rect = self.image.get_rect()

        # Initialize the frame count that defines how long the explosion
        #   stays on the screen.
        self.frame_count = 0
        self.max_frames = 20

    def update(self):
        """Update the explosion using the frame count."""
        if self.frame_count > self.max_frames:
            # Remove the explosion sprite from the group.
            self.kill()
        self.frame_count += 1
