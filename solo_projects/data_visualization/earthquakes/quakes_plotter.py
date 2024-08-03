"""
This module defines the 'EartquakesPlotter' class to analyze, plot and visualize
earthquakes activity using Plotly.

The class allows to:
- Import the earthquake data from GeoJSON files.
- Extract and process magnitude, longitude, latitude, event title, and date of the quake.
- The cass also handles data formatting and customization of the plot title.
- Generate and customize a geographical plot to visualize the data.
"""

import sys
from pathlib import Path
import json
from datetime import datetime, timezone
from logging import warning
from typing import Optional

import pandas as pd
import plotly.express as px


class EartquakesPlotter:
    """Analyze and visualize earthquakes activity."""

    def __init__(self, path: Path):
        """Initialize the class attributes."""
        self.path = path
        self._data_attributes()
        self._data_lists()
        self.dataframe = pd.DataFrame()

    def _data_attributes(self):
        """Initialize the data attributes."""
        self.quakes_data = {}
        (
            self.mag,
            self.long,
            self.lat,
            self.timestamp_seconds,
        ) = (
            0,
            0,
            0,
            0,
        )
        (
            self.event_title,
            self.date,
            self.title_date,
            self.formatted_plot_title,
        ) = (
            "",
            "",
            "",
            "",
        )

    def _data_lists(self):
        """Initialize the lists to store the desired data."""
        (
            self.mags,
            self.longs,
            self.lats,
            self.event_titles,
            self.event_dates,
            self.title_dates,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
        )

    def analyze_data(self, reformat_path: Optional[Path] = None):
        """Main method to analyze the earthquakes data."""
        self._read_text(reformat_path)
        self._extract_data()
        self._quakes_dataframe()

    def _read_text(self, reformat_path):
        """Try to read the earthquakes file."""
        try:
            self._reformat_file(reformat_path)
        except FileNotFoundError as err:
            warning(f"{err}")
            sys.exit()

    def _reformat_file(self, reformat_path):
        """Reformat the json file to make it readable if desired."""
        self._load_text()

        if reformat_path:
            path = Path(reformat_path)
            readable_contents = json.dumps(self.quakes_data, indent=4)
            path.write_text(readable_contents, encoding="utf-8")

    def _load_text(self):
        """Convert the json file into a python object."""
        contents = self.path.read_text(encoding="utf-8")
        self.quakes_data = json.loads(contents)

    def _extract_data(self):
        """Extract the data of interest from the python object."""
        quakes = self.quakes_data["features"]

        # Extract magnitude, longitude, latitude, title and date for each earthquake
        #   only if the magnitude is not negative.
        for quake in quakes:
            if quake["properties"]["mag"] >= 0:
                try:
                    self._collect_data(quake)
                except KeyError as ke:
                    warning(f"{ke} missing in eartquake: {quake}.")
                    sys.exit()
                else:
                    self._get_quakes_date()
                    self._append_data()

        self._format_title()

    def _collect_data(self, quake: dict):
        """Collect the data of interest."""
        self.mag = quake["properties"]["mag"]
        self.long = quake["geometry"]["coordinates"][0]
        self.lat = quake["geometry"]["coordinates"][1]
        self.event_title = quake["properties"]["title"]
        self.timestamp_seconds = quake["properties"]["time"] / 1000

    def _get_quakes_date(self):
        """Get the date of each earthquake and format it."""
        utc_timezone = timezone.utc
        quake_datetime = datetime.fromtimestamp(self.timestamp_seconds, utc_timezone)
        # Format the date for the label of each earthquake.
        self.date = quake_datetime.strftime("%B %d, %Y -- %H:%M:%S %Z (24-Hour format)")
        # Format the date for the plot title.
        self.title_date = quake_datetime.strftime("%B %Y")

    def _append_data(self):
        """Store the collected data in lists."""
        self.mags.append(self.mag)
        self.longs.append(self.long)
        self.lats.append(self.lat)
        self.event_titles.append(self.event_title)
        self.event_dates.append(self.date)
        if self.title_date not in self.title_dates:
            self.title_dates.append(self.title_date)

    def _format_title(self):
        """Neatly format the plot title."""
        self._adjust_title_dates()

        quakes_title = self.quakes_data["metadata"]["title"].split(", ")
        self.formatted_plot_title = (
            f"{quakes_title[0]} ({" - ".join(self.title_dates)})"
        )

    def _adjust_title_dates(self):
        """
        Adjust the title_dates list so the plot title can then be displayed
        as (Month, Month Year).
        """
        if len(self.title_dates) == 2:
            self.title_dates.reverse()
            first_date_split = self.title_dates[0].split(" ")
            self.title_dates[0] = first_date_split[0]

    def _quakes_dataframe(self):
        """Make a dataframe of the earthquakes data."""
        quakes_df = {
            "Magnitude": self.mags,
            "Latitude": self.lats,
            "Longitude": self.longs,
            "Event Title": self.event_titles,
            "Date": self.event_dates,
        }

        self.dataframe = pd.DataFrame(quakes_df)

    def plot_quakes(self, quakes_color: str, title_color: Optional[str] = None):
        """Plot the earthquakes."""
        fig = px.scatter_geo(
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

    def _update_fig_title(self, fig, title_color):
        """Update the layout of the title."""
        fig.update_layout(
            title={
                "text": self.formatted_plot_title,
                "font": {"color": title_color},
                "y": 0.95,
                "x": 0.48,
            }
        )
