#!/usr/bin/env python3

"""
This module imports the 'EarthquakesPlotter' class to plot and visualize
all the earthquakes from mid-June to mid-July, 2024.
"""

from pathlib import Path

from quakes_plotter import EarthquakesPlotter as EP


if __name__ == "__main__":
    # Make the instance and visualize the data.
    path = Path("earthquakes_files/all_month.geojson")
    reformat_path = Path("earthquakes_files/all_month_readable.geojson")

    quakes_plotter = EP(path=path)
    quakes_plotter.analyze_data()
    quakes_plotter.plot_quakes(quakes_color="Cividis")
