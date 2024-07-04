import pygame
from pygame.sprite import Sprite


class Penguin(Sprite):
    """Class to manage the penguin."""

    def __init__(self, s_penguin):
        """Initialize the penguin and set its starting position."""
        super().__init__()
        self.screen = s_penguin.screen
        self.settings = s_penguin.settings
        self.screen_rect = self.screen.get_rect()

        # Load the penguin's image and get its rect.
        self.image = pygame.image.load("images/penguin.bmp")
        self.rect = self.image.get_rect()

        # Set the penguin starting position at the bottom-center of the screen.
        self.center_penguin()

        # Movement flags; start with the penguin that's not moving.
        self.moving_right = False
        self.moving_left = False

    def center_penguin(self):
        """Center the penguin on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        # The Penguin is placed above the Scoreboard.
        self.rect.bottom = self.screen_rect.height - self.rect.height + 5
        # Store a float for the penguin's horizontal position.
        self.x = float(self.rect.x)

    def get_resized_image(self, width, height):
        """Return a resized version of the penguin's image."""
        return pygame.transform.scale(self.image, (width, height))

    def update(self):
        """Update the position of the penguin based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.penguin_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.penguin_speed

        # Update the penguin's rect from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the peguin on the screen."""
        self.screen.blit(self.image, self.rect)
