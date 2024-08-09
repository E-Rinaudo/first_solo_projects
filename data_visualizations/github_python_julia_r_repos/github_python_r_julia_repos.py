"""
This module defines the 'RepositoryPlotter' class to analyze, plot and visualize
data on GitHub repositories. 
The analysis focuses on the top 20 most-starred repositories for 
Python, Julia, and R, using Plotly for visualization.

The class allows to:
- Make an API call to fetch the data.
- Extract and process the repository names and star counts.
- Generate and customize bar plots to visualize the data.
"""

import sys

from logging import warning
from typing import Any, Union
import requests
from requests.exceptions import RequestException

import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go


PLOT_TITLE = "Top 20 Most-Starred Repositories on GitHub for Python, Julia, and R"
XAXES_TITLE = "Repository"
YAXES_TITLE = "Stars"
PYTHON_BARS = "rgb(0, 114, 178)"
JULIA_BARS = "rgb(213, 94, 0)"
R_BARS = "rgb(0, 158, 115)"
BLACK_COLOR = "rgb(0, 0, 0)"
HOVER_LABEL_BGCOLOR = "rgb(255, 255, 255)"
TITLE_SIZE = 24
AXIS_LABEL_SIZE = 16
LEGEND_SIZE = 14
XAXIS_TICK_ANGLE = 45


class RepositoryPlotter:
    """Visualize the top 20 repositories on GitHub for Python, Julia, and R."""

    def __init__(self):
        """Initialize the class attributes."""
        python_url, julia_url, r_url = self._api_urls()
        self.langs_urls = {
            "Python": python_url,
            "Julia": julia_url,
            "R": r_url,
        }
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        self.responses: dict[str, dict[str, Any]] = {}
        self.repositories: dict[str, list[dict[str, Any]]] = {}
        self.repo_data: dict[str, list[Union[str, int]]] = {}
        self.fig = None

    def _api_urls(self):
        """Store the API URLs for Python, Julia, and R repositories."""
        python_url = "https://api.github.com/search/repositories"
        python_url += "?q=language:python+sort:stars+stars:>1000"

        julia_url = "https://api.github.com/search/repositories"
        julia_url += "?q=language:julia+sort:stars+stars:>1000"

        r_url = "https://api.github.com/search/repositories"
        r_url += "?q=language:r+sort:stars+stars:>1000"

        return python_url, julia_url, r_url

    def _make_api_call(self):
        """Make the GitHub API call for each language and store the responses."""
        for lang, url in self.langs_urls.items():
            try:
                request = requests.get(url, headers=self.headers, timeout=(5, 10))
                request.raise_for_status()
            except RequestException as err:
                warning(f"Request failed for {lang}: {err}")
                sys.exit()
            else:
                print(f"Status code ({lang}): {request.status_code}")

                response = request.json()
                self.responses[lang] = response

        self._pull_20_repositories()

    def _pull_20_repositories(self):
        """Extract the top 20 repositories for each language from the API responses."""
        print()
        for lang, response_data in self.responses.items():
            print(
                f"Complete results for {lang}: "
                f"{not response_data["incomplete_results"]}"
            )
            self.repositories[lang] = response_data["items"][:20]

        self._pull_repo_names_stars()

    def _pull_repo_names_stars(self):
        """Extract and store each repository name with its URL link and stars count."""
        for lang, repos in self.repositories.items():
            repo_name_key = f"{lang} Repos Names"
            star_key = f"{lang} Stars"
            repo_name_links = [
                f"<a href='{repo["html_url"]}' style='color: rgb(0, 0, 0)'>"
                f"{repo["name"]}</a>"
                for repo in repos
            ]
            stars = [repo["stargazers_count"] for repo in repos]
            self.repo_data[repo_name_key] = repo_name_links
            self.repo_data[star_key] = stars

    def _make_subplots(self):
        """Make a subplot with three columns, one for each language."""
        self.fig = make_subplots(
            rows=1,
            cols=3,
        )

        self._add_traces()

    def _add_traces(self):
        """Add bar traces for each language to the subplot."""
        self._add_first_trace()
        self._add_second_trace()
        self._add_third_trace()

    def _add_first_trace(self):
        """Add a bar trace to the first subplot column (Python)."""
        self.fig.add_trace(
            go.Bar(
                x=self.repo_data["Python Repos Names"],
                y=self.repo_data["Python Stars"],
                name="Python",
                marker_color=PYTHON_BARS,
                hoverlabel={
                    "bgcolor": HOVER_LABEL_BGCOLOR,
                    "font_color": BLACK_COLOR,
                },
            ),
            row=1,
            col=1,
        )

    def _add_second_trace(self):
        """Add a bar trace to the second subplot column (Julia)."""
        self.fig.add_trace(
            go.Bar(
                x=self.repo_data["Julia Repos Names"],
                y=self.repo_data["Julia Stars"],
                name="Julia",
                marker_color=JULIA_BARS,
                hoverlabel={
                    "bgcolor": HOVER_LABEL_BGCOLOR,
                    "font_color": BLACK_COLOR,
                },
            ),
            row=1,
            col=2,
        )

    def _add_third_trace(self):
        """Add a bar trace to the third subplot column (R)."""
        self.fig.add_trace(
            go.Bar(
                x=self.repo_data["R Repos Names"],
                y=self.repo_data["R Stars"],
                name="R",
                marker_color=R_BARS,
                hoverlabel={
                    "bgcolor": HOVER_LABEL_BGCOLOR,
                    "font_color": BLACK_COLOR,
                },
            ),
            row=1,
            col=3,
        )

    def _update_layout(self):
        """Update the plot layout."""
        self.fig.update_layout(
            title={
                "text": PLOT_TITLE,
                "font": {
                    "color": BLACK_COLOR,
                    "size": TITLE_SIZE,
                    "weight": "bold",
                },
            },
            barmode="group",
            bargap=0.15,
            bargroupgap=0.1,
            legend={
                "font": {
                    "color": BLACK_COLOR,
                    "size": LEGEND_SIZE,
                }
            },
        )

        self._update_xaxes()
        self._update_yaxes()

    def _update_xaxes(self):
        """Update the x-axis for the subplots."""
        # General update.
        self.fig.update_xaxes(
            title={
                "text": XAXES_TITLE,
                "font": {
                    "color": BLACK_COLOR,
                    "size": AXIS_LABEL_SIZE,
                },
            },
            tickangle=XAXIS_TICK_ANGLE,
        )
        # Specific updates.
        self._update_first_xaxis()
        self._update_second_xaxis()
        self._update_third_xaxis()

    def _update_first_xaxis(self):
        """Update the x-axis for the first subplot (Python)."""
        self.fig.update_xaxes(
            title_standoff=28,
            row=1,
            col=1,
        )

    def _update_second_xaxis(self):
        """Update the x-axis for the second subplot (Julia)."""
        self.fig.update_xaxes(
            title_standoff=22,
            row=1,
            col=2,
        )

    def _update_third_xaxis(self):
        """Update the x-axis for the third subplot (R)."""
        self.fig.update_xaxes(
            title_standoff=0,
            row=1,
            col=3,
        )

    def _update_yaxes(self):
        """Update the y-axis of each language, setting a logarithmic scale."""
        self.fig.update_yaxes(
            type="log",
            range=([np.log10(100), np.log10(1_000_000)]),
            exponentformat="power",
            title={
                "text": YAXES_TITLE,
                "font": {
                    "color": BLACK_COLOR,
                    "size": AXIS_LABEL_SIZE,
                },
            },
            tickfont={
                "color": BLACK_COLOR,
            },
            showticklabels=True,
            title_standoff=8,
        )

    def main(self):
        """Store the main methods to make the plot and show it."""
        self._make_api_call()
        self._make_subplots()
        self._update_layout()
        self.fig.show(renderer="browser")


if __name__ == "__main__":
    # Make the instance and visualize the plot.
    repo_plotter = RepositoryPlotter()
    repo_plotter.main()
