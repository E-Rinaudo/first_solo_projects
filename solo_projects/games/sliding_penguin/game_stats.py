import json
from pathlib import Path


class GameStats:
    """Track statistics for the game."""

    def __init__(self, s_penguin):
        """Initialize statistics."""
        self.settings = s_penguin.settings
        self.reset_stats()
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change mid game."""
        self.penguin_life = self.settings.penguin_limit
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
