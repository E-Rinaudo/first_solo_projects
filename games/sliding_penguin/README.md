# Sliding Penguin

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Sliding Penguin** is a fun and dynamic 2D game where you control a penguin at the bottom of the screen, shooting down orcas that appear randomly from the top. Dodge the incoming attacks and aim carefully to eliminate the orcas. As the game progresses, the difficulty will increase and you will have to sharpen your skills to advance through tougher levels.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

Sliding Penguin is a project I developed while working through chapters 12-14 of Python Crash Course, featuring added functionality beyond the standard tutorial. In this game, players guide a penguin located at the bottom of the screen, aiming to shoot orcas that spawn randomly from the top. The game includes three levels of difficulty (easy, medium, and hard), a scoring system, and dynamic game states such as playing, paused, and game over. Sliding Penguin offers a playful take on the shooting genre.

The project includes:

Main module:

+ **[sliding_penguin.py][Sliding-Penguin-url]**: The core game module that manages game initialization, game loop, and overall game state.
  
Other modules:

+ **[bullet.py][Bullet-url]**: Defines the Bullet class, which handles the penguin's projectiles.

+ **[buttons.py][Buttons-url]**: Contains the implementation for various buttons used in the game's UI, such as play, pause, and difficulty selection buttons.

+ **[game_stats.py][Game-Stats-url]**:  Tracks and manages game statistics like the player's score, level, and remaining lives.

+ **[orca_bullet.py][Orca-Bullet-url]**: Handles bullets fired by orcas.

+ **[orca.py][Orca-url]**: Defines the Orca class, representing the enemy characters.

+ **[penguin.py][Penguin-url]**: Contains the Penguin class, which represents the player-controlled character.

+ **[scoreboard.py][Scoreboard-url]**: Displays the player's score, high score, level, and number of penguins' lives left on the screen, providing visual feedback of the player's progress.

+ **[settings.py][Settings-url]**: Stores and manages all the game settings, including screen dimensions, speed settings, and other configurable parameters.

+ **[sound_effects.py][Sound-Effects-url]**: Manages the sound effects in the game, such as firing bullets and background music, enhancing the player's experience.

Data files directories:

+ **[high_score/][High-Score-url]**: Contains a file that stores high score data in JSON format.

+ **[images/][Images-url]**: Contains images used in the game for the penguin, orcas, and other visual elements.

+ **[sounds/][Sounds-url]**:    Includes sound effects and background musics.

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
  
[back to top](#sliding-penguin)

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
$ echo "games/sliding_penguin/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd sliding_penguin

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
$ python sliding_penguin.py
```

[back to top](#sliding-penguin)

## Usage

By running the script, users will be able to experience the sliding penguin game. Use the keyboard to control the penguin, shoot at orcas to score points. The game features various difficulty levels and sound effects and players can pause or restart the game using the interface buttons to enhance the experience.

### Code Example

This code snippet from sliding_penguin.py shows how the SlidingPenguin class is initialized and how the main game loop operates:

```py
class SlidingPenguin:  # pylint: disable = R0902, R0903
    """Class to manage the game and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and generate game resources."""
        self.game_state: GameState = GameState()
        pygame.init()  # pylint: disable=E1101
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.settings: Settings = Settings()
        self.sounds: Sound = Sound()
        self._make_screen()
        self.stats: GameStats = GameStats(self)
        self.game_buttons: GameButtons = GameButtons(self)
        self.sb: Scoreboard = Scoreboard(self)
        self.penguin: Penguin = Penguin(self)
        self._sprite_groups()
        
    def run_game(self) -> None:
        """Main loop for the game."""
        while True:
            self._check_events()

            if (self.game_state.game_active) and (not self.game_state.game_paused):
                self._make_mouse_invisible()
                self._make_fleet()
                self.penguin.update()
                self._update_bullets()
                self._update_orcas()
                self._fire_orca_bullet()
                self._update_orca_bullets()

            self._update_screen()
            self.clock.tick(60)
```

### Project GIF

![Sliding Penguin GIF][GIF-url]

[back to top](#sliding-penguin)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#sliding-penguin)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#sliding-penguin)

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
[Sliding-Penguin-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/sliding_penguin.py
[Orca-Bullet-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/orca_bullet.py
[Orca-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/orca.py
[Bullet-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/bullet.py
[Buttons-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/buttons.py
[Game-Stats-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/game_stats.py
[Scoreboard-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/scoreboard.py
[Settings-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/settings.py
[Penguin-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/penguin.py
[Sound-Effects-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sliding_penguin/sound_effects.py
[High-Score-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sliding_penguin/high_score
[Images-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sliding_penguin/images
[Sounds-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sliding_penguin/sounds
[Txt-Files-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sliding_penguin/txt_files
[Games-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games

<!-- GIF -->
[GIF-url]: gif/sliding_penguin.gif

<!-- MAIN README -->
[First-Solo-Project-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
