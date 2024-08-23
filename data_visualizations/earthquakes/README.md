# Earthquakes Activity Visualizations

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Earthquakes** is a project designed to visualize earthquake activity globally using Plotly. It includes several scripts to analyze and visualize earthquake data from mid-June to mid-July 2024, offering insights into seismic events through interactive geographical plots.

This project was developed while working through chapter 16 of Python Crash Course.

Data source: **United States Geological Survey (USGS)**, <https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php>.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

The Earthquakes project visualizes global seismic activity using data from GeoJSON files.

The project includes:

Main module:

+ **[quakes_plotter.py][Quakes-Plotter-url]**:
Defines the EarthquakesPlotter class to analyze and visualize earthquake activity with Plotly. This class imports data, processes it, and creates interactive geographical plots.

Visualization modules:

+ **[full_month_quakes.py][Full-Month-Quakes-url]**:
Uses the EarthquakesPlotter class to plot and visualize all earthquakes from mid-June to mid-July 2024. It loads the data from all_month.geojson and visualizes it with a color scheme.

+ **[high_magnitude_quakes.py][High-Magnitude-Quakes-url]**:
Uses the EarthquakesPlotter class to plot and visualize earthquakes with a magnitude of 4.5 or higher from mid-June to mid-July 2024. It loads the data from 4.5_month.geojson and visualizes it with a color scheme.

+ **[significant_quakes.py][Significant-Quakes-url]**:
Uses the EarthquakesPlotter class to plot and visualize the most significant earthquakes from mid-June to mid-July 2024. It loads the data from significant_month.geojson and visualizes it with a color scheme.

Test module:

+ **[test_quakes_plotter.py][Test-Quakes-Plotter-url]**:
Tests the EarthquakesPlotter class to ensure it functions correctly. It includes tests for data extraction, file handling, date formatting, and handling of negative magnitudes.

Data files directory:

+ **[earthquakes_files/][Earthquakes-Files/-url]**:
Contains the GeoJSON files used for the visualizations:
  + 4.5_month.geojson: Contains earthquake data with magnitudes of 4.5 or higher.
  + all_month.geojson: Contains earthquake data for the full month.
  + significant_month.geojson: Contains data about the most significant earthquakes.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Plotly][Plotly-badge]][Plotly-url]
+ [![Pandas][Pandas-badge]][Pandas-url]
+ [![Pytest][Pytest-badge]][Pytest-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#earthquakes-activity-visualizations)

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
$ echo "data_visualizations/earthquakes/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd earthquakes

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
$ python full_month_quakes.py
$ python high_magnitude_quakes.py
$ python significant_quakes.py
```

[back to top](#earthquakes-activity-visualizations)

## Usage

By running this project, users can visualize different aspects of earthquakes activity from mid-June to mid-July 2024. Each script loads specific GeoJSON data and creates interactive maps displaying earthquake magnitudes, locations, and event details.

### Code Example

This code snippet from quakes_plotter.py shows how the geographical scatter plot is generated using Plotly.

```py
def plot_quakes(self, quakes_color: str, title_color: Optional[str] = None) -> None:
        """Plot the earthquakes."""
        fig: Figure = px.scatter_geo(
            data_frame=self.dataframe,
            size="Magnitude",
            lat="Latitude",
            lon="Longitude",
            color="Magnitude",
            color_continuous_scale=quakes_color,
            projection="robinson",
            hover_name="Event Title",
            hover_data={"Date": True},
        )

        self._update_fig_title(fig, title_color)
        fig.show()
```

This code snippet from significant_quakes.py shows the use of the EarthquakesPlotter class to analyze and visualize earthquake data:

```py
from pathlib import Path

from quakes_plotter import EarthquakesPlotter as EP


if __name__ == "__main__":
    # Make the instance and visualize the data.
    path: Path = Path("earthquakes_files/significant_month.geojson")

    quakes_plotter: EP = EP(path=path)
    quakes_plotter.analyze_data()
    quakes_plotter.plot_quakes(quakes_color="Cividis")
```

### Project Screenshot

![High Magnitude Screenshot][Screenshot-url]

[back to top](#earthquakes-activity-visualizations)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#earthquakes-activity-visualizations)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#earthquakes-activity-visualizations)

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
[Pandas-badge]: https://img.shields.io/badge/Pandas-%23234CAF50?style=flat&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/docs/
[Pytest-badge]: https://img.shields.io/badge/pytest-%23123A6C?style=flat&logo=pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/en/stable/contents.html
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
[Quakes-Plotter-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/earthquakes/quakes_plotter.py
[Full-Month-Quakes-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/earthquakes/full_month_quakes.py
[High-Magnitude-Quakes-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/earthquakes/high_magnitude_quakes.py
[Significant-Quakes-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/earthquakes/significant_quakes.py
[Test-Quakes-Plotter-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/earthquakes/test_quakes_plotter.py
[Earthquakes-Files/-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/earthquakes/earthquakes_files
[Data-Visualizations-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations

<!-- SCREENSHOT -->
[Screenshot-url]: screenshot/high_magnitude_earthquakes.png

<!-- MAIN README -->
[First-Solo-Project-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
