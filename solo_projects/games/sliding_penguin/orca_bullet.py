from random import choice

import pygame
from pygame.sprite import Sprite


class OrcaBullet(Sprite):
    """A class to manage the bullets shot by the orcas at random."""

    def __init__(self, s_penguin):
        """Create a bullet object and set its position."""
        super().__init__()
        self.screen = s_penguin.screen
        self.settings = s_penguin.settings

        # Load the image and get its rect.
        self.image = pygame.image.load('images/teeth.bmp')
        self.rect = self.image.get_rect()

        # Position the bullet using a random generator;
        #   only if the orcas are generated.
        try:
            orca = choice(s_penguin.orcas.sprites())
        except IndexError:
            pass
        else:
            self.rect.midleft = orca.rect.midleft

        # Store a float of the bullet's vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet down the screen."""
        self.y += self.settings.orca_bullet_speed
        # Update the bullet's rect.
        self.rect.y = self.y