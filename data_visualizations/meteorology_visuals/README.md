# Meteorology Visualizations

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Meteorology Visualizations** is a project aimed at transforming raw weather data from CSV files into plots, displaying daily high and low temperatures and precipitation levels. This project includes nine visualization modules, each plotting different weather data. There is also a module that represents an early attempt at writing tests to ensure code robustness.

This project was developed while working through chapter 16 of Python Crash Course.

Data source: **National Centers for Environmental Information (NCEI)**, <https://www.ncdc.noaa.gov/cdo-web/>

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

Meteorology Visualizations displays weather data through a core class and nine distinct visualization modules. The main module, weather_data_plotter.py, is designed to process weather data from CSV files and produce customizable plots using Matplotlib. This includes plotting high and low temperatures, precipitation, and shading between temperature extremes.

This project includes:

Main module:

+ **[weather_data_plotter.py][Weather-Data-Plotter-url]**:
It defines the WeatherDataPlotter class, which reads weather data from CSV files and generattes various types of plots. It offers flexibility in terms of customization, such as shading between high and low temperatures.

Visualization modules:

+ **[los_angeles_highs_lows_f.py][Los-Angelese-Highs-Lows-F-url]**:
Plots daily high and low temperatures for Los Angeles, with temperatures in Fahrenheit.

+ **[madrid_highs_c.py][Madrid-Highs-C-url]**:
Visualizes daily high temperatures for Madrid, with temperatures in Celsius.

+ **[madrid_highs_f.py][Madrid-Highs-F-url]**:
Visualizes daily high temperatures for Madrid, with temperatures in Fahrenheit.

+ **[madrid_lows_c.py][Madrid-Lows-C-url]**:
Visualizes daily low temperatures for Madrid, with temperatures in Celsius.

+ **[madrid_lows_f.py][Madrid-Lows-F-url]**:
Visualizes daily low temperatures for Madrid, with temperatures in Fahrenheit.

+ **[madrid_rainfall_cm.py][Madrid-Rainfall-CM-url]**:
Plots daily precipitation levels in centimeters for Madrid.

+ **[san_francisco_highs_lows_f.py][San-Francisco-Highs-Lows-F-url]**:
Plots daily high and low temperatures for San Francisco, with temperature values in Fahrenheit.

+ **[sitka_death_valley_highs_lows_f.py][Sitka-Death-Valley-Highs-Lows-F-url]**:
Visualizes daily high and low temperatures for Sitka and Death Valley, with temperature values in Fahrenheit.

+ **[sitka_death_valley_rainfall_in.py][Sitka-Death-Valley-Rainfall-IN-url]**:
Plots daily precipitation levels in inches for Sitka and Death Valley.

Test module:

+ **[test_weather_data_plotter.py][Test-Weather-Data-Plotter-url]**:
Contains unit tests for validating the functionality of the WeatherDataPlotter class, ensuring that the plotting and data processing work as expected.

Data files directory:

+ **[weather_data/][Weather-Data-url]**:
Contains the CSV files with raw weather data used for the visualizations.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Matplotlib][Matplotlib-badge]][Matplotlib-url]
+ [![Pytest][Pytest-badge]][Pytest-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#meteorology-visualizations)

## Getting Started

Follow the steps below to set up and **run this project** locally.

> Note:
>
> If you wish to clone the entire repository, please refer to the "Getting Started" section of the README.md in the [first-solo-projects][First-Solo-Projects-url] repository.
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
$ git remote add origin https://github.com/E-Rinaudo/first-solo-projects.git

# Enable sparse checkout
$ git config core.sparseCheckout true

# Specify the project to include
$ echo "data_visualizations/meteorology_visuals/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd meteorology_visuals

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
$ los_angeles_highs_lows_f.py
$ madrid_highs_c.py
$ madrid_highs_f.py
$ madrid_lows_c.py
$ madrid_lows_f.py
$ madrid_rainfall_cm.py
$ san_francisco_highs_lows_f.py
$ sitka_death_valley_highs_lows_f.py
$ sitka_death_valley_rainfall_in.py
```

[back to top](#meteorology-visualizations)

## Usage

By running this program, users can visualize various aspects of weather data, including high and low temperatures, precipitation levels, and temperature shading. Simply execute one of the provided scripts to generate the respective plots for different locations and data types.

### Code Example

This code snippet from weather_data_plotter.py demonstrates the process of generating the visualizations.

```py
def plot_visual(
        self,
        shade_between: bool = True,
        y_limit: Optional[tuple[Union[float, int], Union[float, int]]] = None,
    ) -> None:
        """Generate and visualize the plot using the data previously extracted."""
        for self.dataset in self.datasets:
            self._make_plot(shade_between)

        self._customize_plot(y_limit)
        plt.show()
```

This code snippet from madrid_highs_f.py illustrates how to use the WeatherDataPlotter class to generate a plot for Madrid’s high temperatures.

```py
from pathlib import Path

from weather_data_plotter import WeatherDataPlotter as WDP


if __name__ == "__main__":
    # Create a plotter instance.
    weather_plotter: WDP = WDP(title="Daily High Temperatures, 2023")

    # Add data for Madrid to the plotter dataset.
    path: Path = Path("weather_data/madrid_weather_2023_f_in.csv")

    weather_plotter.weather_dataset(  # pylint: disable=R0801
        path=path,
        high=True,
        color="red",
        label="Madrid",
        temp_scale="F°",
    )

    # Generate the visualization.
    weather_plotter.plot_visual(y_limit=(0, 110))
```

### Project Screenshots

![Meteorology Screenshots][Screenshots-url]

[back to top](#meteorology-visualizations)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first-solo-projects](https://github.com/E-Rinaudo/first-solo-projects/tree/main)

[back to top](#meteorology-visualizations)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#meteorology-visualizations)

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
[Matplotlib-badge]: https://img.shields.io/badge/Matplotlib-3776AB?
[Matplotlib-url]: https://matplotlib.org/stable/users/index.html
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
[Weather-Data-Plotter-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/weather_data_plotter.py
[Test-Weather-Data-Plotter-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/test_weather_data_plotter.py
[Los-Angelese-Highs-Lows-F-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/los_angeles_highs_lows_f.py
[Madrid-Highs-C-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/madrid_highs_c.py
[Madrid-Highs-F-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/madrid_highs_f.py
[Madrid-Lows-C-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/madrid_lows_c.py
[Madrid-Lows-F-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/madrid_lows_f.py
[Madrid-Rainfall-CM-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/madrid_rainfall_cm.py
[San-Francisco-Highs-Lows-F-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/san_francisco_highs_lows_f.py
[Sitka-Death-Valley-Highs-Lows-F-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/sitka_death_valley_highs_lows_f.py
[Sitka-Death-Valley-Rainfall-IN-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/data_visualizations/meteorology_visuals/sitka_death_valley_rainfall_in.py
[Weather-Data-url]: https://github.com/E-Rinaudo/first-solo-projects/tree/main/data_visualizations/meteorology_visuals/weather_data
[Data-Visualizations-url]: https://github.com/E-Rinaudo/first-solo-projects/tree/main/data_visualizations

<!-- SCREENSHOTS -->
[Screenshots-url]: screenshots/madrid_highs_f_san_francisco.gif

<!-- MAIN README -->
[First-Solo-Projects-url]: https://github.com/E-Rinaudo/first-solo-projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
