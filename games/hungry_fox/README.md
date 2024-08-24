# Hungry Fox

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Hungry Fox** is an arcade-style game where you control a fox that tries to fend off waves of advancing farmers. Dodge their attacks and use your own projectiles to shoot them down. The game uses classic shoot-'em-up mechanics and sound effects to create a fun experience.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

Hungry Fox  is a project I developed while working through chapters 12-14 of Python Crash Course, with additional features and enhancements beyond the standard tutorial. In this game, you control a fox defending itself against waves of farmers. The gameplay focuses on shooting and dodging as you aim to clear each wave and advance through levels of increasing difficulty, ensuring a challenging and fun game. The game includes three levels of difficulty — easy, medium, and hard — so that players can be constantly challenged. A scoring system motivates players to achieve the highest score possible.

The project includes:

Main module:

+ **[hungry_fox.py][Hungry-Fox-url]**: The core game module that manages game initialization, game loop, and overall game state.
  
Other modules:

+ **[bullet.py][Bullet-url]**:  Defines the Bullet class, which handles the fox's projectiles.

+ **[buttons.py][Buttons-url]**: Contains the implementation for various buttons used in the game's UI, such as play, pause, and difficulty selection buttons.

+ **[farmer_bullet.py][Farmer-Bullet-url]**: Handles bullets fired by farmers.

+ **[farmer.py][Farmer-url]**: Defines the Farmer class, representing the enemy characters.

+ **[fox.py][Fox-url]**: Contains the Fox class, which represents the player-controlled character.

+ **[game_stats.py][Game-Stats-url]**:   Tracks and manages game statistics like the player's score, level, and remaining lives.

+ **[scoreboard.py][Scoreboard-url]**:  Displays the player's score, high score, level, and number of fox's lives left on the screen, providing visual feedback of the player's progress.

+ **[settings.py][Settings-url]**: Stores and manages all the game settings, including screen dimensions, speed settings, and other configurable parameters.

+ **[sound_effects.py][Sound-Effects-url]**: Manages the sound effects in the game, such as firing bullets and background music, enhancing the player's experience.

Data files directories:

+ **[high_score/][High-Score-url]**: Contains a file that stores high score data in JSON format.

+ **[images/][Images-url]**: Contains images used in the game for the fox, farmers, and other visual elements.

+ **[sounds/][Sounds-url]**: Includes sound effects and background musics.

+ **[txt_files/][Txt-Files-url]**: Contains two text files used in the game to display the credits and hotkeys.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Pygame][Pygame-badge]][Pygame-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#hungry-fox)

## Getting Started

Follow the steps below to set up and **run this project** locally.

> Note:
>
> If you wish to clone the entire repository, please refer to the "Getting Started" section of the README.md in the [first_solo_project][First-Solo-Project-url] repository.
>
> If you wish to clone the entire games subdirectory, please refer to the "Getting Started" section of the README.md in [games][Games-url].
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
$ echo "games/hungry_fox/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd hungry_fox

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
$ python hungry_fox.py
```

[back to top](#hungry-fox)

## Usage

By running the script, users can control the fox using the arrow keys to shoot at advancing farmers while avoiding their attacks. The game features various difficulty levels and sound effects and players can pause or restart the game using the interface buttons to enhance the experience.

### Code Example

This code snippet from game_stats.py shows how game statistics are initialized.

```py
class GameStats:
    """Track game statistics."""

    def __init__(self, h_fox: "HungryFox") -> None:
        """Initialize game statistics."""
        self.settings: "Settings" = h_fox.settings
        self.reset_stats()
        self.high_score: int = self.read_high_score()

    def reset_stats(self) -> None:
        """Initialize statistics that can change mid game."""
        self.fox_life: int = self.settings.difficulty_settings.fox_limit
        self.score: int = 0
        self.level: int = 1

    def read_high_score(self) -> int:
        """Read the high score when the game starts."""
        path: Path = Path("high_score/high_score.json")
        try:
            contents: str = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            high_score: int = 0
        else:
            high_score = json.loads(contents)

        return high_score
```

### Project GIF

![Hungry Fox GIF][GIF-url]

[back to top](#hungry-fox)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#hungry-fox)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#hungry-fox)

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
[Hungry-Fox-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/hungry_fox.py
[Farmer-Bullet-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/farmer_bullet.py
[Farmer-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/farmer.py
[Bullet-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/bullet.py
[Buttons-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/buttons.py
[Game-Stats-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/game_stats.py
[Scoreboard-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/scoreboard.py
[Settings-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/settings.py
[Fox-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/fox.py
[Sound-Effects-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/hungry_fox/sound_effects.py
[High-Score-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/hungry_fox/high_score
[Images-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/hungry_fox/images
[Sounds-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/hungry_fox/sounds
[Txt-Files-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/hungry_fox/txt_files
[Games-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games

<!-- GIF -->
[GIF-url]: gif/hungry_fox.gif

<!-- MAIN README -->
[First-Solo-Project-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
