# Sideways Shooter

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Sideways Shooter** is a retro-inspired arcade game where you take on the role of a hero battling waves of alien invaders. With varying difficulty levels, your mission is to shoot at enemies while dodging their projectiles. Customize your experience by selecting different difficulty settings, and aim for the highest score.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

Sideways Shooter is a project I developed while studying chapters 12-14 of Python Crash Course, incorporating additional features and enhancements beyond the standard tutorial. In this game, players control a hero who is stationed on the left side of the screen and must move vertically to avoid alien bullets while shooting down enemies that appear from the right side at random intervals. The game includes three levels of difficulty — easy, medium, and hard — and engaging sound effects, providing an exciting challenge for fans of classic arcade shooters.

The project includes:

Main module:

+ **[sideways_shooter.py][Sideways-Shooter-url]**: The core game module that manages game initialization, game loop, and overall game state.
  
Other modules:

+ **[alien_bullet.py][Alien-Bullet-url]**: Handles bullets fired by aliens.

+ **[alien.py][Alien-url]**: Defines the Alien class, representing the enemy characters.

+ **[bullet.py][Bullet-url]**: Defines the Bullet class, which handles the hero's projectiles.

+ **[buttons.py][Buttons-url]**: Contains the implementation for various buttons used in the game's UI, such as play, pause, and difficulty selection buttons.

+ **[explosion.py][Explosion-url]**: Manages the explosion effects that occur when an alien is hit by a bullet.

+ **[game_stats.py][Game-Stats-url]**:  Tracks and manages game statistics like the player's score, level, and remaining lives.

+ **[hero.py][Hero-url]**: Contains the Hero class, which represents the player-controlled character.

+ **[scoreboard.py][Scoreboard-url]**: Displays the player's score, high score, level, and number of hero's lives left on the screen, providing visual feedback of the player's progress.

+ **[settings.py][Settings-url]**: Stores and manages all the game settings, including screen dimensions, speed settings, and other configurable parameters.

+ **[sound_effects.py][Sound-Effects-url]**: Manages the sound effects in the game, such as firing bullets, alien explosions and background music, enhancing the player's experience.

Data files directories:

+ **[high_score/][High-Score-url]**: Contains a file that stores high score data in JSON format.

+ **[images/][Images-url]**: Contains images used in the game for the hero, aliens, and other visual elements.

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
  
[back to top](#sideways-shooter)

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
$ echo "games/sideways_shooter/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd sideways_shooter

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
$ python sideways_shooter.py
```

[back to top](#sideways-shooter)

## Usage

By running the script, users will be able to experience a retro space shooter game. Progress through levels, earn points, and achieve high scores by destroying all aliens on the screen. The game features various difficulty levels and sound effects and players can pause or restart the game using the interface buttons to enhance the experience.

### Code Example

This code snippet from sideways_shooter.py demonstrates how the SidewaysShooter class handles the difficulty selection.

```py
def _choose_difficulty(self) -> tuple[bool, bool, bool]:
        """Store attributes for the click of the difficulty levels buttons."""
        easy_clicked: bool = self._is_button_clicked(self.game_buttons.easy_diff_button)
        medium_clicked: bool = self._is_button_clicked(
            self.game_buttons.medium_diff_button
        )
        hard_clicked: bool = self._is_button_clicked(self.game_buttons.hard_diff_button)

        return easy_clicked, medium_clicked, hard_clicked

def _handle_difficulty_selection(
        self, easy_clicked: bool, medium_clicked: bool, hard_clicked: bool
    ) -> None:
        """Handle the difficulty selection based on which button is clicked."""
        if self._are_credits_and_hotkeys_not_displayed():
            if easy_clicked:
                self._easy_difficulty()
            elif medium_clicked:
                self._medium_difficulty()
            elif hard_clicked:
                self._hard_difficulty()
```

### Project GIF

![Sideways Shooter GIF][GIF-url]

[back to top](#sideways-shooter)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#sideways-shooter)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#sideways-shooter)

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
[Sideways-Shooter-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/sideways_shooter.py
[Alien-Bullet-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/alien_bullet.py
[Alien-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/alien.py
[Bullet-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/bullet.py
[Buttons-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/buttons.py
[Explosion-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/explosion.py
[Game-Stats-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/game_stats.py
[Scoreboard-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/scoreboard.py
[Settings-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/settings.py
[Hero-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/hero.py
[Sound-Effects-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/games/sideways_shooter/sound_effects.py
[High-Score-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sideways_shooter/high_score
[Images-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sideways_shooter/images
[Sounds-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sideways_shooter/sounds
[Txt-Files-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games/sideways_shooter/txt_files
[Games-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/games

<!-- GIF -->
[GIF-url]: gif/sideways_shooter.gif

<!-- MAIN README -->
[First-Solo-Project-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
