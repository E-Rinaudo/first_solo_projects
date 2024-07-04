import matplotlib.pyplot as plt

from molecular_motion_random_walk import MolecularMotion


NUM_POINTS = 50_000
FIG_SIZE = (14, 5.5)
DPI = 130
FONT_SIZE_TITLE = 14
FONT_SIZE_MAIN_POINTS = 80
FONT_SIZE_LEGEND = 8


class MolecularVisual:
    """A class to generate a random walk chart of a pollen grain."""

    def __init__(self):
        """Initialize and generate the random walk."""
        self._random_walk_loop()

    def _random_walk_loop(self):
        """Generate multiple walks based on user input."""
        random_walk = True

        while random_walk:
            self.mm = MolecularMotion(num_points=NUM_POINTS)
            self.mm.make_walk()
            self._make_plot()

            # Prompt the user to make a new walk.
            new_walk = input("\nMake another walk? (y/n) ")

            if new_walk != "y":
                random_walk = False

    def _customize_chart(self, ax):
        """Customize the random walk."""
        # Number of points used to set the color of each point in the walk.
        num_points = range(NUM_POINTS)

        ax.scatter(
            self.mm.x_values,
            self.mm.y_values,
            c=num_points,
            cmap=plt.cm.Reds,
            edgecolors="none",
            s=1,
        )
        ax.set_aspect("equal")
        ax.set_title("Pollen Grain Walk", fontsize=FONT_SIZE_TITLE)

        # Remove the axes for a clearer visualization.
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

    def _make_start_end_points(self, ax):
        """Emphasize the start and end points."""
        ax.scatter(
            0,
            0,
            color="green",
            label="Start Walk",
            edgecolors="none",
            s=FONT_SIZE_MAIN_POINTS,
        )
        ax.scatter(
            self.mm.x_values[-1],
            self.mm.y_values[-1],
            color="blue",
            label="End Walk",
            edgecolors="none",
            s=FONT_SIZE_MAIN_POINTS,
        )

    def _make_legend(self, ax):
        """Make a legend indicating the start and end points."""
        ax.legend(
            loc="upper left",
            scatterpoints=1,
            fancybox=True,
            shadow=True,
            fontsize=FONT_SIZE_LEGEND,
        )

    def _make_plot(self):
        """Create and display the plot."""
        plt.style.use("classic")
        fig, ax = plt.subplots(figsize=FIG_SIZE, dpi=DPI)

        self._customize_chart(ax)
        self._make_start_end_points(ax)
        self._make_legend(ax)

        plt.show()


if __name__ == "__main__":
    # Make the instance and generate the walk.
    pollen_walk = MolecularVisual()
