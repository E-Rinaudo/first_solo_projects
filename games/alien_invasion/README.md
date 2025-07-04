# Alien Invasion

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Alien Invasion** is an arcade-style game where you pilot a spaceship to defend against waves of descending alien invaders. Your mission is to shoot down all the aliens before they reach the bottom of the screen. Aim for the highest score in this classic space shooter.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

Alien Invasion is a project I developed while working through chapters 12-14 of Python Crash Course, with additional features and enhancements beyond the standard tutorial. In this game, you control a spaceship tasked with shooting down a fleet of alien enemies. The game includes three levels of difficulty — easy, medium, and hard — ensuring that players are constantly challenged. A scoring system motivates players to achieve the highest score possible.

The project includes:

Main module:

+ **[alien_invasion.py][Alien-Invasion-url]**: The core game module that manages game initialization, game loop, and overall game state.
  
Other modules:

+ **[alien_bullet.py][Alien-Bullet-url]**: Handles bullets fired by aliens.

+ **[alien.py][Alien-url]**: Defines the Alien class, representing the enemy characters.

+ **[bullet.py][Bullet-url]**: Defines the Bullet class, which handles the ship's projectiles.

+ **[buttons.py][Buttons-url]**: Contains the implementation for various buttons used in the game's UI, such as play, pause, and difficulty selection buttons.

+ **[explosion.py][Explosion-url]**: Manages the explosion effects that occur when an alien is hit by a bullet.

+ **[game_stats.py][Game-Stats-url]**: Tracks and manages game statistics like the player's score, level, and remaining lives.

+ **[scoreboard.py][Scoreboard-url]**: Displays the player's score, high score, level, and number of ships left on the screen, providing visual feedback of the player's progress.

+ **[settings.py][Settings-url]**: Stores and manages all the game settings, including screen dimensions, speed settings, and other configurable parameters.

+ **[ship.py][Ship-url]**: Contains the Ship class, which represents the player-controlled character.

+ **[sound_effects.py][Sound-Effects-url]**: Manages the sound effects in the game, such as firing bullets, alien explosions and background music, enhancing the player's experience.

Data files directories:

+ **[high_score/][High-Score-url]**: Contains a file that stores high score data in JSON format.

+ **[images/][Images-url]**: Contains images used in the game for the player's ship, aliens, and other visual elements.

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
  
[back to top](#alien-invasion)

## Getting Started

Follow the steps below to set up and **run this project** locally.

> Note:
>
> If you wish to clone the entire repository, please refer to the "Getting Started" section of the README.md in the [first-solo-projects][First-Solo-Projects-url] repository.
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
$ git remote add origin https://github.com/E-Rinaudo/first-solo-projects.git

# Enable sparse checkout
$ git config core.sparseCheckout true

# Specify the project to include
$ echo "games/alien_invasion/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd alien_invasion

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
$ python alien_invasion.py
```

[back to top](#alien-invasion)

## Usage

By running the script, users will be able to experience the alien invasion game. Players control a spaceship at the bottom of the screen, moving it left and right to avoid incoming alien bullets and shoot down waves of aliens. Progress through levels, earn points, and achieve high scores by destroying all aliens on the screen. The game features various difficulty levels and sound effects and players can pause or restart the game using the interface buttons to enhance the experience.

### Code Example

This code snippet from alien_invasion.py demonstrates how the game initializes a fleet of aliens.

```py
def _make_fleet(self) -> None:
        """Make the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien_width and one alien_height.
        alien: Alien = Alien(self)
        alien_width: int
        alien_height: int
        alien_width, alien_height = alien.rect.size

        current_x: int = alien_width
        current_y: int = alien_height
        while current_y < (self.settings.screen_height - 5 * alien_height):
            while current_x < (self.settings.screen_width - (2 * alien_width)):
                self._make_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _make_alien(self, x_position: int, y_position: int) -> None:
        """Make an alien and place it in the fleet."""
        new_alien: Alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
```

### Project GIF

![Alien Invasion GIF][GIF-url]

[back to top](#alien-invasion)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first-solo-projects](https://github.com/E-Rinaudo/first-solo-projects/tree/main)

[back to top](#alien-invasion)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#alien-invasion)

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
[Alien-Invasion-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/alien_invasion.py
[Alien-Bullet-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/alien_bullet.py
[Alien-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/alien.py
[Bullet-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/bullet.py
[Buttons-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/buttons.py
[Explosion-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/explosion.py
[Game-Stats-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/game_stats.py
[Scoreboard-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/scoreboard.py
[Settings-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/settings.py
[Ship-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/ship.py
[Sound-Effects-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/games/alien_invasion/sound_effects.py
[High-Score-url]: https://github.com/E-Rinaudo/first-solo-projects/tree/main/games/alien_invasion/high_score
[Images-url]: https://github.com/E-Rinaudo/first-solo-projects/tree/main/games/alien_invasion/images
[Sounds-url]: https://github.com/E-Rinaudo/first-solo-projects/tree/main/games/alien_invasion/sounds
[Txt-Files-url]: https://github.com/E-Rinaudo/first-solo-projects/tree/main/games/alien_invasion/txt_files
[Games-url]: https://github.com/E-Rinaudo/first-solo-projects/tree/main/games

<!-- GIF -->
[GIF-url]: gif/alien_invasion.gif

<!-- MAIN README -->
[First-Solo-Projects-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
