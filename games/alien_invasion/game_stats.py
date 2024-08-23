#!/usr/bin/env python3

"""
This module defines the 'GameStats' class to track and manage game statistics.

It handles the tracking of game statistics such as score, level, and ship limit.
It also manages high score reading and resets statistics at the start of a new game.
"""

from typing import TYPE_CHECKING

import json
from pathlib import Path

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from settings import Settings


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialize game statistics."""
        self.settings: "Settings" = ai_game.settings
        self.reset_stats()
        self.high_score: int = self.read_high_score()

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.ships_left: int = self.settings.difficulty_settings.ship_limit
        self.score: int = 0
        self.level: int = 1

    def read_high_score(self) -> int:
        """Read the high score when the game starts."""
        path: Path = Path("high_score/high_score.json")
        try:
            contents: str = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            high_score: int = 0
        else:
            high_score = json.loads(contents)

        return high_score
