#!/usr/bin/env python3

"""
This module defines the 'MolecularMotion' class to create a random walk of 5_000 steps.
Each step is taken in a random direction and with a random distance.
"""

from random import choice


class MolecularMotion:  # pylint: disable=R0903
    """A class to generate a random walk of a pollen grain on water."""

    def __init__(self, num_points: int = 5000) -> None:
        """Initialize the random walk attributes."""
        self.num_points = num_points

        # The walk starts at (0, 0).
        self.x_values: list[int] = [0]
        self.y_values: list[int] = [0]

    def make_walk(self) -> None:
        """Generate the random walk."""
        while len(self.x_values) < self.num_points:
            x_step = self._get_step()
            y_step = self._get_step()

            # Discard steps that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            x: int = self.x_values[-1] + x_step
            y: int = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self) -> int:
        """Determine direction and distance of each step."""
        direction: int = choice([1, -1])
        distance: int = choice([0, 1, 2, 3, 4, 5])
        step: int = direction * distance

        return step
