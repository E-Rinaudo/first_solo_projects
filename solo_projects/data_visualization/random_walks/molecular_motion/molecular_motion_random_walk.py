from random import choice


class MolecularMotion:
    """A class to generate a random walk of a pollen grain on water."""

    def __init__(self, num_points=5000):
        """Initialize the random walk attributes."""
        self.num_points = num_points

        # The walk starts at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def make_walk(self):
        """Generate the random walk."""
        while len(self.x_values) < self.num_points:
            x_step = self._get_step()
            y_step = self._get_step()

            # Discard steps that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self):
        """Determine direction and distance of each step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5])
        step = direction * distance

        return step
