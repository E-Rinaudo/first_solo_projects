from pathlib import Path

from weather_data_plotter import WeatherDataPlotter as WDP


# Analize the high and low temperatures (F°) in Sitka (AK, US)
#   and Death Valley (CA, US) for the year 2021.


if __name__ == "__main__":
    # Create a plotter instance.
    weather_plotter = WDP(
        title="Daily High and Low Temperatures, 2021", title_color="k"
    )

    # Add data for Death Valley to the plotter dataset.
    dv_path = Path("weather_data/death_valley_weather_2021_F_in.csv")

    weather_plotter.weather_dataset(
        path=dv_path,
        high=True,
        low=True,
        alpha=0.8,
        label="Death Valley",
        temp_scale="F°",
    )

    # Add data for Sitka to the plotter dataset.
    sitka_path = Path("weather_data/sitka_weather_2021_F_in.csv")

    weather_plotter.weather_dataset(
        path=sitka_path,
        high=True,
        low=True,
        alpha=0.5,
        label="Sitka",
    )

    # Generate the visualization.
    weather_plotter.plot_visual(y_limit=(10, 140))
