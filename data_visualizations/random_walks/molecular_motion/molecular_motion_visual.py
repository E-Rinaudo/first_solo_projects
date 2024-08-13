#!/usr/bin/env python3

"""
This module imports the 'MolecularMotion' class from molecular_motion_random_walk.py
and defines the 'MolecularVisual' class to visualize the walk using Matplotlib.

The 'MolecularVisual' uses a loop to generate as many scatter plots as the user desires,
representing the path of a pollen grain on a drop of water.
"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from molecular_motion_random_walk import MolecularMotion


NUM_POINTS = 50_000
FIG_SIZE = (14, 5.5)
DPI = 130
FONT_SIZE_TITLE = 14
FONT_SIZE_MAIN_POINTS = 100
FONT_SIZE_LEGEND = 8


class MolecularVisual:
    """A class to visualize a random walk chart of a pollen grain."""

    def __init__(self) -> None:
        """Initialize and generate the random walk."""
        self.mm: MolecularMotion = MolecularMotion(NUM_POINTS)

    def random_walk_loop(self) -> None:
        """Generate multiple walks based on user input."""
        random_walk = True

        while random_walk:
            self.mm = MolecularMotion(NUM_POINTS)
            self.mm.make_walk()
            self._make_plot()

            # Prompt the user to make a new walk.
            new_walk = input("\nMake another walk? (y/n) ")

            if new_walk != "y":
                random_walk = False

    def _make_plot(self) -> None:
        """Create and display the plot."""
        plt.style.use("classic")
        fig, ax = plt.subplots(figsize=FIG_SIZE, dpi=DPI)

        self._customize_chart(ax)
        self._make_start_end_points(ax)
        self._make_legend(ax)

        plt.show()

    def _customize_chart(self, ax: Axes) -> None:
        """Customize the random walk."""
        # Number of points used to set the color of each point in the walk.
        num_points = range(NUM_POINTS)

        ax.scatter(
            self.mm.x_values,
            self.mm.y_values,
            c=num_points,
            cmap="viridis",
            edgecolors="none",
            s=1,
        )
        ax.set_aspect("equal")
        ax.set_title("Pollen Grain Walk", fontsize=FONT_SIZE_TITLE)

        # Remove the axes for a clearer visualization.
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

    def _make_start_end_points(self, ax: Axes) -> None:
        """Emphasize the start and end points."""
        ax.scatter(
            0,
            0,
            color="red",
            label="Start Walk",
            edgecolors="none",
            s=FONT_SIZE_MAIN_POINTS,
        )
        ax.scatter(
            self.mm.x_values[-1],
            self.mm.y_values[-1],
            color="violet",
            label="End Walk",
            edgecolors="none",
            s=FONT_SIZE_MAIN_POINTS,
        )

    def _make_legend(self, ax: Axes) -> None:
        """Make a legend indicating the start and end points."""
        ax.legend(
            loc="upper left",
            scatterpoints=1,
            fancybox=True,
            shadow=True,
            fontsize=FONT_SIZE_LEGEND,
        )


if __name__ == "__main__":
    # Make the instance and generate the walk.
    pollen_walk = MolecularVisual()
    pollen_walk.random_walk_loop()
