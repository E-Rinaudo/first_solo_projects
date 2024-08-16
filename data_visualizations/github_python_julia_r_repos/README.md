# Most-Starred Repositories on GitHub for Python, Julia, and R

[![MIT License][license-shield]][license-url]
[![Gmail][Gmail-shield]][Gmail-url]

**Most-Starred Repositories on GitHub for Python, Julia and R** is a project designed to visualize the top 20 most-starred repositories on GitHub for these three programming languages, using Plotly.

This project was developed while working through chapter 17 of Python Crash Course.

<!-- markdownlint-disable MD001 -->
### Table of Contents

[About this Project](#about-this-project) •
[Getting Started](#getting-started) •
[Usage](#usage) •
[Contact](#contact) •
[License](#license)
<!-- markdownlint-enable MD001 -->

## About this Project

This project uses GitHub's API to gather data on the top 20 repositories by stars for Python, Julia, and R. The data is then processed and visualized using Plotly, with each language's repositories displayed in a separate subplot. The visualization employs a logarithmic scale on the y-axis to handle the wide range of star counts effectively. This allows users to quickly see which repositories are most popular in each language and compare them side-by-side.

The project includes:

Main module:

+ **[github_python_julia_r_repos.py][GitHub-Python-R-Julia-Repos-url]**:
Handles data fetching, processing, and visualization.

Test module:

+ **[test_github_python_julia_r_repos.py][Test-GitHub-Python-R-Julia-Repos-url]**:
Ensures the functionality and accuracy of the data processing and visualization steps.

### Built With

+ [![Python][Python-badge]][Python-url]
+ [![Visual Studio Code][VSCode-badge]][VSCode-url]
+ [![Plotly][Plotly-badge]][Plotly-url]
+ [![Requests][Requests-badge]][Requests-url]
+ [![Numpy][Numpy-badge]][Numpy-url]
+ [![Pytest][Pytest-badge]][Pytest-url]
+ [![Mypy][Mypy-badge]][Mypy-url]
+ [![Black][Black-badge]][Black-url]
+ [![Pylint][Pylint-badge]][Pylint-url]
+ [![Flake8][Flake8-badge]][Flake8-url]
+ [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#most-starred-repositories-on-github-for-python-julia-and-r)

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
$ echo "data_visualizations/github_python_julia_r_repos/" >> .git/info/sparse-checkout

# Pull the contents
$ git pull origin main
```

#### After Cloning

```bash
# Go to the cloned project
$ cd github_python_julia_r_repos

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
$ python github_python_julia_r_repos.py
```

[back to top](#most-starred-repositories-on-github-for-python-julia-and-r)

## Usage

By running the script, users will be able visualize in their default web browser the most-starred repositories for Python, Julia, and R and their respective star counts.

### Code Example

This code snippet from github_python_julia_r_repos.py demonstrates the core functionality of the RepositoryPlotter class. This class is responsible for fetching data from GitHub's API, initializing API URLs, performing API calls, and generating a Plotly bar plot to display the repositories side-by-side for easy comparison.

```py
class RepositoryPlotter:
    """Visualize the top 20 repositories on GitHub for Python, Julia, and R."""

    def __init__(self) -> None:
        """Initialize the class attributes."""
        python_url, julia_url, r_url = self._api_urls()
        self.langs_urls: dict[str, str] = {
            "Python": python_url,
            "Julia": julia_url,
            "R": r_url,
        }
        self.headers: dict[str, str] = {"Accept": "application/vnd.github.v3+json"}
        self.responses: dict[str, dict[str, Any]] = {}
        self.repositories: dict[str, list[dict[str, Any]]] = {}
        self.repo_data: dict[str, list[Union[str, int]]] = {}
        self.fig: Figure = None

    def _api_urls(self) -> tuple[str, str, str]:
        """Store the API URLs for Python, Julia, and R repositories."""
        python_url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>1000"

        julia_url = "https://api.github.com/search/repositories?q=language:julia+sort:stars+stars:>1000"

        r_url = "https://api.github.com/search/repositories?q=language:r+sort:stars+stars:>1000"

        return python_url, julia_url, r_url

    def main(self) -> None:
        """Store the main methods to make the plot and show it."""
        self._make_api_call()
        self._make_subplots()
        self._update_layout()
        self.fig.show(renderer="browser")
```

### Project Screenshot

![GitHub Repos Screenshot][Screenshot-url]

[back to top](#most-starred-repositories-on-github-for-python-julia-and-r)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email at <enricorinaudo91@gmail.com>.
Your feedback is appreciated as it helps me to continue improving.

You can also explore my GitHub profile or the project repository for more information:

+ Profile Link: [https://github.com/E-Rinaudo](https://github.com/E-Rinaudo)
+ Project Link: [https://github.com/E-Rinaudo/first_solo_project](https://github.com/E-Rinaudo/first_solo_projects/tree/main)

[back to top](#most-starred-repositories-on-github-for-python-julia-and-r)

## License

These projects are distributed under the MIT License. See [`LICENSE.txt`][license-url] for more information.

[back to top](#most-starred-repositories-on-github-for-python-julia-and-r)

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
[Requests-badge]: https://img.shields.io/badge/requests-%2335C2C2?style=flat&logo=requests&logoColor=white
[Requests-url]: https://requests.readthedocs.io/en/latest/
[Numpy-badge]: https://img.shields.io/badge/numpy-%234B8BBE?style=flat&logo=numpy&logoColor=white
[Numpy-url]: https://numpy.org/doc/stable/
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
[GitHub-Python-R-Julia-Repos-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/github_python_julia_r_repos/github_python_julia_r_repos.py
[Test-GitHub-Python-R-Julia-Repos-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/data_visualizations/github_python_julia_r_repos/test_github_python_julia_r_repos.py
[Data-Visualizations-url]: https://github.com/E-Rinaudo/first_solo_projects/tree/main/data_visualizations

<!-- SCREENSHOT -->
[Screenshot-url]: screenshot/github_repos.png

<!-- MAIN README -->
[First-Solo-Project-url]: https://github.com/E-Rinaudo/first_solo_projects/blob/main/README.md

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
