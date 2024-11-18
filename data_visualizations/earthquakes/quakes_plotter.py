#!/usr/bin/env python3

"""
This module defines the 'EarthquakesPlotter' class to analyze, plot and visualize
earthquakes activity using Plotly.

The class allows to:
- Import the earthquake data from GeoJSON files.
- Extract and handle magnitude, longitude, latitude, event title, and date of the quake.
- The cass also handles data formatting and customization of the plot title.
- Generate and customize a geographical plot to visualize the data.
"""

import sys
from pathlib import Path
import json
from datetime import datetime, timezone
from logging import warning
from typing import Any, Union, Optional

import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure


class EarthquakesPlotter:  # pylint: disable=R0902
    """Analyze and visualize earthquakes activity."""

    def __init__(self, path: Path) -> None:
        """Initialize the class attributes."""
        self.path = path
        self._data_attributes()
        self._data_lists()
        self.dataframe: pd.DataFrame = pd.DataFrame()

    def _data_attributes(self) -> None:
        """Initialize the data attributes."""
        self.quakes_data: dict[str, Any] = {}
        self.mag: Union[float, int] = 0.0
        self.long: float = 0.0
        self.lat: float = 0.0
        self.timestamp_seconds: float = 0.0
        self.event_title: str = ""
        self.date: str = ""
        self.title_date: str = ""
        self.formatted_plot_title: str = ""

    def _data_lists(self) -> None:
        """Initialize the lists to store the desired data."""
        self.mags: list[Union[float, int]] = []
        self.longs: list[float] = []
        self.lats: list[float] = []
        self.event_titles: list[str] = []
        self.event_dates: list[str] = []
        self.title_dates: list[str] = []

    def analyze_data(self, reformat_path: Optional[Path] = None) -> None:
        """Main method to analyze the earthquakes data."""
        self._read_text(reformat_path)
        self._extract_data()
        self._quakes_dataframe()

    def _read_text(self, reformat_path: Optional[Path]) -> None:
        """Try to read the earthquakes file."""
        try:
            self._reformat_file(reformat_path)
        except FileNotFoundError as err:
            warning(f"{err}")
            sys.exit()

    def _reformat_file(self, reformat_path: Optional[Path]) -> None:
        """Reformat the json file to make it readable if desired."""
        self._load_text()

        if reformat_path:
            path: Path = Path(reformat_path)
            readable_contents: str = json.dumps(self.quakes_data, indent=4)
            path.write_text(readable_contents, encoding="utf-8")

    def _load_text(self) -> None:
        """Convert the json file into a python object."""
        contents: str = self.path.read_text(encoding="utf-8")
        self.quakes_data = json.loads(contents)  # pylint: disable=W0201

    def _extract_data(self) -> None:
        """Extract the data of interest from the python object."""
        quakes: list[dict[str, Any]] = self.quakes_data["features"]

        # Extract magnitude, longitude, latitude, title and date for each earthquake
        #   only if the magnitude is not negative.
        for quake in quakes:
            if quake["properties"]["mag"] >= 0:
                try:
                    self._collect_data(quake)
                except KeyError as ke:
                    warning(f"{ke} missing in earthquake: {quake}.")
                    sys.exit()
                else:
                    self._get_quakes_date()
                    self._append_data()

        self._format_title()

    def _collect_data(self, quake: dict[str, Any]) -> None:
        """Collect the data of interest."""
        self.mag = quake["properties"]["mag"]  # pylint: disable=W0201
        self.long = quake["geometry"]["coordinates"][0]  # pylint: disable=W0201
        self.lat = quake["geometry"]["coordinates"][1]  # pylint: disable=W0201
        self.event_title = quake["properties"]["title"]  # pylint: disable=W0201
        self.timestamp_seconds = quake["properties"]["time"] / 1000  # pylint: disable=W0201

    def _get_quakes_date(self) -> None:
        """Get the date of each earthquake and format it."""
        utc_timezone: timezone = timezone.utc
        quake_datetime: datetime = datetime.fromtimestamp(self.timestamp_seconds, utc_timezone)
        # Format the date for the label of each earthquake.
        self.date = quake_datetime.strftime("%B %d, %Y -- %H:%M:%S %Z (24-Hour format)")  # pylint: disable=W0201
        # Format the date for the plot title.
        self.title_date = quake_datetime.strftime("%B %Y")  # pylint: disable=W0201

    def _append_data(self) -> None:
        """Store the collected data in lists."""
        self.mags.append(self.mag)
        self.longs.append(self.long)
        self.lats.append(self.lat)
        self.event_titles.append(self.event_title)
        self.event_dates.append(self.date)
        if self.title_date not in self.title_dates:
            self.title_dates.append(self.title_date)

    def _format_title(self) -> None:
        """Neatly format the plot title."""
        self._adjust_title_dates()

        quakes_title: str = self.quakes_data["metadata"]["title"].split(", ")
        self.formatted_plot_title = f"{quakes_title[0]} ({" - ".join(self.title_dates)})"  # pylint: disable=W0201

    def _adjust_title_dates(self) -> None:
        """
        Adjust the title_dates list so the plot title can then be displayed
        as (Month, Month Year).
        """
        if len(self.title_dates) == 2:
            self.title_dates.reverse()
            first_date_split: list[str] = self.title_dates[0].split(" ")
            self.title_dates[0] = first_date_split[0]

    def _quakes_dataframe(self) -> None:
        """Make a dataframe of the earthquakes data."""
        quakes_df: dict[str, list[Any]] = {
            "Magnitude": self.mags,
            "Latitude": self.lats,
            "Longitude": self.longs,
            "Event Title": self.event_titles,
            "Date": self.event_dates,
        }

        self.dataframe = pd.DataFrame(quakes_df)

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

    def _update_fig_title(self, fig: Figure, title_color: Optional[str]) -> None:
        """Update the layout of the title."""
        fig.update_layout(
            title={
                "text": self.formatted_plot_title,
                "font": {"color": title_color},
                "y": 0.95,
                "x": 0.48,
            }
        )
