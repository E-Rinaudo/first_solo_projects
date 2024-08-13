#!/usr/bin/env python3

"""
This module imports the 'WeatherDataPlotter' class to plot and visualize
the low temperatures (C°) for Madrid (SP) in 2023.
"""

from pathlib import Path

from weather_data_plotter import WeatherDataPlotter as WDP


if __name__ == "__main__":
    # Create a plotter instance.
    weather_plotter = WDP(title="Daily Low Temperatures, 2023")

    # Add data for Madrid to the plotter dataset.
    path = Path("weather_data/madrid_weather_2023_c_cm.csv")

    weather_plotter.weather_dataset(
        path=path,
        low=True,
        color="blue",
        label="Madrid",
    )

    # Generate the visualization.
    weather_plotter.plot_visual()
