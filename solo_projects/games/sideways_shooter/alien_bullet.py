from random import choice

import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    """A class to manage the bullets shot by the aliens at random."""

    def __init__(self, s_shooter):
        """Create a bullet object and set its position."""
        super().__init__()
        self.screen = s_shooter.screen
        self.settings = s_shooter.settings

        # Load the bullet's images, choose one random and get the rect.
        image_1 = pygame.image.load("images/alien_bullet1.bmp")
        image_2 = pygame.image.load("images/alien_bullet2.bmp")
        images = [image_1, image_2]
        self.image = choice(images)
        self.rect = self.image.get_rect()

        # Position the bullet using a random generator;
        #   only if the aliens' ships are generated.
        try:
            alien = choice(s_shooter.aliens.sprites())
        except IndexError:
            pass
        else:
            self.rect.midright = alien.rect.midleft

        # Store a float for the bullet's horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen."""
        self.x -= self.settings.alien_bullet_speed
        # Update the bullet's rect.
        self.rect.x = self.x
