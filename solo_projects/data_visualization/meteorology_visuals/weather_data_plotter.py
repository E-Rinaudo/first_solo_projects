import sys
from typing import Any, Literal, Iterable, Optional
from pathlib import Path
import csv
from datetime import datetime
from logging import warning

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


FONT_SIZE_TITLE = 11
FONT_SIZE_LABELS = 10
FONT_SIZE_TICKS = 9
FONT_SIZE_LEGEND = 8
DATE_FORMAT = "%Y-%m-%d"


class WeatherDataPlotter:
    """Plot and visualize weather data."""

    def __init__(self, title: str = "", title_color: str = ""):
        """Initialize the weather plot attributes."""
        self.title = title
        self.title_color = title_color

        plt.style.use("seaborn-v0_8")
        self.fig, self.ax = plt.subplots(figsize=(14, 5.5), dpi=130)

        # Initialize a list to store the dataset dictionary.
        self.datasets: list[dict[Any, Any]] = []

    def weather_dataset(
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
    ):
        """Make a dictionary to store the data needed for the visualization."""
        self.dataset: dict[Any, Any] = {
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
            "weather_data": {"highs": [], "lows": [], "precipitations": []},
            "date_index": 0,
            "name_index": 0,
            "high_index": 0,
            "low_index": 0,
            "precip_index": 0,
        }

        self._read_file()
        # Store the data in the datasets dictionary. Used to generate the visualization.
        self.datasets.append(self.dataset)

    def _read_file(self):
        """Read the weather file."""
        try:
            lines = self.dataset["path"].read_text().splitlines()
        except FileNotFoundError as fne:
            warning(f" {fne}")
            sys.exit()
        else:
            reader = csv.reader(lines)
            header_row = next(reader)

            self._get_data_indices(header_row)
            self._extract_data(reader)

    def _get_data_indices(self, header_row: list[str]):
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

    def _extract_data(self, reader: Iterable[list[str]]):
        """Determine which data is needed for the plot and extract them."""
        for row in reader:
            self._extract_station_name(row)
            date = self._extract_date(row)
            self._extract_weather_data(row, date)

    def _extract_station_name(self, row: list[str]):
        """Extract the name of the weather station from the row."""
        if not self.dataset["loc_name"]:
            self.dataset["loc_name"] = row[self.dataset["name_index"]]

    def _extract_date(self, row: list[str]) -> datetime:
        """Extract the dates of the recording from the row."""
        date = datetime.strptime(row[self.dataset["date_index"]], DATE_FORMAT)
        return date

    def _extract_weather_data(self, row: list[str], date: datetime):
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

    def _collect_data(
        self, row: list[str], data_1: str, data_2: str, index: int, date: datetime
    ):
        """Collect the specified data in the _extract methods and store them."""
        try:
            values = self._collect_values(row, data_1, data_2, index)
        except ValueError as ve:
            warning(f" Missing data for {date}: {ve}")
        else:
            self._store_collected_values(data_1, data_2, date, values)

    def _collect_values(
        self, row: list[str], data_1: str, data_2: str, index: int
    ) -> list[float]:
        """Collect the specified weather data values from the row."""
        values = []

        if data_1 == "highs" and data_2 == "lows":
            for data_index in ("high_index", "low_index"):
                values.append(float(row[self.dataset[data_index]]))
        elif data_1 == "highs" or data_1 == "lows" or data_1 == "precipitations":
            values.append(float(row[index]))

        return values

    def _store_collected_values(
        self, data_1: str, data_2: str, date: datetime, values: list[float]
    ):
        """Store the collected weather data values in the dataset dictionary."""
        self.dataset["dates"].append(date)
        if data_1 == "highs" and data_2 == "lows":
            for data, value in [(data_1, values[0]), (data_2, values[1])]:
                self._append_data(data, value)
        elif (
            data_1 == "highs" or data_1 == "lows" or data_1 == "precipitations"
        ) and not data_2:
            self._append_data(data_1, values[0])

    def _append_data(self, data_key: str, value: float):
        """Append the weather data value to the specific list in the dataset."""
        self.dataset["weather_data"][data_key].append(value)

    def plot_visual(
        self, shade_between: bool = True, y_limit: Optional[tuple[float, float]] = None
    ):
        """Generate and visualize the plot using the data previously extracted."""
        for self.dataset in self.datasets:
            self._make_plot(shade_between)

        self._customize_plot(y_limit)
        plt.show()

    def _make_plot(self, shade_between: bool):
        """Make the plot for the data of interest."""
        weather_data, highs, lows, precips, color, alpha = self._set_plot_variables()

        if self.dataset["high"] and self.dataset["low"]:
            self._plot_weather(
                [highs, lows], weather_data, ["red", "blue"], alpha, shade_between
            )
        else:
            if self.dataset["high"] and not self.dataset["low"]:
                weather_name = highs
            elif self.dataset["low"] and not self.dataset["high"]:
                weather_name = lows
            elif self.dataset["precip"]:
                weather_name = precips

            self._plot_weather(
                [weather_name],
                weather_data,
                [color],
                alpha,
                shade_between,
            )

    def _set_plot_variables(
        self,
    ) -> tuple[dict[str, list[float]], str, str, str, str, float]:
        """Store the variables needed to make the plot."""
        # Set a variable for the dictionary of the weather data.
        weather_data = self.dataset["weather_data"]
        # List the keys of the weather data dictionary. Used with the
        #   variable above to determine which specific weather data to plot.
        weather_data_keys = list(weather_data.keys())
        highs, lows, precips = (
            weather_data_keys[0],
            weather_data_keys[1],
            weather_data_keys[2],
        )
        color = self.dataset["color"]
        alpha = self.dataset["alpha"]

        return weather_data, highs, lows, precips, color, alpha

    def _plot_weather(
        self,
        weather_names: list[str],
        weather_data: dict[str, list[float]],
        colors: list[str],
        alpha: float,
        shade_between: bool,
    ):
        """Plot the weather data and shade between them if desired."""
        for weather_name, color in zip(weather_names, colors):
            self._plot_weather_data(
                weather_name, weather_data[weather_name], color, alpha
            )
        if shade_between:
            if len(weather_names) == 2:
                self._fill_between(
                    weather_data[weather_names[0]],
                    weather_data[weather_names[1]],
                    facecolor="blue",
                )
            elif len(weather_names) == 1:
                self._fill_between(
                    weather_data[weather_names[0]],
                    weather_data_2=[0],
                    facecolor=colors[0],
                )

    def _plot_weather_data(
        self, weather_name: str, weather_data: list[float], color: str, alpha: float
    ):
        """Plot the weather data."""
        self.ax.plot(
            self.dataset["dates"],
            weather_data,
            color=color,
            alpha=alpha,
            label=f"{self.dataset["label"]} {weather_name.title()}",
        )

    def _fill_between(
        self, weather_data_1: list[float], weather_data_2: list[float], facecolor: str
    ):
        """Fill the area inside the weather data."""
        self.ax.fill_between(
            self.dataset["dates"],
            y1=weather_data_1,
            y2=weather_data_2,
            facecolor=facecolor,
            alpha=0.3,
        )

    def _customize_plot(self, y_limit: Optional[tuple[float, float]]):
        """Customize the plot."""
        self._customize_title()
        self._customize_x_axis()
        self._customize_y_axis(y_limit)
        self._customize_extras()

    def _customize_title(self):
        """Customize the title."""
        formatted_name = self._format_plot_title()
        title = self.title
        title += f"\n{formatted_name}"
        self.ax.set_title(title, color=self.title_color, fontsize=FONT_SIZE_TITLE)

    def _format_plot_title(self) -> str:
        """Return a neatly formatted string of the location name for the title."""
        loc_names = [dataset["loc_name"].split(", ") for dataset in self.datasets]
        formatted_names = [f"{loc[0].title()}, {loc[1]}" for loc in loc_names]
        formatted_name = "\n".join(formatted_names)
        return formatted_name

    def _customize_x_axis(self):
        """Customize the x axis."""
        self.ax.set_xlabel("", fontsize=FONT_SIZE_LABELS)
        # Display the dates at intervals of 1 month.
        self.ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
        # Display the date as Month Year.
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
        self.fig.autofmt_xdate()

    def _customize_y_axis(self, y_limit: Optional[tuple[float, float]]):
        """Customize the y axis."""
        if self.dataset["high"] or self.dataset["low"]:
            self.ax.set_ylabel(
                f"Temperature ({self.dataset["temp_scale"]})", fontsize=FONT_SIZE_LABELS
            )
        elif self.dataset["precip"]:
            self.ax.set_ylabel(
                f"Precipitation Amount ({self.dataset["precip_scale"]})",
                fontsize=FONT_SIZE_LABELS,
            )
        if y_limit is not None:
            self.ax.set_ylim(*y_limit)

    def _customize_extras(self):
        """Extra customizations for the plot."""
        self.ax.grid(True, linestyle="--")
        self.ax.tick_params(labelsize=FONT_SIZE_TICKS)
        self.ax.legend(loc="upper left", fontsize=FONT_SIZE_LEGEND)
