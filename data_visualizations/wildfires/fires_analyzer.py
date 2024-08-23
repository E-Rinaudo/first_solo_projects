#!/usr/bin/env python3

"""
This module defines the 'WildfirePlotter' class to visualize wildfire activity
in North America (July 12, 2024 to July 14, 2024).

It reads data from a CSV file, formats the dates and times,
and creates a geographical scatter plot to visualize wildfire locations
and brightness using Plotly.
"""

from datetime import datetime

import pandas as pd
import plotly.graph_objects as go


class WildfirePlotter:
    """A class to visualize wildfire activity in North America."""

    def __init__(self, path: str) -> None:
        """Initialize the class attributes, read the csv file and plot the data."""
        self.path = path
        self.acq_times: list[str] = []
        self.acq_dates: list[str] = []
        self.fires_data: pd.DataFrame = pd.DataFrame()

    def read_file(self) -> None:
        """Read the csv file."""
        self.fires_data = pd.read_csv(self.path)

    def visualize_plot(self) -> None:
        """Visualize wildfire activity."""
        self._format_label_text()
        # Lower the brightness value to use it as a size in the plot.
        bright_size: list[int] = [
            bright // 18 for bright in self.fires_data["brightness"]
        ]

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

    def _format_label_text(self) -> None:
        """Combine the date, time and brightness into a text for the plot label."""
        self._format_date()
        self._format_time()

        self.fires_data["text"] = [
            f"Acquisition Date: {date} -- {time} -- Brightness: {brightness}"
            for date, time, brightness in zip(
                self.acq_dates,
                self.acq_times,
                self.fires_data["brightness"].astype(str),
            )
        ]

    def _format_date(self) -> None:
        """Format the data acquisition date to neatly display it."""
        df_dates: list[str] = list(self.fires_data["acq_date"])

        for df_date in df_dates:
            datetime_date: datetime = datetime.strptime(df_date, "%Y-%m-%d")
            formatted_date: str = datetime_date.strftime("%B %d, %Y")
            self.acq_dates.append(formatted_date)

    def _format_time(self) -> None:
        """Format the data acquisition time to neatly display it."""
        df_times: list[str] = list(self.fires_data["acq_time"])

        for df_time in df_times:
            time_str: str = str(df_time).zfill(4)
            datetime_time: datetime = datetime.strptime(time_str, "%H%M")
            formatted_time: str = datetime_time.strftime("%H:%M (24 HR Format)")
            self.acq_times.append(formatted_time)

    def _update_plot(self, fig: go.Figure) -> None:
        """Customize the plot."""
        title: str = "USA Contiguous and Hawaii Wildfire Activity "
        title += f"({self.acq_dates[0]} to {self.acq_dates[-1]})"

        fig.update_layout(
            geo={
                "scope": "north america",
                "resolution": 50,
                "projection": {"type": "conic conformal", "rotation_lon": -100},
                "lonaxis": {
                    "showgrid": True,
                    "gridwidth": 0.5,
                    "range": [-180.0, -20.0],
                    "dtick": 5,
                },
                "lataxis": {
                    "showgrid": True,
                    "gridwidth": 0.5,
                    "range": [10.0, 50.0],
                    "dtick": 5,
                },
            },
            title=title,
        )


if __name__ == "__main__":
    # Give a path and make the instance to visualize the data.
    PATH = "fires_file/MODIS_C6_1_USA_contiguous_and_Hawaii_3d.csv"
    wildfire = WildfirePlotter(PATH)
    wildfire.read_file()
    wildfire.visualize_plot()
