"""
This module imports the 'WeatherDataPlotter' class to plot and visualize
the precipitation (inches) for Sitka (AK, US) and Death Valley (CA, US) in 2021.
"""

from pathlib import Path

from weather_data_plotter import WeatherDataPlotter as WDP


if __name__ == "__main__":
    # Create a plotter instance.
    weather_plotter = WDP(
        title="Daily Precipitation, 2021", title_color="mediumseagreen"
    )

    # Add data for Sitka to the plotter dataset.
    sitka_path = Path("weather_data/sitka_weather_2021_f_in.csv")

    weather_plotter.weather_dataset(
        path=sitka_path,
        precip=True,
        color="blue",
        alpha=0.3,
        label="Sitka",
    )

    # Add data for Death Valley to the plotter dataset.
    dv_path = Path("weather_data/death_valley_weather_2021_f_in.csv")

    weather_plotter.weather_dataset(
        path=dv_path,
        precip=True,
        color="green",
        alpha=0.8,
        label="Death Valley",
        precip_scale="in",
    )

    # Generate the visualization.
    weather_plotter.plot_visual(shade_between=False, y_limit=(-0.01, 2.8))
