import matplotlib.pyplot as plt

from molecular_motion_random_walk import MolecularMotion


class MolecularVisual:
    """A class to generate the chart of the pollen grain walk."""

    def __init__(self):
        """Initialize and generate random walks."""
        self._random_walk_loop()

    def _random_walk_loop(self):
        """Generate multiple walks based on user input."""
        random_walk = True

        while random_walk:
            self.mm = MolecularMotion(num_points=50000)
            self.mm.make_walk()
            self._make_plot()

            # Prompt the user to make a new walk.
            new_walk = input("\nMake another walk? (y/n) ")

            if new_walk != 'y':
                random_walk = False

    def _make_plot(self):
        """Create and display the plot."""
        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(14, 5.5), dpi=130)

        # Number of points used to set the color of each point in the walk.
        num_points = range(self.mm.num_points)
        ax.scatter(self.mm.x_values, self.mm.y_values, c=num_points, 
            cmap=plt.cm.Reds, edgecolors='none', s=1)
        ax.set_aspect('equal')
        ax.set_title("Pollen Grain Walk", fontsize=14)

        # Emphasize the start and end points.
<<<<<<< HEAD
        ax.scatter(0, 0, color='green', label='Start Walk', edgecolors='none', s=80)
=======
        ax.scatter(0, 0, color='green', label='Start Walk', edgecolors='none', 
            s=80)
>>>>>>> 1e8c2f8 (Refactor the molecular motion project.)
        ax.scatter(self.mm.x_values[-1], self.mm.y_values[-1], color='blue', 
                   label='End Walk', edgecolors='none', s=80)

        # Make a legend indicating the start and end points.
        ax.legend(loc='upper left', scatterpoints=1, fancybox=True, shadow=True, 
            fontsize=8)

        # Remove the axes for a clearer visualization.
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        plt.show()

if __name__ == '__main__':
    # Make the instance and generate the walk.
    pollen_walk = MolecularVisual()