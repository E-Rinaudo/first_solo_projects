# Rolling Dice

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Rolling Dice** is a project that simulates rolling two six-sided dice 50,000 times and visualizes the results. It provides a way to see how often each possible outcome occurs, with a bar chart generated using Matplotlib.

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

The primary aim of this project is to analyze and display the frequency of each possible result of rolling two six-sided dice 50,000 times using a bar chart.

The project includes two modules:

+ **[matplotlib_die_visual.py][Matplotlib-Die-Visual-url]**:
Imports the Die class (die.py) and defines the DieVisual class that takes care of the visualization and plots the results.

+ **[die.py][Die-url]**:
Defines the Die class to represent a six-sided die and includes functionality for rolling the die.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Matplotlib][Matplotlib-badge]][Matplotlib-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#rolling-dice)

## Getting Started

Follow the steps below to set up and **run this project** locally.

> Note:
>
> If you wish to clone the entire repository, please refer to the "Getting Started" section of the README.md in the [first_solo_project][First-Solo-Project-url] repository.
>
> If you wish to clone the entire data visualizations subdirectory, please refer to the "Getting Started" section of the README.md in [data_visualizations][Data-Visualizations-url].
>

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
$ echo "data_visualizations/rolling_dice/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd rolling_dice

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
$ python matplotlib_die_visual.py
```

[back to top](#rolling-dice)

## Usage

By executing the script, a bar chart will be displayed, showing how often each result occurred in the simulated rolls.

### Code Example

This code snippet from matplotlib_die_visual.py demonstrates how the DieVisual class is used to create a bar chart of the dice roll results.

```py
class DieVisual:  # pylint: disable=R0903
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
        fig: Figure  # pylint: disable=W0612
        ax: plt.Axes
        fig, ax = plt.subplots(figsize=FIG_SIZE, dpi=DPI)
        bars: BarContainer = ax.bar(
            x=poss_results,
            height=frequencies,
            color=BARS_COLOR,
            tick_label=poss_results,
        )

        self._label_bars(ax, bars)
        self._chart_customization(ax)

        plt.show()
```

### Project Screenshot

![Rolling Dice Screenshot][Screenshot-url]

[back to top](#rolling-dice)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#rolling-dice)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#rolling-dice)

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
[Matplotlib-Die-Visual-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/rolling_dice/matplotlib_die_visual.py
[Die-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/rolling_dice/die.py
[Data-Visualizations-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations

<!-- SCREENSHOT -->
[Screenshot-url]: screenshot/rolling_dice.png

<!-- MAIN README -->
[First-Solo-Project-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
