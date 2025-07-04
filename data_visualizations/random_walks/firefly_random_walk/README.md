# Firefly Random Walk

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Firefly Random Walk** simulates the journey of a firefly on a summer night through random movements in a two-dimensional space. Using the FireflyWalk class, this project visualizes the firefly's path with a scatter plot that captures its flight.

This project was developed while working through chapter 15 of Python Crash Course.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

This project is designed to create a visually captivating representation of a firefly's random walk. It uses the RandomWalk class to simulate the firefly's journey, which is then plotted by the FireflyWalk class. This visualization is accomplished with Plotly, resulting in a scatter plot that highlights the firefly's path, starting and ending points, against a black background. Each step in the walk is represented by a star symbol with varying shades of orange, evoking the feel of a summer night.

The project includes two modules:

+ **[ff_random_walk_visual.py][FF-Random-Walk-Visual-url]**:
Handles the visualization of the firefly's random walk using Plotly. It generates a scatter plot that showcases the firefly's path with customizable aesthetics.

+ **[ff_random_walk.py][FF-Random-Walk-url]**:
Defines the RandomWalk class, responsible for generating the random walk of 5,000 steps, simulating the firefly's movements.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Plotly][Plotly-badge]][Plotly-url]
+ [![Numpy][Numpy-badge]][Numpy-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#firefly-random-walk)

## Getting Started

Follow the steps below to set up and **run this project** locally.

> Note:
>
> If you wish to clone the entire repository, please refer to the "Getting Started" section of the README.md in the [first-solo-projects][First-Solo-Projects-url] repository.
>
> If you wish to clone the entire data visualizations subdirectory, please refer to the "Getting Started" section of the README.md in [data_visualizations][Data-Visualizations-url].
>
> If you wish to clone the entire random walks subdirectory, please refer to the "Getting Started" section of the README.md in [random_walks][Random-Walks-url].

### Prerequisites

Ensure you have [Python][Python-download] and [Git][Git-download] installed on your computer.
Optionally, you may want to use a virtual environment to manage Python dependencies.

### Setup

From your command line:

#### Clone Only This Specific Project

```bash
# Make a directory
$ mkdir <repo>
$ cd <repo>

# Initialize a new Git repository
$ git init

# Add the remote repository
$ git remote add origin https://github.com/E-Rinaudo/first-solo-projects.git

# Enable sparse checkout
$ git config core.sparseCheckout true

# Specify the project to include
$ echo "data_visualizations/random_walks/firefly_random_walk/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd firefly_random_walk

# Create a virtual environment
$ python -m venv venv

# Activate the virtual environment

## On macOS/Linux
$ source venv/bin/activate

## On Windows with CMD
$ .\venv\Scripts\activate.bat

## On Windows With Power shell.
.\venv\Scripts\activate.ps1

## On Windows With Unix Like Shells (e.g. Git Bash CLI).
source venv/Scripts/activate

# Install dependencies
$ pip install -r requirements.txt
```

#### Finally

```bash
# Run the project
$ python ff_random_walk_visual.py
```

[back to top](#firefly-random-walk)

## Usage

By running this program, users can generate an interactive scatter plot showing the firefly's path across 5,000 random steps. The plot will open in your default web browser, displaying the trajectory with points representing the firefly's movement, starting point in green, and ending point in blue.

### Code Example

This code snippet from ff_random_walk_visual.py demonstrates how the FireflyWalk class creates and customizes the plot.

```py
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
```

### Project Screenshot

![Firefly Walk Screenshot][Screenshot-url]

[back to top](#firefly-random-walk)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first-solo-projects](https://github.com/E-Rinaudo/first-solo-projects/tree/main)

[back to top](#firefly-random-walk)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#firefly-random-walk)

---

**Happy coding!**

<!-- SHIELDS -->
[license-shield]: https://img.shields.io/github/license/E-Rinaudo/first-solo-projects.svg?style=flat
[license-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/LICENSE.txt
[Gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white
[Gmail-url]: mailto:enricorinaudo91@gmail.com

<!-- BADGES -->
[Python-badge]: https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54&style=flat
[Python-url]: https://docs.python.org/3/
[VSCode-badge]: https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=fff&style=flat
[VSCode-url]: https://code.visualstudio.com/docs
[Plotly-badge]: https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white&style=flat
[Plotly-url]: https://plotly.com/python/
[Numpy-badge]: https://img.shields.io/badge/numpy-%234B8BBE?style=flat&logo=numpy&logoColor=white
[Numpy-url]: https://numpy.org/doc/stable/
[Mypy-badge]: https://img.shields.io/badge/mypy-checked-blue?style=flat
[Mypy-url]: https://mypy.readthedocs.io/
[Black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[Black-url]: https://black.readthedocs.io/en/stable/
[Pylint-badge]: https://img.shields.io/badge/linting-pylint-yellowgreen?style=flat
[Pylint-url]: https://pylint.readthedocs.io/
[Ruff-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[Ruff-url]: https://docs.astral.sh/ruff/tutorial/
[Flake8-badge]: https://img.shields.io/badge/linting-flake8-blue?style=flat
[Flake8-url]: https://flake8.pycqa.org/en/latest/

<!-- PROJECTS LINKS -->
[FF-Random-Walk-Visual-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/random_walks/firefly_random_walk/ff_random_walk_visual.py
[FF-Random-Walk-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/random_walks/firefly_random_walk/ff_random_walk.py
[Data-Visualizations-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations
[Random-Walks-url]: https://github.com/E-Rinaudo/first-solo-projects/tree/main/data_visualizations/random_walks

<!-- SCREENSHOT -->
[Screenshot-url]: screenshot/firefly.png

<!-- MAIN README -->
[First-Solo-Projects-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
