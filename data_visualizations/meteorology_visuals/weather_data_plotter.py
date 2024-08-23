#!/usr/bin/env python3

"""
This module defines the 'WeatherDataPlotter' class to analyze, plot and visualize
weather data using matplotlib.pyplot.

The class allows to:
- Import weather data from CSV files.
- Extract and process high and low temperatures, as well as precipitation data.
- Generate and customize plots to visualize the data.
"""

import sys
from typing import TypedDict, Literal, Iterator, Optional, Union
from pathlib import Path
import csv
from datetime import datetime
from logging import warning

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.figure import Figure


FONT_SIZE_TITLE: int = 11
FONT_SIZE_LABELS: int = 10
FONT_SIZE_TICKS: int = 9
FONT_SIZE_LEGEND: int = 8
DATE_FORMAT: str = "%Y-%m-%d"


class WeatherDataset(TypedDict):
    """A TypedDict used as a type annotation class to describe the weather dataset."""

    path: Path
    high: bool
    low: bool
    precip: bool
    color: str
    alpha: float
    label: str
    temp_scale: Literal["C°", "F°"]
    precip_scale: Literal["cm", "in"]
    dates: list[datetime]
    loc_name: str
    weather_info: dict[str, list[float]]
    date_index: int
    name_index: int
    high_index: int
    low_index: int
    precip_index: int


class WeatherDataPlotter:
    """Plot and visualize weather data."""

    def __init__(self, title: str = "", title_color: str = "k") -> None:
        """Initialize the weather plot attributes."""
        self.title = title
        self.title_color = title_color
        self.dataset: WeatherDataset = {}  # type: ignore
        self.datasets: list[WeatherDataset] = []

        plt.style.use("seaborn-v0_8")
        self.fig: Figure
        self.ax: plt.Axes
        self.fig, self.ax = plt.subplots(figsize=(14, 5.5), dpi=130)

    def weather_dataset(  # pylint: disable=R0913
        self,
        path: Path,
        high: bool = False,
        low: bool = False,
        precip: bool = False,
        color: str = "",
        alpha: float = 1.0,
        label: str = "",
        temp_scale: Literal["C°", "F°"] = "C°",
        precip_scale: Literal["cm", "in"] = "cm",
    ) -> None:
        """Make a dictionary to store the data needed for the visualization."""
        self.dataset = {
            "path": path,
            "high": high,
            "low": low,
            "precip": precip,
            "color": color,
            "alpha": alpha,
            "label": label,
            "temp_scale": temp_scale,
            "precip_scale": precip_scale,
            "dates": [],
            "loc_name": "",
            "weather_info": {"highs": [], "lows": [], "precipitations": []},
            "date_index": 0,
            "name_index": 0,
            "high_index": 0,
            "low_index": 0,
            "precip_index": 0,
        }

        self._read_file()
        # Store the data in the datasets dictionary. Used to generate the visualization.
        self.datasets.append(self.dataset)

    def _read_file(self) -> None:
        """Read the weather file."""
        try:
            lines: list[str] = self.dataset["path"].read_text().splitlines()
        except FileNotFoundError as fne:
            warning(f" {fne}")
            sys.exit()
        else:
            reader: Iterator[list[str]] = csv.reader(lines)
            header_row: list[str] = next(reader)

            self._get_data_indices(header_row)
            self._extract_data(reader)

    def _get_data_indices(self, header_row: list[str]) -> None:
        """Get the indices of the weather data."""
        try:
            self.dataset["date_index"] = header_row.index("DATE")
            self.dataset["name_index"] = header_row.index("NAME")

            if self.dataset["high"]:
                self.dataset["high_index"] = header_row.index("TMAX")
            if self.dataset["low"]:
                self.dataset["low_index"] = header_row.index("TMIN")
            if self.dataset["precip"]:
                self.dataset["precip_index"] = header_row.index("PRCP")
        except ValueError as ve:
            warning(f" {ve}")
            sys.exit()

    def _extract_data(self, reader: Iterator[list[str]]) -> None:
        """Determine which data is needed for the plot and extract them."""
        for row in reader:
            self._extract_station_name(row)
            date = self._extract_date(row)
            self._extract_weather_data(row, date)

    def _extract_station_name(self, row: list[str]) -> None:
        """Extract the name of the weather station from the row."""
        if not self.dataset["loc_name"]:
            self.dataset["loc_name"] = row[self.dataset["name_index"]]

    def _extract_date(self, row: list[str]) -> datetime:
        """Extract the dates of the recording from the row."""
        date: datetime = datetime.strptime(row[self.dataset["date_index"]], DATE_FORMAT)
        return date

    def _extract_weather_data(self, row: list[str], date: datetime) -> None:
        """Determine the weather data of interest and extract them."""
        if self.dataset["high"] and self.dataset["low"]:
            self._collect_data(row, "highs", "lows", 0, date)
        elif self.dataset["high"] and not self.dataset["low"]:
            self._collect_data(row, "highs", "", self.dataset["high_index"], date)
        elif self.dataset["low"] and not self.dataset["high"]:
            self._collect_data(row, "lows", "", self.dataset["low_index"], date)
        elif self.dataset["precip"]:
            self._collect_data(
                row, "precipitations", "", self.dataset["precip_index"], date
            )

    def _collect_data(  # pylint: disable=R0913
        self,
        row: list[str],
        weather_type_1: str,
        weather_type_2: str,
        weather_type_index: int,
        date: datetime,
    ) -> None:
        """Collect the specified data in the _extract methods and store them."""
        try:
            values: list[float] = self._collect_values(
                row, weather_type_1, weather_type_2, weather_type_index
            )
        except ValueError as ve:
            warning(f" Missing data for {date}: {ve}")
        else:
            self._store_collected_values(weather_type_1, weather_type_2, date, values)

    def _collect_values(
        self,
        row: list[str],
        weather_type_1: str,
        weather_type_2: str,
        weather_type_index: int,
    ) -> list[float]:
        """Collect the specified weather data values from the row."""
        values: list[float] = []

        if weather_type_1 == "highs" and weather_type_2 == "lows":
            for weather_index in ("high_index", "low_index"):
                values.append(float(row[self.dataset[weather_index]]))  # type: ignore
        elif weather_type_1 in ("highs", "lows", "precipitations"):
            values.append(float(row[weather_type_index]))

        return values

    def _store_collected_values(
        self,
        weather_type_1: str,
        weather_type_2: str,
        date: datetime,
        values: list[float],
    ) -> None:
        """Store the collected weather data values in the dataset dictionary."""
        self.dataset["dates"].append(date)
        if weather_type_1 == "highs" and weather_type_2 == "lows":
            for weather_type, value in [
                (weather_type_1, values[0]),
                (weather_type_2, values[1]),
            ]:
                self._append_data(weather_type, value)
        elif (
            weather_type_1 in ("highs", "lows", "precipitations")
        ) and not weather_type_2:
            self._append_data(weather_type_1, values[0])

    def _append_data(self, weather_type: str, value: float) -> None:
        """Append the weather data value to the specific list in the dataset."""
        self.dataset["weather_info"][weather_type].append(value)

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

    def _make_plot(self, shade_between: bool) -> None:
        """Make the plot for the data of interest."""
        weather_info_dict, highs, lows, precips, color, alpha = (
            self._set_plot_variables()
        )

        if self.dataset["high"] and self.dataset["low"]:
            self._plot_weather(
                [highs, lows], weather_info_dict, ["red", "blue"], alpha, shade_between
            )
        else:
            if self.dataset["high"] and not self.dataset["low"]:
                weather_type: str = highs
            elif self.dataset["low"] and not self.dataset["high"]:
                weather_type = lows
            elif self.dataset["precip"]:
                weather_type = precips

            self._plot_weather(
                [weather_type],
                weather_info_dict,
                [color],
                alpha,
                shade_between,
            )

    def _set_plot_variables(
        self,
    ) -> tuple[dict[str, list[float]], str, str, str, str, float]:
        """Store the variables needed to make the plot."""
        # Set a variable for the dictionary of the weather data.
        weather_info_dict: dict[str, list[float]] = self.dataset["weather_info"]
        # List the keys of the weather data dictionary. Used with the
        #   variable above to determine which specific weather data to plot.
        weather_info_dict_keys: list[str] = list(weather_info_dict.keys())
        highs: str = weather_info_dict_keys[0]
        lows: str = weather_info_dict_keys[1]
        precips: str = weather_info_dict_keys[2]
        color: str = self.dataset["color"]
        alpha: float = self.dataset["alpha"]

        return weather_info_dict, highs, lows, precips, color, alpha

    def _plot_weather(  # pylint: disable=R0913
        self,
        weather_types: list[str],
        weather_info_dict: dict[str, list[float]],
        colors: list[str],
        alpha: float,
        shade_between: bool,
    ) -> None:
        """Plot the weather data and shade between them if desired."""
        for weather_type, color in zip(weather_types, colors):
            self._plot_weather_data(
                weather_type, weather_info_dict[weather_type], color, alpha
            )
        if shade_between:
            if len(weather_types) == 2:
                self._fill_between(
                    weather_info_dict[weather_types[0]],
                    weather_info_dict[weather_types[1]],
                    facecolor="blue",
                )
            elif len(weather_types) == 1:
                self._fill_between(
                    weather_info_dict[weather_types[0]],
                    weather_info_list_2=[0],
                    facecolor=colors[0],
                )

    def _plot_weather_data(
        self,
        weather_type: str,
        weather_info_list: list[float],
        color: str,
        alpha: float,
    ) -> None:
        """Plot the weather data."""
        self.ax.plot(
            self.dataset["dates"],
            weather_info_list,
            color=color,
            alpha=alpha,
            label=f"{self.dataset["label"]} {weather_type.title()}",
        )

    def _fill_between(
        self,
        weather_info_list_1: list[float],
        weather_info_list_2: list[float],
        facecolor: str,
    ) -> None:
        """Fill the area inside the weather data."""
        self.ax.fill_between(
            self.dataset["dates"],
            y1=weather_info_list_1,  # type: ignore
            y2=weather_info_list_2,  # type: ignore
            facecolor=facecolor,
            alpha=0.3,
        )

    def _customize_plot(
        self, y_limit: Optional[tuple[Union[float, int], Union[float, int]]]
    ) -> None:
        """Customize the plot."""
        self._customize_title()
        self._customize_x_axis()
        self._customize_y_axis(y_limit)
        self._customize_extras()

    def _customize_title(self) -> None:
        """Customize the title."""
        formatted_name = self._format_plot_title()
        title: str = self.title
        title += f"\n{formatted_name}"
        self.ax.set_title(title, color=self.title_color, fontsize=FONT_SIZE_TITLE)

    def _format_plot_title(self) -> str:
        """Return a neatly formatted string of the location name for the title."""
        loc_names: list[list[str]] = [
            dataset["loc_name"].split(", ") for dataset in self.datasets
        ]
        formatted_names: list[str] = [
            f"{loc[0].title()}, {loc[1]}" for loc in loc_names
        ]
        formatted_name: str = "\n".join(formatted_names)
        return formatted_name

    def _customize_x_axis(self) -> None:
        """Customize the x axis."""
        self.ax.set_xlabel("", fontsize=FONT_SIZE_LABELS)
        # Display the dates at intervals of 1 month.
        self.ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
        # Display the date as Month Year.
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
        self.fig.autofmt_xdate()

    def _customize_y_axis(
        self, y_limit: Optional[tuple[Union[float, int], Union[float, int]]]
    ) -> None:
        """Customize the y axis."""
        if self.dataset["high"] or self.dataset["low"]:
            self.ax.set_ylabel(
                f"Temperature ({self.dataset["temp_scale"]})",
                fontsize=FONT_SIZE_LABELS,
                labelpad=10,
            )
        elif self.dataset["precip"]:
            self.ax.set_ylabel(
                f"Precipitation Amount ({self.dataset["precip_scale"]})",
                fontsize=FONT_SIZE_LABELS,
                labelpad=10,
            )
        if y_limit is not None:
            self.ax.set_ylim(*y_limit)

    def _customize_extras(self) -> None:
        """Extra customizations for the plot."""
        self.ax.grid(True, linestyle="--")
        self.ax.tick_params(labelsize=FONT_SIZE_TICKS)
        self.ax.legend(loc="upper left", fontsize=FONT_SIZE_LEGEND)
