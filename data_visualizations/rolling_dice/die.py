#!/usr/bin/env python3

"""
This module defines the 'Die' class to represent a die with 6 sides.
The die is rolled to obtain a random number between 1 and the number of sides.
"""

from random import randint


class Die:
    """A class to represent a die."""

    def __init__(self, num_sides=6):
        """Initialize the die attributes."""
        self.num_sides = num_sides

    def roll(self):
        """Return the result of the roll of a die."""
        return randint(1, self.num_sides)
