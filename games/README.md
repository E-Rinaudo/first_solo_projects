# Alien Invasion Inspired Games

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

A collection of game projects developed while working through chapters 12-14 of Python Crash Course. These projects are inspired by the "Alien Invasion" game from the book and each includes unique features and enhancements that extend the foundational concepts.
Each game is housed within its own subdirectory. Feel free to explore the READMEs of these projects for detailed information. You will find screenshots and code snippets to help you understand the functionality and design of each game.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Projects Collection](#about-this-projects-collection) •
[Getting Started](#getting-started) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Projects Collection

The projects included in this directory albeit similar to the classic "Alien Invasion" game, were developed with some unique twists. They served as a foundation to explore and enhance my understanding of the concepts covered in the book.

+ **[alien_invasion/][Alien-Invasion-url]**:
A classic arcade-style game where the player controls a spaceship to shoot down waves of aliens descending from the sky. This project includes additional features beyond those covered in the book.

+ **[hungry_fox/][Hungry-Fox-url]**:
A game where the player controls a fox and tries to "kill" farmers.

+ **[sideways_shooter/][Sideways-Shooter-url]**:
A variation of Alien Invasion where the player shoots at enemies that approach horizontally, adding a new dimension to the gameplay.

+ **[sliding_penguin/][Sliding-Penguin-url]**:
A game featuring a penguin that shoots down randomly generated orcas, offering a playful take on the shooting mechanics.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Pygame][Pygame-badge]][Pygame-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]

[back to top](#alien-invasion-inspired-games)

## Getting Started

Each project within this directory can be executed independently.
Follow the steps below to set up and run the projects locally.

> Note:
>
> If you wish to clone the entire repository, please refer to the "Getting Started" section of the README.md in the [first_solo_project][FirstSoloProject-url] repository.

### Prerequisites

Ensure you have [Python][Python-download] and [Git][Git-download] installed on your computer.
Optionally, you may want to use a virtual environment to manage Python dependencies.

### Setup

From your command line:

#### Either Clone This Entire Directory

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

# Specify the directory to include
$ echo "games/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### Or Clone Only a Specific Project Within this Directory

> Note:
>
> To see a list of available projects, refer to [About this Projects Collection](#about-this-projects-collection).

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
$ echo "games/project_name/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to what you cloned
# Choose one of the following based on what you cloned

## If you cloned the entire directory
$ cd games

## If you only cloned a project
$ cd project_name

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
# Run the projects
# Choose one of the following based on what you cloned

## If you cloned the entire directory
$ cd project_name
$ python project_name.py

## If you cloned only a project
$ python project_name.py
```

[back to top](#alien-invasion-inspired-games)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#alien-invasion-inspired-games)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#alien-invasion-inspired-games)

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
[Pygame-badge]: https://img.shields.io/badge/pygame-gold?logo=python&logoColor=white&style=flat
[Pygame-url]: https://www.pygame.org/docs/
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
[Alien-Invasion-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/alien_invasion
[Hungry-Fox-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/hungry_fox
[Sideways-Shooter-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sideways_shooter
[Sliding-Penguin-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sliding_penguin

<!-- MAIN README -->
[FirstSoloProject-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
