#!/usr/bin/env python3

"""
This module defines the 'Scoreboard' class to display and update scoring information.

It manages the rendering of the current score, high score, level,
and remaining ships on the screen.
It handles updating and positioning these elements based on the game's state.
"""

from typing import TYPE_CHECKING

import pygame.font
from pygame.sprite import Group

from ship import Ship

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
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
        self.ships_resized: Group = Group()


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen: pygame.Surface = ai_game.screen
        self.screen_rect: pygame.Rect = self.screen.get_rect()
        self.stats: "GameStats" = ai_game.stats

        # Font settings for scoring information.
        self.text_color: tuple[int, int, int] = (200, 200, 200)
        self.font: pygame.font.Font = pygame.font.SysFont(None, 30)

        # Initialize the score-related visuals.
        self.scores_images: ScoresImages = ScoresImages()

        self._prep_scoreboard()

    def _prep_scoreboard(self) -> None:
        """Prepare the initial score, high-score, level and ship images."""
        self.prep_score()
        self._prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self) -> None:
        """Turn the score into a rendered image."""
        rounded_score: int = round(self.stats.score, -1)
        score_str: str = f"Score {rounded_score:,}"
        self.scores_images.score_image = self.font.render(
            score_str, True, self.text_color, None
        )

        # Display the score at the top left of the screen.
        self.scores_images.score_rect = self.scores_images.score_image.get_rect()
        self.scores_images.score_rect.top = 10
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
        self.scores_images.level_rect.top = self.scores_images.score_rect.top * 3

    def prep_ships(self) -> None:
        """Show how many ships are left and resize the ship image."""
        self.scores_images.ships_resized = Group()

        # Width and height of the resized ship image.
        ship_width: int = 35
        ship_height: int = 40
        # Total available width, excluding menu and pause buttons.
        available_width: int = (
            self.screen_rect.width
            - self.ai_game.game_buttons.pause_button.rect.width * 2
        )

        # Calculate the total width required for all ships.
        total_ships_width: int = self.stats.ships_left * ship_width
        # Get the starting x position to place ships on the top right.
        start_x: int = available_width - total_ships_width

        for ship_number in range(self.stats.ships_left):
            ship: Ship = Ship(self.ai_game)
            resized_image: pygame.Surface = ship.get_resized_image(
                ship_width, ship_height
            )
            ship.image = resized_image
            ship.rect = resized_image.get_rect()
            ship.rect.x = (start_x) + (ship_number * ship_width)
            ship.rect.y = self.scores_images.score_rect.top // 2
            self.scores_images.ships_resized.add(ship)

    def show_score(self) -> None:
        """Draw the score to the screen."""
        self.screen.blit(self.scores_images.score_image, self.scores_images.score_rect)
        self.screen.blit(
            self.scores_images.high_score_image, self.scores_images.high_score_rect
        )
        self.screen.blit(self.scores_images.level_image, self.scores_images.level_rect)
        self.scores_images.ships_resized.draw(self.screen)
