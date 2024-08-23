#!/usr/bin/env python3

"""
This module defines the 'Scoreboard' class to display and update scoring information.

It manages the rendering of the current score, high score, level,
and remaining fox life on the screen.
It handles updating and positioning these elements based on the game's state.
"""

from typing import TYPE_CHECKING

import pygame.font
from pygame.sprite import Group

from fox import Fox

if TYPE_CHECKING:
    from hungry_fox import HungryFox
    from game_stats import GameStats


class ScoresImages:  # pylint: disable=R0903
    """A class to encapsulate all score-related attributes."""

    def __init__(self) -> None:
        """Initialize the attributes for score-related visuals."""
        self.score_image: pygame.Surface = pygame.Surface((0, 0))
        self.score_rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        self.high_score_image: pygame.Surface = pygame.Surface((0, 0))
        self.high_score_rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        self.level_image: pygame.Surface = pygame.Surface((0, 0))
        self.level_rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        self.foxs_resized: Group = Group()


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, h_fox: "HungryFox") -> None:
        """Initialize scorekeeping attributes."""
        self.h_fox = h_fox
        self.screen: pygame.Surface = h_fox.screen
        self.screen_rect: pygame.Rect = self.screen.get_rect()
        self.stats: "GameStats" = h_fox.stats

        # Font settings for scoring information.
        self.text_color: tuple[int, int, int] = (22, 57, 129)
        self.font: pygame.font.Font = pygame.font.SysFont(None, 30)

        # Initialize the score-related visuals.
        self.scores_images: ScoresImages = ScoresImages()

        self._prep_scoreboard()

    def _prep_scoreboard(self) -> None:
        """Prepare the initial score, high-score, level and fox images."""
        self.prep_score()
        self._prep_high_score()
        self.prep_level()
        self.prep_foxs()

    def prep_score(self) -> None:
        """Turn the score into a rendered image."""
        rounded_score: int = round(self.stats.score, -1)
        score_str: str = f"Score {rounded_score:,}"
        self.scores_images.score_image = self.font.render(
            score_str, True, self.text_color, None
        )

        # Display the score at the top left of the screen.
        self.scores_images.score_rect = self.scores_images.score_image.get_rect()
        self.scores_images.score_rect.top = 5
        self.scores_images.score_rect.left = self.screen_rect.left

    def _prep_high_score(self) -> None:
        """Turn the high score into a rendered image."""
        high_score: int = round(self.stats.high_score, -1)
        high_score_str: str = f"High Score {high_score:,}"
        self.scores_images.high_score_image = self.font.render(
            high_score_str, True, self.text_color, None
        )

        # Center the high score at the top of the screen.
        self.scores_images.high_score_rect = (
            self.scores_images.high_score_image.get_rect()
        )
        self.scores_images.high_score_rect.centerx = self.screen_rect.centerx
        self.scores_images.high_score_rect.top = self.scores_images.score_rect.top

    def check_high_score(self) -> None:
        """Check if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self._prep_high_score()

    def prep_level(self) -> None:
        """Turn the level into a rendered image."""
        level_font: pygame.font.Font = pygame.font.SysFont(None, 25)
        level_str: str = f"Level {self.stats.level}"
        self.scores_images.level_image = level_font.render(
            level_str, True, self.text_color, None
        )

        # Position the level below the score.
        self.scores_images.level_rect = self.scores_images.level_image.get_rect()
        self.scores_images.level_rect.left = self.scores_images.score_rect.left
        self.scores_images.level_rect.top = self.scores_images.score_rect.top * 5

    def prep_foxs(self) -> None:
        """Show how many foxs are left and resize the fox image."""
        self.scores_images.foxs_resized = Group()

        # Width and height of the resized fox image.
        fox_width: int = 55
        fox_height: int = 34
        # Total available width, excluding menu and pause buttons.
        available_width: int = (
            self.screen_rect.width - self.h_fox.game_buttons.pause_button.rect.width * 2
        )

        # Calculate the total width required for all foxs.
        total_foxs_width: int = self.stats.fox_life * fox_width
        # Get the starting x position to place foxs on the top right.
        start_x: int = available_width - total_foxs_width

        for fox_number in range(self.stats.fox_life):
            fox: Fox = Fox(self.h_fox)
            resized_image: pygame.Surface = fox.get_resized_image(fox_width, fox_height)
            fox.image = resized_image
            fox.rect = resized_image.get_rect()
            fox.rect.x = (start_x) + (fox_number * fox_width)
            fox.rect.y = self.scores_images.score_rect.top // 2
            self.scores_images.foxs_resized.add(fox)

    def show_score(self) -> None:
        """Draw the score to the screen."""
        self.screen.blit(self.scores_images.score_image, self.scores_images.score_rect)
        self.screen.blit(
            self.scores_images.high_score_image, self.scores_images.high_score_rect
        )
        self.screen.blit(self.scores_images.level_image, self.scores_images.level_rect)
        self.scores_images.foxs_resized.draw(self.screen)
