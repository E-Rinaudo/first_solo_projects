from random import choice

import pygame
from pygame.sprite import Sprite


class Farmer(Sprite):
    """A class to represent a single farmer from the fleet."""

    def __init__(self, h_fox):
        """Initialize the farmer and set its position."""
        super().__init__()
        self.screen = h_fox.screen
        self.settings = h_fox.settings

        # Load two images of the same size and get the rect of one.
        # Use random.choice to choose between images.
        image_1 = pygame.image.load("images/farmer1.bmp")
        image_2 = pygame.image.load("images/farmer2.bmp")
        images = [image_1, image_2]
        self.image = choice(images)
        self.rect = self.image.get_rect()

        # Store a float for the farmer's horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if the farmer is going over either edges."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the farmer to the right or left."""
        self.x += self.settings.farmer_speed * self.settings.farmer_direction
        # Update the rect.
        self.rect.x = self.x
