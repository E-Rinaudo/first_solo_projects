#!/usr/bin/env python3

"""
This module defines the 'GameStats' class to track and manage game statistics.

It handles the tracking of game statistics such as score, level, and fox life.
It also manages high score reading and resets statistics at the start of a new game.
"""

from typing import TYPE_CHECKING

import json
from pathlib import Path

if TYPE_CHECKING:
    from hungry_fox import HungryFox
    from settings import Settings


class GameStats:
    """Track game statistics."""

    def __init__(self, h_fox: "HungryFox") -> None:
        """Initialize game statistics."""
        self.settings: "Settings" = h_fox.settings
        self.reset_stats()
        self.high_score: int = self.read_high_score()

    def reset_stats(self) -> None:
        """Initialize statistics that can change mid game."""
        self.fox_life: int = self.settings.difficulty_settings.fox_limit
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
