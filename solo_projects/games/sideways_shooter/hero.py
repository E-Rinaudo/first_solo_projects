"""
This module defines the 'Hero' class to manage the hero character in the game.

It handles the initialization, movement, and rendering of the hero sprite,
including image selection based on user input.
"""


import pygame
from pygame.sprite import Sprite


class Hero(Sprite):
    """A class to manage the hero."""

    def __init__(self, s_shooter):
        """Initialize the hero and set its starting position."""
        super().__init__()
        self.s_shooter = s_shooter
        self.screen = s_shooter.screen
        self.settings = s_shooter.settings
        self.screen_rect = self.screen.get_rect()

        # Set a flag to detect when the space key is pressed
        #   and choose an image accordingly.
        self.space_pressed = False
        self.rect = self.choose_image()

        # Center the hero on the screen's left side.
        self.center_hero()

        # Movement flags; start with the hero that's not moving.
        self.moving_up = False
        self.moving_down = False

    def choose_image(self):
        """
        Load the hero's images.
        Choose an image based on the pressing or release of the space key.
        Get its rect.
        """
        if self.space_pressed:
            self.image = pygame.image.load("images/hero1.bmp")
        else:
            self.image = pygame.image.load("images/hero2.bmp")
        rect = self.image.get_rect()
        return rect

    def center_hero(self):
        """Center the hero on the screen's left side."""
        self.rect.midleft = self.screen_rect.midleft
        # Store a float for the hero's vertical position.
        self.y = float(self.rect.y)

    def get_risized_image(self, width, height):
        """Return a resized version of the first hero image."""
        return pygame.transform.scale(self.image, (width, height))

    def update(self):
        """Update the hero's position based on movements flags."""
        if self.moving_up and self.rect.top > self.s_shooter.sb.score_rect.height * 3:
            self.y -= self.settings.hero_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.hero_speed

        # Update the hero's rect from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the hero on the screen."""
        self.screen.blit(self.image, self.rect)
