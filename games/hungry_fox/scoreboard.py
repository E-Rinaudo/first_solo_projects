#!/usr/bin/env python3

"""
This module defines the 'Scoreboard' class to display and update scoring information.

It manages the rendering of the current score, high score, level,
and remaining fox life on the screen.
It handles updating and positioning these elements based on the game's state.
"""

import pygame.font
from pygame.sprite import Group

from fox import Fox


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, h_fox):
        """Initialize scorekeeping attributes."""
        self.h_fox = h_fox
        self.screen = h_fox.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = h_fox.stats

        # Font settings for scoring information.
        self.text_color = (22, 57, 129)
        self.font = pygame.font.SysFont(None, 30)

        self._prep_scoreboard()

    def _prep_scoreboard(self):
        """Prepare the initial score, high-score, level and fox images."""
        self.prep_score()
        self._prep_high_score()
        self.prep_level()
        self.prep_foxs()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score {rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, None)

        # Display the score at the top left of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 5
        self.score_rect.left = self.screen_rect.left

    def _prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score {high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, None
        )

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

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

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.score_rect.top * 5

    def prep_foxs(self):
        """Show how many foxs are left and resize the fox image."""
        self.foxs_resized = Group()

        # Width and height of the resized fox image.
        fox_width, fox_height = 55, 34
        # Total available width, excluding menu and pause buttons.
        available_width = (
            self.screen_rect.width - self.h_fox.pause_button.rect.width * 2
        )

        # Calculate the total width required for all foxs.
        total_foxs_width = self.stats.fox_life * fox_width
        # Get the starting x position to place foxs on the top right.
        start_x = available_width - total_foxs_width

        for fox_number in range(self.stats.fox_life):
            fox = Fox(self.h_fox)
            resized_image = fox.get_resized_image(fox_width, fox_height)
            fox.image = resized_image
            fox.rect = resized_image.get_rect()
            fox.rect.x = (start_x) + (fox_number * fox_width)
            fox.rect.y = self.score_rect.top // 2
            self.foxs_resized.add(fox)

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.foxs_resized.draw(self.screen)
