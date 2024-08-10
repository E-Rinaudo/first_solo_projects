#!/usr/bin/env python3

"""
This module defines the 'Scoreboard' class to display and update scoring information.

It manages the rendering of the current score, high score, level,
and remaining penguin life on the screen.
It handles updating and positioning these elements based on the game's state.
"""

import pygame.font
from pygame.sprite import Group

from penguin import Penguin


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, s_penguin):
        """Initialize scorekeeping attributes."""
        self.s_penguin = s_penguin
        self.screen = s_penguin.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = s_penguin.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        self._prep_scoreboard()

    def _prep_scoreboard(self):
        """Prepare the initial score, high-score, level and penguin images."""
        self.prep_score()
        self._prep_high_score()
        self.prep_level()
        self.prep_penguins()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score {rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, None)

        # Display the score at the bottom left of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.bottomleft = self.screen_rect.bottomleft
        self.score_rect.bottom -= 2.5

    def _prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score {high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, None
        )

        # Center the high score at the bottom of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.midbottom = self.screen_rect.midbottom
        self.high_score_rect.bottom = self.score_rect.bottom

    def check_high_score(self):
        """Check if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self._prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_font = pygame.font.SysFont(None, 25)
        level_str = f"Level {self.stats.level}"
        self.level_image = self.level_font.render(
            level_str, True, self.text_color, None
        )

        # Position the level above the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.bottomleft = self.score_rect.bottomleft
        self.level_rect.bottom -= 25

    def prep_penguins(self):
        """Show how many penguins are left and resize the penguin image."""
        self.penguins_resized = Group()

        # Width and height of the resized penguin image.
        penguin_width, penguin_height = 25, 45

        # Calculate the total width required for all penguins.
        total_penguins_width = self.stats.penguin_life * penguin_width
        # Get the starting x position to place penguins on the top right.
        start_x = self.screen_rect.width - total_penguins_width

        for penguin_number in range(self.stats.penguin_life):
            penguin = Penguin(self.s_penguin)
            resized_image = penguin.get_resized_image(penguin_width, penguin_height)
            penguin.image = resized_image
            penguin.rect = resized_image.get_rect()
            penguin.rect.x = (start_x) + (penguin_number * penguin_width)
            penguin.rect.y = self.screen_rect.height - (self.score_rect.height + 30)
            self.penguins_resized.add(penguin)

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.penguins_resized.draw(self.screen)
