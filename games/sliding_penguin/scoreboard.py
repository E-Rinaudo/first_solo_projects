#!/usr/bin/env python3

"""
This module defines the 'Scoreboard' class to display and update scoring information.

It manages the rendering of the current score, high score, level,
and remaining penguin life on the screen.
It handles updating and positioning these elements based on the game's state.
"""

from typing import TYPE_CHECKING

import pygame.font
from pygame.sprite import Group

from penguin import Penguin

if TYPE_CHECKING:
    from sliding_penguin import SlidingPenguin
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
        self.penguins_resized: Group = Group()


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, s_penguin: "SlidingPenguin") -> None:
        """Initialize scorekeeping attributes."""
        self.s_penguin = s_penguin
        self.screen: pygame.Surface = s_penguin.screen
        self.screen_rect: pygame.Rect = self.screen.get_rect()
        self.stats: "GameStats" = s_penguin.stats

        # Font settings for scoring information.
        self.text_color: tuple[int, int, int] = (30, 30, 30)
        self.font: pygame.font.Font = pygame.font.SysFont(None, 30)

        # Initialize the score-related visuals.
        self.scores_images: ScoresImages = ScoresImages()

        self._prep_scoreboard()

    def _prep_scoreboard(self) -> None:
        """Prepare the initial score, high-score, level and penguin images."""
        self.prep_score()
        self._prep_high_score()
        self.prep_level()
        self.prep_penguins()

    def prep_score(self) -> None:
        """Turn the score into a rendered image."""
        rounded_score: int = round(self.stats.score, -1)
        score_str: str = f"Score {rounded_score:,}"
        self.scores_images.score_image = self.font.render(
            score_str, True, self.text_color, None
        )

        # Display the score at the bottom left of the screen.
        self.scores_images.score_rect = self.scores_images.score_image.get_rect()
        self.scores_images.score_rect.bottomleft = self.screen_rect.bottomleft
        self.scores_images.score_rect.bottom -= 2

    def _prep_high_score(self) -> None:
        """Turn the high score into a rendered image."""
        high_score: int = round(self.stats.high_score, -1)
        high_score_str: str = f"High Score {high_score:,}"
        self.scores_images.high_score_image = self.font.render(
            high_score_str, True, self.text_color, None
        )

        # Center the high score at the bottom of the screen.
        self.scores_images.high_score_rect = (
            self.scores_images.high_score_image.get_rect()
        )
        self.scores_images.high_score_rect.midbottom = self.screen_rect.midbottom
        self.scores_images.high_score_rect.bottom = self.scores_images.score_rect.bottom

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

        # Position the level above the score.
        self.scores_images.level_rect = self.scores_images.level_image.get_rect()
        self.scores_images.level_rect.bottomleft = (
            self.scores_images.score_rect.bottomleft
        )
        self.scores_images.level_rect.bottom -= 25

    def prep_penguins(self) -> None:
        """Show how many penguins are left and resize the penguin image."""
        self.scores_images.penguins_resized = Group()

        # Width and height of the resized penguin image.
        penguin_width: int = 25
        penguin_height: int = 45

        # Calculate the total width required for all penguins.
        total_penguins_width: int = self.stats.penguin_life * penguin_width
        # Get the starting x position to place penguins on the top right.
        start_x: int = self.screen_rect.width - total_penguins_width

        for penguin_number in range(self.stats.penguin_life):
            penguin: Penguin = Penguin(self.s_penguin)
            resized_image: pygame.Surface = penguin.get_resized_image(
                penguin_width, penguin_height
            )
            penguin.image = resized_image
            penguin.rect = resized_image.get_rect()
            penguin.rect.x = (start_x) + (penguin_number * penguin_width)
            penguin.rect.y = self.screen_rect.height - (
                self.scores_images.score_rect.height + 30
            )
            self.scores_images.penguins_resized.add(penguin)

    def show_score(self) -> None:
        """Draw the score to the screen."""
        self.screen.blit(self.scores_images.score_image, self.scores_images.score_rect)
        self.screen.blit(
            self.scores_images.high_score_image, self.scores_images.high_score_rect
        )
        self.screen.blit(self.scores_images.level_image, self.scores_images.level_rect)
        self.scores_images.penguins_resized.draw(self.screen)
