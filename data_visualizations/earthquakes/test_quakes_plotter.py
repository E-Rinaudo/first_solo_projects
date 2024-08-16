#!/usr/bin/env python3

"""This module tests the 'EarthquakesPlotter' class to ensure it works as expected."""

from pathlib import Path
from datetime import datetime, timezone
from typing import Any
import pytest

from quakes_plotter import EarthquakesPlotter as EP


@pytest.fixture(name="path")
def path_fixture() -> Path:
    """A path object available for all tests."""
    return Path("earthquakes_files/significant_month.geojson")


@pytest.fixture(name="quakes_plotter")
def quakes_plotter_fixture(path: Path) -> EP:
    """An instance of the earthquakes class available to all test functions."""
    quakes_plotter = EP(path)
    return quakes_plotter


@pytest.fixture(name="quake_dictionary")
def quake_dictionary_fixture() -> dict[str, Any]:
    """A mock of an earthquake dictionary available for all tests."""
    quake_dictionary = {
        "properties": {
            "mag": 7.1,
            "time": 1720663997513,
            "title": "M 7.1 - 106 km WSW of Sangay, Philippines",
        },
        "geometry": {"coordinates": [123.1605, 6.0646]},
    }
    return quake_dictionary


def test_read_file_not_found() -> None:
    """Test if the system exits after a FileNotFound error."""
    with pytest.raises(SystemExit):
        foo_plot = EP(Path("foo.geojson"))
        foo_plot.analyze_data()


def test_is_readable_written(path: Path) -> None:
    """Test if the readable geojson file is written."""
    reformat_path = Path("earthquakes_files/significant_month_readable.geojson")
    reformat_plot = EP(path)
    reformat_plot.analyze_data(reformat_path)

    assert reformat_path.exists()


def test_do_data_get_extracted(
    quakes_plotter: EP, quake_dictionary: dict[str, Any]
) -> None:
    """Test if the data get extracted."""
    quakes = [quake_dictionary, quake_dictionary]
    quakes_plotter._data_lists()

    quakes_plotter.quakes_data = {
        "features": quakes,
        "metadata": {"title": "Test Earthquake Data"},
    }

    quakes_plotter._extract_data()

    assert quake_dictionary["properties"]["mag"] in quakes_plotter.mags
    assert quake_dictionary["geometry"]["coordinates"][0] in quakes_plotter.longs
    assert quake_dictionary["geometry"]["coordinates"][1] in quakes_plotter.lats
    assert quake_dictionary["properties"]["title"] in quakes_plotter.event_titles


def test_is_date_formatted(
    quakes_plotter: EP, quake_dictionary: dict[str, Any]
) -> None:
    """Test if the date of the earthquake event is formatted."""
    quakes_plotter.analyze_data()

    utc_timezone = timezone.utc
    date = quake_dictionary["properties"]["time"] / 1000
    date_datetime = datetime.fromtimestamp(date, utc_timezone)
    formatted_date = date_datetime.strftime("%B %d, %Y -- %H:%M:%S %Z (24-Hour format)")
    assert formatted_date in quakes_plotter.event_dates


def test_is_negative_mag_appended(
    quakes_plotter: EP, quake_dictionary: dict[str, Any]
) -> None:
    """Assure negative magnitude values are not appended in the mags list."""
    negative_quake = {
        "properties": {
            "mag": -7.1,
            "time": 1720663997513,
            "title": "M -7.1 - 106 km WSW of Sangay, Philippines",
        },
        "geometry": {"coordinates": [123.1605, 6.0646]},
    }
    quakes_plotter.quakes_data = {
        "features": [quake_dictionary, negative_quake],
        "metadata": {"title": "Test Earthquake Data"},
    }
    quakes_plotter._data_lists()
    quakes_plotter._extract_data()

    assert negative_quake["properties"]["mag"] not in quakes_plotter.mags
    assert quake_dictionary["properties"]["mag"] in quakes_plotter.mags
