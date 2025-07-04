# Spaced Repetition Reminder

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Spaced Repetition Reminder** is a simple program designed to help with study planning by generating a daily reminder based on the spaced repetition method, a learning technique where information is reviewed at increasing intervals over time to improve long-term retention and recall.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

This project utilizes a pop-up window to display the tasks scheduled for the current day, ensuring one stays on track with the study goals.

The project includes two modules:

+ **[pop_up.py][PopUp-url]**:
Defines the StudyPopUp class, which creates and displays a pop-up window using Tkinter. The pop-up shows the current date, the subject being studied, and a list of tasks scheduled for the day.

+ **[study_schedule.py][Study-Schedule-url]**:
Configures the study schedule for the week and determines which tasks should be displayed each day. It initializes an instance of the StudyPopUp class to generate the daily reminder pop-up based on the defined schedule.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#spaced-repetition-reminder)

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
$ echo "spaced_repetition_reminder/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd spaced_repetition_reminder
```

#### Finally

```bash
# Run the project
$ python study_schedule.py
```

[back to top](#spaced-repetition-reminder)

## Usage

By running this program, users receive a reminder about what to study or review, making it easier to follow a structured study plan and keep track of their progress.

For convenience, consider creating a terminal alias to run the script automatically each day.

### Code Example

This code snippet from study_schedule.py demonstrates how the weekly schedule is defined.

```py
from pop_up import StudyPopUp

# Define the parameters.
DAYS: list[str] = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

MONTHS: list[str] = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]

STUDY_METHOD: dict[str, list[str]] = {
    "monday": ["Study new block", "Repeat today's block"],
    "tuesday": ["Repeat yesterday's block", "Study new block", "Repeat today's block"],
    "wednesday": [
        "Repeat yesterday's block",
        "Study new block",
        "Repeat today's block",
    ],
    "thursday": ["Repeat yesterday's block", "Study new block", "Repeat today's block"],
    "friday": [
        "Repeat Monday's block",
        "Repeat yesterday's block",
        "Study new block",
        "Repeat today's block",
    ],
    "saturday": ["Repeat all blocks"],
    "sunday": ["Repeat all blocks"],
}

subject: str = "python crash course"

if __name__ == "__main__":
    # Make an instance of StudyPopUp to display the study reminder.
    show_popup = StudyPopUp(DAYS, MONTHS, STUDY_METHOD, subject)
```

[back to top](#spaced-repetition-reminder)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first-solo-projects](https://github.com/E-Rinaudo/first-solo-projects/tree/main)

[back to top](#spaced-repetition-reminder)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#spaced-repetition-reminder)

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
[PopUp-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/spaced_repetition_reminder/pop_up.py
[Study-Schedule-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/spaced_repetition_reminder/study_schedule.py

<!-- MAIN README -->

[First-Solo-Projects-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
