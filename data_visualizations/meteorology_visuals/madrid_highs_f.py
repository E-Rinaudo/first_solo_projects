#!/usr/bin/env python3

"""
This module imports the 'WeatherDataPlotter' class to plot and visualize
the high temperatures (F°) for Madrid (SP) in 2023.
"""

from pathlib import Path

from weather_data_plotter import WeatherDataPlotter as WDP


if __name__ == "__main__":
    # Create a plotter instance.
    weather_plotter = WDP(title="Daily High Temperatures, 2023", title_color="k")

    # Add data for Madrid to the plotter dataset.
    path = Path("weather_data/madrid_weather_2023_f_in.csv")

    weather_plotter.weather_dataset(
        path=path,
        high=True,
        color="red",
        label="Madrid",
        temp_scale="F°",
    )

    # Generate the visualization.
    weather_plotter.plot_visual(y_limit=(0, 110))
