# Wildfires Activity Visualization

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Wildfires** is a project designed to visualize wildfire activity across North America from July 12 to July 14, 2024. Using the fires_analyzer.py module, this project creates geographical scatter plots to display wildfire locations and brightness levels, using Plotly.

This project was developed while working through chapters 16 of Python Crash Course.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

It visualizes wildfire data to illustrate the intensity and spread of wildfires in the contiguous USA and Hawaii. The visualization includes details such as the location (latitude and longitude) and brightness of wildfires, helping to better understand their geographical distribution and intensity.

The project includes:

Main module:

+ **[fires_analyzer.py][Fires-Analyzer-url]**:
Reads data from a CSV file, formats it, and generates an interactive map using Plotly.

Data files directory:

+ **[fires_file/.py][Fires-File-url]**:
It stores a CSV file which data is sourced from the Fire Information for Resource Management System (FIRMS): <https://firms.modaps.eosdis.nasa.gov/active_fire/>.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Plotly][Plotly-badge]][Plotly-url]
+ [![Pandas][Pandas-badge]][Pandas-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#wildfires-activity-visualization)

## Getting Started

Follow the steps below to set up and **run this project** locally.

> Note:
>
> If you wish to clone the entire repository, please refer to the "Getting Started" section of the README.md in the [first_solo_project][First-Solo-Project-url] repository.
>
> Whereas, if you wish to clone the entire data visualizations subdirectory, please refer to the "Getting Started" section of the README.md in [data_visualizations][Data-Visualizations-url].
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
$ echo "data_visualizations/wildfires/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd wildfires

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
$ python fires_analyzer.py
```

[back to top](#wildfires-activity-visualization)

## Usage

By running this program, users can generate an interactive map showing wildfire activity. Each marker on the scatter plot represents a wildfire, with the size and color of the markers indicating the fire's brightness and intensity. The map will open in your browser for easy exploration.

### Code Example

This code snippet from fires_analyzer.py demonstrates how the data is processed and visualized.

```py
def visualize_plot(self) -> None:
    """Visualize wildfire activity."""
    self._format_label_text()
    # Lower the brightness value to use it as a size in the plot.
    bright_size = [bright // 18 for bright in self.fires_data["brightness"]]

    # Make the plot.
    fig = go.Figure(
        data=go.Scattergeo(
            lat=self.fires_data["latitude"],
            lon=self.fires_data["longitude"],
            text=self.fires_data["text"],
            mode="markers",
            marker={
                "size": bright_size,
                "symbol": "star-triangle-up",
                "color": self.fires_data["brightness"],
                "colorscale": "Hot",
                "colorbar_title": "Wildfire Brightness",
            },
        )
    )

    self._update_plot(fig)
    fig.show(renderer="browser")
```

### Project Screenshot

![Wildfires Screenshot][Screenshot-url]

[back to top](#wildfires-activity-visualization)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#wildfires-activity-visualization)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#wildfires-activity-visualization)

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
[Fires-Analyzer-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/wildfires/fires_analyzer.py
[Fires-File-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations/wildfires/fires_file
[Data-Visualizations-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations

<!-- SCREENSHOT -->
[Screenshot-url]: screenshot/wildfires.png

<!-- MAIN README -->
[First-Solo-Project-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
