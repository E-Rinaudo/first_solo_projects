# Athleanx Hurricane Workout Clock

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Hurricane Clock** is a program designed to simulate timed exercise intervals for the Hurricane Hypertrophy month of NXT in [Athleanx][Athleanx-url], a popular fitness program created by Jeff Cavaliere.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

This project provides a structured interval training experience by prompting the user for workout details. It then runs a clock for each set, alternating between 20-second and 40-second intervals with sound cues for timing. This structure replicates the workout regimen outlined in the [Hurricane Hypertrophy][HurricaneHypertrophy-url] program within Athlean-X.

The project includes one module:

+ **[hurricane_clock.py][Hurricane-Clock-url]**:
Contains two classes that handle the workout functionality:

  + **`HurricaneWorkout`**: Prompts the user for workout details such as muscle group, number of sets, and type of exercise. It initiates the workout based on these inputs.
  + **`HurricaneSob`**: Uses the details from "HurricaneWorkout" to implement a timed interval training structure. It guides users through the workout with sound notifications for each interval and handles workout set progression.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#athleanx-hurricane-workout-clock)

## Getting Started

Follow the steps below to set up and **run this project** locally.

> Note:
>
> If you wish to clone the entire repository, please refer to the "Getting Started" section of the README.md in the [first-solo-projects][First-Solo-Projects-url] repository.

### Prerequisites

Ensure you have [Python][Python-download] and [Git][Git-download] installed on your computer.

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

# Specify the subdirectory to include
$ echo "hurricane_clock/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd hurricane_clock
```

#### Finally

```bash
# Run the project
$ python hurricane_clock.py
```

[back to top](#athleanx-hurricane-workout-clock)

## Usage

By running this program, users can conduct interval training with a structured schedule, complete with sound cues to mark the end of each interval.

To start a workout session, simply run the script and follow the prompts to enter the details for your workout, then press "ENTER" to begin. The program will guide you through the intervals, playing sound cues to mark the end of each interval.

### Code Example

This code snippet from hurricane_clock.py demonstrates how the HurricaneSob class is defined and how it manages the structured interval workout session.

```py
class HurricaneSob:  # pylint: disable=R0903
    """Represent the Hurricane Hypertrophy interval training structure."""

    def __init__(self) -> None:
        """Initialize the instance of the HurricaneWorkout class."""
        self.workout: HurricaneWorkout = HurricaneWorkout()

    def run_clock(self) -> None:
        """Create the exercise interval clock."""
        print(f"\nGet ready to blast your {self.workout.muscle}.")

        for workout_set in range(1, self.workout.sets + 1):
            print(f"\n-  SOB {self.workout.exercise} Set {workout_set}:")

            # Run the interval clock.
            self._run_interval(20)
            self._run_interval(40)

        print(f"\nSOB {self.workout.exercise} completed.")

        # Restart the clock if the interval completed was the SOB 320.
        self._restart_clock()

    def _run_interval(self, duration: int) -> None:
        """
        Run for the specified duration in seconds
        and play a sound three times to simulate a countdown.
        """
        print(f"Running for {duration} seconds...")
        time.sleep(duration - 3)
        for _ in range(3):
            os.system("afplay /System/Library/Sounds/Ping.aiff")

    def _restart_clock(self) -> None:
        """Restart the clock if the exercise completed was the SOB 320."""
        if self.workout.exercise == 320:
            self.workout.exercise = 160
            self.workout.sets = 4
            self.workout.workout_start()
            self.run_clock()


if __name__ == "__main__":
    # Run the workout session.
    workout_session = HurricaneSob()
    workout_session.run_clock()
```

[back to top](#athleanx-hurricane-workout-clock)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first-solo-projects](https://github.com/E-Rinaudo/first-solo-projects/tree/main)

[back to top](#athleanx-hurricane-workout-clock)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#athleanx-hurricane-workout-clock)

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
[Hurricane-Clock-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/hurricane_clock/hurricane_clock.py

<!-- MAIN README -->
[First-Solo-Projects-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/README.md

<!-- MISCELLANEA -->
[Athleanx-url]: https://athleanx.com/
[HurricaneHypertrophy-url]: https://athleanx.com/nxt

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
