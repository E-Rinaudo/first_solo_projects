from random import randint

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien from the fleet."""

    def __init__(self, s_shooter):
        """Initialize the alien and set its position."""
        super().__init__()
        self.screen = s_shooter.screen
        self.settings = s_shooter.settings
        self.sb = s_shooter.sb

        # Load the image and get its rect.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Set the alien on the right side of the screen, outside of view.
        self.rect.left = self.screen.get_rect().right
        # Aliens will be generated randomly and placed at a maximum height
        #   from the bottom and top of the screen.
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(self.sb.score_rect.height * 3, alien_top_max)

        # Store a float for the alien's horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien across the screen."""
        self.x -= self.settings.alien_speed
        # Update the rect.
        self.rect.x = self.x
