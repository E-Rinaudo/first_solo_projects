#!/usr/bin/env python3

"""
This module imports the 'RandomWalk' class from the ff_random_walk module
and defines the 'FireflyWalk' class to visualize the walk simulation using Plotly.

The class generates a scatter plot, representing the path of a firefly
on a summer night.
"""

import plotly.graph_objects as go
import numpy as np

from ff_random_walk import RandomWalk


FONT_SCATTER_POINTS: int = 5
FONT_MAIN_POINTS: int = 40
FONT_TITLE: int = 25
FONT_AXES_LABELS: int = 10


class FireflyWalk:  # pylint: disable=R0903
    """A Class to visualize the random walk of a Firefly at night."""

    def __init__(self) -> None:
        """Initialize the Random Walk attributes and generate it."""
        self.rw: RandomWalk = RandomWalk()
        self.rw.make_walk()
        self.fig: go.Figure = None

    def make_plot(self) -> None:
        """Create and display the scatter plot for the random walk."""
        self.fig = go.Figure()

        self._random_walk_trace()
        self._starting_point()
        self._ending_point()
        self._customize_plot()

        self.fig.show()

    def _random_walk_trace(self) -> None:
        """Add the random walk trace."""
        self.fig.add_trace(
            go.Scattergl(
                x=self.rw.x_values,
                y=self.rw.y_values,
                name="Random Walk",
                mode="markers",
                marker={
                    "color": np.arange(self.rw.num_points),
                    "symbol": "star",
                    "size": FONT_SCATTER_POINTS,
                    "colorscale": "Hot",
                },
            )
        )

    def _starting_point(self) -> None:
        """Add the starting point."""
        self.fig.add_trace(
            go.Scatter(
                x=[0],
                y=[0],
                name="Start Point",
                mode="markers",
                marker={
                    "color": "green",
                    "symbol": "circle",
                    "size": FONT_MAIN_POINTS,
                },
            )
        )

    def _ending_point(self) -> None:
        """Add the ending point."""
        self.fig.add_trace(
            go.Scatter(
                x=[self.rw.x_values[-1]],
                y=[self.rw.y_values[-1]],
                name="End Point",
                mode="markers",
                marker={
                    "color": "blue",
                    "symbol": "circle",
                    "size": FONT_MAIN_POINTS,
                },
            )
        )

    def _customize_plot(self) -> None:
        """Customize the plot."""
        self.fig.update_layout(
            plot_bgcolor="black",
            title={
                "text": "Firefly Dance: A Random Walk on a Summer Night",
                "font": {"family": "Arial", "size": FONT_TITLE, "color": "darkred"},
            },
            font={"size": FONT_AXES_LABELS},
            xaxis={
                "showgrid": False,
                "zeroline": False,
                "showticklabels": False,
            },
            yaxis={
                "showgrid": False,
                "zeroline": False,
                "showticklabels": False,
                "scaleanchor": "x",
            },
            legend={"yanchor": "top", "y": 0.99, "xanchor": "left", "x": 0.01},
        )


if __name__ == "__main__":
    # Make the instance and generate the plot.
    fw = FireflyWalk()
    fw.make_plot()
