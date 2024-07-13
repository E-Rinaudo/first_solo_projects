from pathlib import Path

from weather_data_plotter import WeatherDataPlotter as WDP


# Analize the high and low temperatures (F°) in Los Angeles (CA, US)
#   for the year 2000.


if __name__ == "__main__":
    # Create a plotter instance.
    weather_plotter = WDP(
        title="Daily High and Low Temperatures, 2000", title_color="k"
    )

    # Add data for Los Angeles to the plotter dataset.
    path = Path("weather_data/los_angeles_weather_2000_F_in.csv")

    weather_plotter.weather_dataset(
        path=path,
        high=True,
        low=True,
        label="Los Angeles",
        temp_scale="F°",
    )

    # Generate the visualization.
    weather_plotter.plot_visual()
