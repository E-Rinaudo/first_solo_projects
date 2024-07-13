from typing import Any
import pytest
from unittest.mock import patch
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

from weather_data_plotter import WeatherDataPlotter as WDP


@pytest.fixture
def weather_plotter() -> WDP:
    """An instance of the weather class available to all test functions."""
    weather_plotter = WDP(title="Weather Test", title_color="red")
    return weather_plotter


@pytest.fixture
def path() -> Path:
    """A path object available for all tests."""
    path = Path("weather_data/madrid_weather_2023_F_in.csv")
    return path


@pytest.fixture
def header_row() -> list[str]:
    """The header row of the file available for all tests."""
    header_row = ["STATION", "NAME", "DATE", "PRCP", "TMAX", "TMIN"]
    return header_row


@pytest.fixture
def first_row() -> list[str]:
    """The first row of the file available for all tests."""
    first_row = ["SPE00120278", "MADRID BARAJAS, SP", "2023-01-01", "0.00", "62", "39"]
    return first_row


@pytest.fixture
def dataset(weather_plotter, path) -> dict[Any, Any]:
    """A plotter dataset available for all tests."""
    weather_plotter.weather_dataset(
        path, high=True, color="red", alpha=0.7, temp_scale="F°"
    )
    return weather_plotter.dataset


def test_dataset_gets_filled(path, dataset):
    """Test if the dataset is filled with the data passed in the dataset method above."""
    assert dataset["path"] == path
    assert dataset["high"] == True
    assert dataset["low"] == dataset["precip"] == False
    assert dataset["color"] == "red"
    assert dataset["alpha"] == 0.7
    assert dataset["temp_scale"] == "F°"
    assert dataset["precip_scale"] == "cm"


def test_read_file_not_found(weather_plotter, dataset):
    """Test if the system exits after a FileNotFound error."""
    dataset["path"] = Path("foo.csv")
    with pytest.raises(SystemExit):
        weather_plotter._read_file()


def test_is_file_read(weather_plotter, dataset, header_row):
    """Test if the file is read correctly and therefore the indices are collected."""
    weather_plotter._read_file()

    assert dataset["name_index"] == header_row.index("NAME")
    assert dataset["date_index"] == header_row.index("DATE")
    assert dataset["high_index"] == header_row.index("TMAX")
    assert dataset["low_index"] == 0
    assert dataset["precip_index"] == 0


def test_exit_if_no_data(weather_plotter, dataset, header_row):
    """Test if the system exits if the header_row is missing the required data."""
    header_row_copy_1 = header_row.copy()
    header_row_copy_1.remove("DATE")
    with pytest.raises(SystemExit):
        weather_plotter._get_data_indices(header_row_copy_1)

    header_row_copy_2 = header_row.copy()
    header_row_copy_2.remove("NAME")
    with pytest.raises(SystemExit):
        weather_plotter._get_data_indices(header_row_copy_2)

    header_row_copy_3 = header_row.copy()
    header_row_copy_3.remove("TMAX")
    with pytest.raises(SystemExit):
        weather_plotter._get_data_indices(header_row_copy_3)


def test_collect_values(dataset, first_row):
    """Test if the data is being extracted and then collected correctly."""
    date = datetime.strptime(first_row[2], "%Y-%m-%d")

    assert dataset["loc_name"] == first_row[1]
    assert date in dataset["dates"]
    assert float(first_row[-2]) in dataset["weather_data"]["highs"]
    assert float(first_row[-1]) not in dataset["weather_data"]["lows"]
    assert (
        dataset["weather_data"]["lows"]
        == dataset["weather_data"]["precipitations"]
        == []
    )


def test_does_it_plot(weather_plotter, dataset):
    """Test if the methods used to plot the weather get called."""
    with patch.object(weather_plotter.ax, "plot") as make_plot:
        weather_plotter._make_plot(shade_between=True)
        assert make_plot.called, "_make_plot was not called."
        plt.close("all")


def test_shade_between(weather_plotter, dataset):
    """Test if fill_between doesn't get called when shade_between is False."""
    with patch.object(weather_plotter.ax, "fill_between") as fill_between:
        weather_plotter.plot_visual(shade_between=False)
        assert not fill_between.called, "_fill_between was called."


def test_is_title_customized(weather_plotter, dataset):
    """Test if the title gets formatted correctly."""
    formatted_title = weather_plotter._format_plot_title()
    title = "Madrid Barajas, SP"
    assert formatted_title == title

    title = weather_plotter.title
    title += "\nMadrid Barajas, SP"
    weather_plotter._customize_title()
    actual_title = weather_plotter.ax.get_title()
    assert actual_title == title


def test_axis_labels(weather_plotter, dataset):
    """Test if the axes correctly displays their labels."""
    weather_plotter._make_plot(shade_between=False)

    weather_plotter._customize_x_axis()
    xlabel = weather_plotter.ax.get_xlabel()
    assert xlabel == ""

    weather_plotter._customize_y_axis(y_limit=None)
    ylabel = weather_plotter.ax.get_ylabel()
    assert ylabel == f"Temperature ({dataset["temp_scale"]})"


def test_legend(weather_plotter, dataset):
    """Test if the legend is displayed correctly."""
    weather_plotter._make_plot(shade_between=False)
    weather_plotter._customize_extras()
    legend = weather_plotter.ax.get_legend()
    assert legend
