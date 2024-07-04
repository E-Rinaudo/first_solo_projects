from random import randint

import pygame
from pygame.sprite import Sprite


class Orca(Sprite):
    """A class to represent a single orca from the fleet."""

    def __init__(self, s_penguin):
        """Initialize the orca and set its position."""
        super().__init__()
        self.screen = s_penguin.screen
        self.settings = s_penguin.settings

        # Load the image and get its rect.
        self.image = pygame.image.load("images/orca.bmp")
        self.rect = self.image.get_rect()

        # Set the orca on the top of the screen, outside of view.
        self.rect.bottom = self.screen.get_rect().top
        # Orcas will be generated randomly and will be placed at a maximum
        #   distance from the screen.
        orca_left_max = self.settings.screen_width - self.rect.width
        self.rect.left = randint(0, orca_left_max)

        # Store a float for the orca's vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the orca down the screen."""
        self.y += self.settings.orca_speed
        # Update the rect.
        self.rect.y = self.y
