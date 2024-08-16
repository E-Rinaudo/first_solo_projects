# Data Visualizations

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

A collection of projects focused on visualizing data using Matplotlib and Plotly. These projects were developed working through chapters 15-17 of Python Crash Course.s
Each one is housed within its own subdirectory. Feel free to explore the READMEs of these projects for detailed information. You will find code snippets and screenshots to help you understand the functionality of each project.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Projects Collection](#about-this-projects-collection) •
[Getting Started](#getting-started) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Projects Collection

The projects included in this directory focus on various domains, from earthquake and weather data to random walks and wildfire intensity.

+ **[earthquakes/][Earthquakes-url]**:
Visualizes earthquake data, using Plotly. The module reads data from GeoJSON files and plots them to show their geographical distribution and intensity.

+ **[github_python_julia_r_repos/][Github-Python-Julia-R-Repos-url]**:
Displays the top 20 most-starred repositories on GitHub for Python, Julia, and R, using Plotly. It extracts data from GitHub's API and displays the repository names and star counts in separate subplots for each programming language.

+ **[meteorology_visuals/][Meteorology-Visuals-url]**:
Generates various weather-related visualizations using Matplotlib, based on data read from CSV files.

+ **[random_walks/][Random-Walks-url]**:
This subdirectory contains two projects that visualize random walks:

  + **[firefly_random_walk/][Firefly-Random-Walk-url]**:
  Uses Plotly to visualize the imaginary random walk of a firefly on a summer night.

  + **[molecular_motion/][Molecular-Motion-url]**:
  Uses Matplotlib to visualize the simulated random motion of a pollen grain on the surface of a drop of water.

+ **[rolling_dice/][Rolling-Dice-url]**:
Shows the results of rolling two six-sided dice 50,000 times, using Matplotlib.

+ **[wildfires/][Wildfires-url]**:
Illustrates the intensity and spread of wildfires in the contiguous USA and Hawaii from July 12 to July 14, 2024 through a visualization created with Plotly.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Plotly][Plotly-badge]][Plotly-url]
+ [![Matplotlib][Matplotlib-badge]][Matplotlib-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]

[back to top](#data-visualizations)

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
$ echo "data_visualizations/" >> .git/info/sparse-checkout

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
$ echo "data_visualizations/project_name/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to what you cloned
# Choose one of the following based on what you cloned

## If you cloned the entire directory
$ cd data_visualizations

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

[back to top](#data-visualizations)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#data-visualizations)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#data-visualizations)

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
[Plotly-badge]: https://img.shields.io/badge/Plotly-239120?style=flat&logo=plotly&logoColor=white
[Plotly-url]: https://plotly.com/python/
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
[Earthquakes-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/earthquakes
[Github-Python-Julia-R-Repos-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/github_python_julia_r_repos
[Meteorology-Visuals-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/meteorology_visuals
[Random-Walks-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/random_walks
[Firefly-Random-Walk-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/random_walks/firefly_random_walk
[Molecular-Motion-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/random_walks/molecular_motion
[Rolling-Dice-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/rolling_dice
[Wildfires-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/wildfires

<!-- MAIN README -->
[FirstSoloProject-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
