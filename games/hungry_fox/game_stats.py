#!/usr/bin/env python3

"""
This module defines the 'GameStats' class to track and manage game statistics.

It handles the tracking of game statistics such as score, level, and fox life.
It also manages high score reading and resets statistics at the start of a new game.
"""

import json
from pathlib import Path


class GameStats:
    """Track game statistics."""

    def __init__(self, h_fox):
        """Initialize game statistics."""
        self.settings = h_fox.settings
        self.reset_stats()
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change mid game."""
        self.fox_life = self.settings.fox_limit
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
