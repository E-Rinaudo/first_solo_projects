# Molecular Motion

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Molecular Motion** visualizes the random movement of a pollen grain on a drop of water. By simulating the pollen's path through a series of random steps, this project offers a visualization of molecular motion. The simulation is implemented using Matplotib, and the results are presented through scatter plots.

This project was developed while working through chapters 15 of Python Crash Course.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

Molecular Motion demonstrates the random walk of a pollen grain on a water surface. The MolecularMotion class in molecular_motion_random_walk.py creates a series of random steps for the pollen grain, resulting in a path that is visualized using Matplotlib in molecular_motion_visual.py. The visualization allows users to generate and view multiple random walks, offering insight into the nature of molecular motion.

The project includes two modules:

+ **[molecular_motion_visual.py][Molecular-Motion-Visual-url]**:
Visualizes the random walk using Matplotlib, creating a scatter plot that represents the path of the pollen grain with customizable aesthetics. It features a loop to create multiple scatter plots, emphasizing the start and end points of each walk.

+ **[molecular_motion_random_walk.py][Molecular-Motion-Random-Walk-url]**:
Defines the MolecularMotion class, which simulates the random walk of the pollen grain, generating a path with random directions and distances.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Matplotlib][Matplotlib-badge]][Matplotlib-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#molecular-motion)

## Getting Started

Follow the steps below to set up and **run this project** locally.

> Note:
>
> If you wish to clone the entire repository, please refer to the "Getting Started" section of the README.md in the [first_solo_project][First-Solo-Project-url] repository.
>
> If you wish to clone the entire data visualizations subdirectory, please refer to the "Getting Started" section of the README.md in [data_visualizations][Data-Visualizations-url].
>
> If you wish to clone the entire random_walks subdirectory, please refer to the "Getting Started" section of the README.md in [random_walks][Random-Walks-url].

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
$ git remote add origin https://github.com/E-Rinaudo/first_solo_projects.git

# Enable sparse checkout
$ git config core.sparseCheckout true

# Specify the project to include
$ echo "data_visualizations/random_walks/molecular_motion/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd molecular_motion

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
$ python molecular_motion_visual.py
```

[back to top](#molecular-motion)

## Usage

By running this program, users can visualize the path of a pollen grain moving randomly on a water surface. The script generates a scatter plot of the pollen's trajectory, with the option to create and view multiple random walks. The visualization highlights the start and end points of the walk and uses color to represent the sequence of steps.

You will be prompted to generate multiple walks, with each new walk visualized in a new plot.

### Code Example

This code snippet from molecular_motion_visual.py demonstrates how the MolecularVisual class generates and visualizes the random walk.

```py
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
```

### Project Screenshot

![Molecular Motion Screenshot][Screenshot-url]

[back to top](#molecular-motion)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#molecular-motion)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#molecular-motion)

---

**Happy coding!**

<!-- SHIELDS -->
[license-shield]: https://img.shields.io/github/license/E-Rinaudo/first_solo_projects.svg?style=flat
[license-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/LICENSE.txt
[Gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white
[Gmail-url]: mailto:enricorinaudo91@gmail.com

<!-- BADGES -->
[Python-badge]: https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54&style=flat
[Python-url]: https://docs.python.org/3/
[VSCode-badge]: https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=fff&style=flat
[VSCode-url]: https://code.visualstudio.com/docs
[Matplotlib-badge]: https://img.shields.io/badge/Matplotlib-%23FF7F0E?style=flat&logo=matplotlib&logoColor=white
[Matplotlib-url]: https://matplotlib.org/stable/users/index.html
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
[Molecular-Motion-Visual-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/random_walks/firefly_random_walk/ff_random_walk_visual.py
[Molecular-Motion-Random-Walk-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/random_walks/molecular_motion/molecular_motion_random_walk.py
[Data-Visualizations-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations
[Random-Walks-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/random_walks

<!-- SCREENSHOT -->
[Screenshot-url]: screenshot/molecular_motion.png

<!-- MAIN README -->
[First-Solo-Project-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
