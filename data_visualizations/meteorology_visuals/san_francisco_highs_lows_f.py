#!/usr/bin/env python3

"""
This module imports the 'WeatherDataPlotter' class to plot and visualize
the high and low temperatures (F°) for San Francisco (CA, US) in 2000.
"""

from pathlib import Path

from weather_data_plotter import WeatherDataPlotter as WDP


if __name__ == "__main__":
    # Create a plotter instance.
    weather_plotter: WDP = WDP(title="Daily High and Low Temperatures, 2000")

    # Add data for San Francisco to the plotter dataset.
    path: Path = Path("weather_data", "san_francisco_weather_2000_f_in.csv")

    weather_plotter.weather_dataset(
        path=path,
        high=True,
        low=True,
        label="San Francisco",
        temp_scale="F°",
    )

    # Generate the visualization.
    weather_plotter.plot_visual()
