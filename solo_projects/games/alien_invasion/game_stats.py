"""
This module defines the 'GameStats' class to track and manage game statistics.

It handles the tracking of game statistics such as score, level, and ship limit.
It also manages high score reading and resets statistics at the start of a new game.
"""


import json
from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """Read the high score when the game starts."""
        path = Path("high_score/high_score.json")
        try:
            contents = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            high_score = 0
        else:
            high_score = json.loads(contents)

        return high_score
