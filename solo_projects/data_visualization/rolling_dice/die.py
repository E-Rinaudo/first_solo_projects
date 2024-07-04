from random import randint


class Die:
    """A class to represent a die."""

    def __init__(self, num_sides=6):
        """Initialize the die attributes."""
        self.num_sides = num_sides

    def roll(self):
        """Return the result of the roll of a die."""
        return randint(1, self.num_sides)
