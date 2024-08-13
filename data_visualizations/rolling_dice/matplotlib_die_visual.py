#!/usr/bin/env python3

"""
This module imports the 'Die' class from die.py and defines the 'DieVisual class to plot
the results of rolling two six-sided dice 50_000 times.

The results are displayed in a bar graph using matplotlib.pyplot.
"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from die import Die


NUM_ROLLS = 50_000
FIG_SIZE = (14, 5.5)
DPI = 130
BARS_COLOR = "DarkCyan"
FONT_SIZE_TITLE = 16
FONT_SIZE_AXES_LABELS = 12
FONT_SIZE_TICKS = 8
FONT_SIZE_BARS_LABELS = 8


class DieVisual:
    """A class to visualize the rolls of two D6 dice 50_000 times."""

    def __init__(self) -> None:
        """Make the die instance and generate the visualization."""
        # Make two D6.
        self.die_1: Die = Die()
        self.die_2: Die = Die()

    def make_plot(self) -> None:
        """Make a bar chart of the results of the rolls."""
        poss_results, frequencies = self._analyze_rolls()

        # Make the chart.
        plt.style.use("seaborn-v0_8-muted")
        fig, ax = plt.subplots(figsize=FIG_SIZE, dpi=DPI)
        bars = ax.bar(
            x=poss_results,
            height=frequencies,
            color=BARS_COLOR,
            tick_label=poss_results,
        )

        self._label_bars(ax, bars)
        self._chart_customization(ax)

        plt.show()

    def _analyze_rolls(self) -> tuple[range, list[int]]:
        """Return the possible results of the roll and their frequency."""
        results = self._dice_rolls()

        max_results = self.die_1.num_sides + self.die_2.num_sides
        poss_results = range(1, max_results + 1)

        return poss_results, [results.count(value) for value in poss_results]

    def _dice_rolls(self) -> list[int]:
        """Return the results of the two D6 rolled 50,000 times."""
        return [self.die_1.roll() + self.die_2.roll() for _ in range(NUM_ROLLS)]

    def _label_bars(self, ax: Axes, bars: BarContainer) -> None:
        """Add text labels on top of the bars."""
        for bar_ in bars:
            rolls_result = bar_.get_height()
            if rolls_result > 0:
                ax.text(
                    x=(bar_.get_x() + bar_.get_width() / 2),
                    y=rolls_result,
                    s=str(rolls_result),
                    ha="center",
                    va="bottom",
                    fontsize=FONT_SIZE_BARS_LABELS,
                )

    def _chart_customization(self, ax: Axes) -> None:
        """Customize the chart."""
        ax.set_title(
            "Results of Rolling Two D6 Dice 50,000 Times",
            fontsize=FONT_SIZE_TITLE,
        )
        ax.set_xlabel(
            "Result",
            fontsize=FONT_SIZE_AXES_LABELS,
            labelpad=10,
        )
        ax.set_ylabel(
            "Frequency of Result",
            fontsize=FONT_SIZE_AXES_LABELS,
            labelpad=10,
        )
        ax.grid(axis="y", linestyle="dashed", alpha=0.5)
        ax.set(xlim=(1, 13))
        ax.set_xticks(range(2, 13))
        ax.tick_params(labelsize=FONT_SIZE_TICKS)


if __name__ == "__main__":
    # Make the instance to generate the chart.
    dv = DieVisual()
    dv.make_plot()
