# First Solo Projects in Python

[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

A collection of my first Python projects that I completed independently while studying Python Crash Course by Eric Matthes.
Each subdirectory is dedicated to a specific project category.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Repository](#about-this-repository) •
[Getting Started](#getting-started) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Repository

Welcome to my "first_solo_projects" repository.

Here, you'll find a variety of projects, from practical applications like a spaced repetition reminder and a fitness interval timer to interactive games and data visualizations. Each project reflects the skills and concepts I developed while studying Python Crash Course.

Feel free to explore the READMEs of the subdirectories for detailed information about the projects. I have included additional resources such code snippets and screenshots to provide a clearer understanding of each project functionality.

+ **[data_visualizations/][Data-Visualizations-url]**:
A collection of projects focused on visualizing data using Matplotlib and Plotly.

+ **[games/][Games-url]**:
A collection of interactive games inspired by the "Alien Invasion" game of Python Crash Course, each with unique features.

+ **[hurricane_clock/][Hurricane-Clock-url]**:
A project simulating timed exercise intervals for a fitness program by [Athleanx][Athleanx-url].

+ **[spaced_repetition_reminder/][Spaced-Repetition-Reminder-url]**:
A tool that generates reminders for study tasks using the spaced repetition method.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#first-solo-projects-in-python)

## Getting Started

Each project within this repository can be executed independently.
Follow the steps below to set up and run the projects locally.

### Prerequisites

Ensure you have [Python][Python-download] and [Git][Git-download] installed on your computer.
Optionally, you may want to use a virtual environment to manage Python dependencies.

### Setup

From your command line:

#### Either Clone the Entire Repository

```bash
# Clone the entire repository
$ git clone https://github.com/E-Rinaudo/first_solo_projects.git

# Or Clone the entire repository using GitHub CLI
$ gh repo clone E-Rinaudo/first_solo_projects
```

#### Or Clone Only a Specific Subdirectory

> Note:
>
> To see a list of available subdirectories, refer to [About this Repository](#about-this-repository).

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

# Specify the subdirectory to include
$ echo "subdirectory_name/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### Or Clone Only a Specific Project Within a Subdirectory

> Note:
>
> This method is applicable only for "data_visualizations" or "games".
> For "hurricane_clock" or "spaced_repetition_reminder" please use the method above to clone the relevant subdirectory.
>
> To see a list of available subdirectories, refer to [About this Repository](#about-this-repository).

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
$ echo "subdirectory_name/project_name/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to what you cloned
# Choose one of the following based on what you cloned

## If you cloned the entire repository
$ cd first_solo_projects

## If you only cloned a subdirectory
$ cd subdirectory_name

## If you only cloned a project of either data_visualizations or games
$ cd project_name

# Create a virtual environment
$ python -m venv venv

# Activate the virtual environment

## On macOS/Linux
$ source venv/bin/activate

## On Windows with CMD
$ .\venv\Scripts\activate.bat

## On Windows With PowerShell.
.\venv\Scripts\activate.ps1

## On Windows With Unix Like Shells (e.g. Git Bash CLI).
source venv/Scripts/activate

# Install dependencies
$ pip install -r requirements.txt
```

#### Finally

```bash
# Run the projects
# Choose one of the following based on what you cloned

## If you cloned the entire repository
$ cd subdirectory_name/project_name
$ python project_name_main.py

## If you cloned the entire subdirectory of either data_visualizations or games
$ cd project_name
$ python project_name_main.py

## If you cloned either hurricane_clock or spaced_repetition_reminder or a project within either data_visualizations or games
$ python project_name_main.py
```

[back to top](#first-solo-projects-in-python)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#first-solo-projects-in-python)

---

**Happy coding!**

<!-- SHIELDS -->
[stars-shield]: https://img.shields.io/github/stars/E-Rinaudo/first_solo_projects.svg?style=flat
[stars-url]: https://github.com/E-Rinaudo/first_solo_projects/stargazers
[license-shield]: https://img.shields.io/github/license/E-Rinaudo/first_solo_projects.svg?style=flat
[license-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/LICENSE.txt
[Gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white
[Gmail-url]: mailto:enricorinaudo91@gmail.com

<!-- BADGES -->
[Python-badge]: https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54&style=flat
[Python-url]: https://docs.python.org/3/
[VSCode-badge]: https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=fff&style=flat
[VSCode-url]: https://code.visualstudio.com/docs
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
[Data-Visualizations-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations
[Games-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games
[Hurricane-Clock-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/hurricane_clock
[Spaced-Repetition-Reminder-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/spaced_repetition_reminder

<!-- MISCELLANEA -->
[Athleanx-url]: https://athleanx.com/

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
