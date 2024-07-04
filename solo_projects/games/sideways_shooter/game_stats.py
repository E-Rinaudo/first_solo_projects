import json
from pathlib import Path


class GameStats:
    """A class to track game statistics."""

    def __init__(self, s_shooter):
        """Initialize game statistics."""
        self.settings = s_shooter.settings
        self.reset_stats()
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change mid game."""
        self.hero_life = self.settings.hero_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """Read the high score when the game starts."""
        path = Path("high_score/high_score.json")
        try:
            contents = path.read_text()
        except FileNotFoundError:
            high_score = 0
        else:
            high_score = json.loads(contents)

        return high_score
