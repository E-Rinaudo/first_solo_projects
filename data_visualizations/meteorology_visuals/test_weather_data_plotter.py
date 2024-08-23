#!/usr/bin/env python3

"""This module tests the 'WeatherDataPlotter' class to ensure it works as expected."""

from typing import Any, Union
from pathlib import Path
from datetime import datetime
from unittest.mock import patch

import pytest
import matplotlib.pyplot as plt
from matplotlib.legend import Legend

from weather_data_plotter import WeatherDataPlotter as WDP
from weather_data_plotter import WeatherDataset as WD


@pytest.fixture(name="weather_plotter")
def weather_plotter_fixture() -> WDP:
    """An instance of the weather class available to all test functions."""
    return WDP(title="Weather Test", title_color="red")


@pytest.fixture(name="path")
def path_fixture() -> Path:
    """A path object available for all tests."""
    return Path("weather_data/madrid_weather_2023_F_in.csv")


@pytest.fixture(name="header_row")
def header_row_fixture() -> list[str]:
    """The header row of the file available for all tests."""
    return ["STATION", "NAME", "DATE", "PRCP", "TMAX", "TMIN"]


@pytest.fixture(name="first_row")
def first_row_fixture() -> list[str]:
    """The first row of the file available for all tests."""
    return ["SPE00120278", "MADRID BARAJAS, SP", "2023-01-01", "0.00", "62", "39"]


@pytest.fixture(name="dataset")
def dataset_fixture(weather_plotter: WDP, path: Path) -> WD:
    """A plotter dataset available for all tests."""
    weather_plotter.weather_dataset(
        path, high=True, color="red", alpha=0.7, temp_scale="F°"
    )
    return weather_plotter.dataset


def test_dataset_gets_filled(path: Path, dataset: dict[str, Any]) -> None:
    """Test if the dataset is filled with the data passed in the dataset method."""
    assert dataset["path"] == path
    assert dataset["high"]
    assert not dataset["low"]
    assert not dataset["precip"]
    assert dataset["color"] == "red"
    assert dataset["alpha"] == 0.7
    assert dataset["temp_scale"] == "F°"
    assert dataset["precip_scale"] == "cm"


def test_read_file_not_found(
    weather_plotter: WDP, dataset: dict[str, Any]  # pylint: disable=W0613
) -> None:
    """Test if the system exits after a FileNotFound error."""
    path: Path = Path("foo.csv")
    with pytest.raises(SystemExit):
        weather_plotter.weather_dataset(path)


def test_is_file_read(
    weather_plotter: WDP, path: Path, dataset: dict[str, Any], header_row: list[str]
) -> None:
    """Test if the file is read correctly and therefore the indices are collected."""
    weather_plotter.weather_dataset(path)

    assert dataset["name_index"] == header_row.index("NAME")
    assert dataset["date_index"] == header_row.index("DATE")
    assert dataset["high_index"] == header_row.index("TMAX")
    assert dataset["low_index"] == 0
    assert dataset["precip_index"] == 0


def test_exit_if_no_data(
    weather_plotter: WDP,
    dataset: dict[str, Any],  # pylint: disable=W0613
    header_row: list[str],
) -> None:
    """Test if the system exits if the header_row is missing the required data."""
    # Disabling pylint warning for accessing protected members.
    header_row_copy_1: list[str] = header_row.copy()
    header_row_copy_1.remove("DATE")
    with pytest.raises(SystemExit):
        weather_plotter._get_data_indices(header_row_copy_1)  # pylint: disable=W0212
    # Disabling pylint warning for accessing protected members.
    header_row_copy_2: list[str] = header_row.copy()
    header_row_copy_2.remove("NAME")
    with pytest.raises(SystemExit):
        weather_plotter._get_data_indices(header_row_copy_2)  # pylint: disable=W0212
    # Disabling pylint warning for accessing protected members.
    header_row_copy_3: list[str] = header_row.copy()
    header_row_copy_3.remove("TMAX")
    with pytest.raises(SystemExit):
        weather_plotter._get_data_indices(header_row_copy_3)  # pylint: disable=W0212


def test_collect_values(dataset: dict[str, Any], first_row: list[str]) -> None:
    """Test if the data is being extracted and then collected correctly."""
    date: datetime = datetime.strptime(first_row[2], "%Y-%m-%d")

    assert dataset["loc_name"] == first_row[1]
    assert date in dataset["dates"]
    assert float(first_row[-2]) in dataset["weather_info"]["highs"]
    assert float(first_row[-1]) not in dataset["weather_info"]["lows"]
    assert (
        dataset["weather_info"]["lows"]
        == dataset["weather_info"]["precipitations"]
        == []
    )


def test_does_it_plot(
    weather_plotter: WDP, dataset: dict[str, Any]  # pylint: disable=W0613
) -> None:
    """Test if the methods used to plot the weather get called."""
    # Disabling pylint warning for accessing protected members.
    with patch.object(weather_plotter.ax, "plot") as make_plot:
        weather_plotter._make_plot(shade_between=True)  # pylint: disable=W0212
        assert make_plot.called, "_make_plot was not called."
        plt.close("all")


def test_shade_between(
    weather_plotter: WDP, dataset: dict[str, Any]  # pylint: disable=W0613
) -> None:
    """Test if fill_between doesn't get called when shade_between is False."""
    with patch.object(weather_plotter.ax, "fill_between") as fill_between:
        weather_plotter.plot_visual(shade_between=False)
        assert not fill_between.called, "_fill_between was called."


def test_is_title_customized(
    weather_plotter: WDP, dataset: dict[str, Any]  # pylint: disable=W0613
) -> None:
    """Test if the title gets formatted correctly."""
    # Disabling pylint warning for accessing protected members.
    formatted_title: str = weather_plotter._format_plot_title()  # pylint: disable=W0212
    title: str = "Madrid Barajas, SP"
    assert formatted_title == title

    long_title: str = weather_plotter.title
    long_title += "\nMadrid Barajas, SP"
    # Disabling pylint warning for accessing protected members.
    weather_plotter._customize_title()  # pylint: disable=W0212
    actual_title: str = weather_plotter.ax.get_title()
    assert actual_title == long_title


def test_axis_labels(weather_plotter: WDP, dataset: dict[str, Any]) -> None:
    """Test if the axes correctly displays their labels."""
    # Disabling pylint warning for accessing protected members.
    weather_plotter._make_plot(shade_between=False)  # pylint: disable=W0212
    # Disabling pylint warning for accessing protected members.
    weather_plotter._customize_x_axis()  # pylint: disable=W0212
    xlabel: str = weather_plotter.ax.get_xlabel()
    assert xlabel == ""
    # Disabling pylint warning for accessing protected members.
    weather_plotter._customize_y_axis(y_limit=None)  # pylint: disable=W0212
    ylabel: str = weather_plotter.ax.get_ylabel()
    assert ylabel == f"Temperature ({dataset["temp_scale"]})"


def test_legend(
    weather_plotter: WDP, dataset: dict[str, Any]  # pylint: disable=W0613
) -> None:
    """Test if the legend is displayed correctly."""
    # Disabling pylint warning for accessing protected members.
    weather_plotter._make_plot(shade_between=False)  # pylint: disable=W0212
    weather_plotter._customize_extras()  # pylint: disable=W0212
    legend: Union[Legend, None] = weather_plotter.ax.get_legend()
    assert legend
