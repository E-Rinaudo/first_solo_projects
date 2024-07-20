import pandas as pd
from datetime import datetime

import plotly.graph_objects as go


class WildfirePlotter:
    """A class to visualize wildfire activity in North America."""

    def __init__(self, path: str):
        """Initialize the class attribute, read the csv file and plot the data."""
        self.path = path
        self._read_file()
        self._visualize_plot()

    def _read_file(self):
        """Read the csv file."""
        self.fires_data = pd.read_csv(self.path)

    def _format_date(self):
        """Format the data acquisition date to neatly display it."""
        df_dates = list(self.fires_data["acq_date"])
        self.acq_dates = []

        for df_date in df_dates:
            date_str = str(df_date)
            datetime_date = datetime.strptime(date_str, "%Y-%m-%d")
            formatted_date = datetime_date.strftime("%B %d, %Y")
            self.acq_dates.append(formatted_date)

    def _format_time(self):
        """Format the data acquisition time to neatly display it."""
        df_times = list(self.fires_data["acq_time"])
        self.acq_times = []

        for df_time in df_times:
            time_str = str(df_time).zfill(4)
            datetime_time = datetime.strptime(time_str, "%H%M")
            formatted_time = datetime_time.strftime("%H:%M (24 HR Format)")
            self.acq_times.append(formatted_time)

    def _format_label_text(self):
        """Combine the date, time and brightness into a text for the plot label."""
        self._format_date()
        self._format_time()

        self.fires_data["text"] = [
            f"Acquisition Date: {date} -- {time} -- Brightness: {brightness}"
            for date, time, brightness in zip(
                self.acq_dates,
                self.acq_times,
                self.fires_data["brightness"].astype(str),
            )
        ]

    def _visualize_plot(self):
        """Visualize wildfire activity."""
        self._format_label_text()
        # Lower the brightness value to use it as a size in the plot.
        bright_size = [bright // 18 for bright in self.fires_data["brightness"]]

        # Make the plot.
        fig = go.Figure(
            data=go.Scattergeo(
                lat=self.fires_data["latitude"],
                lon=self.fires_data["longitude"],
                text=self.fires_data["text"],
                mode="markers",
                marker=dict(
                    size=bright_size,
                    color=self.fires_data["brightness"],
                    colorscale="Hot",
                    colorbar_title="Wildfire Brightness",
                ),
            )
        )

        self._update_plot(fig)
        fig.show()

    def _update_plot(self, fig: go.Figure):
        """Customize the plot."""
        title = "USA Contiguous and Hawaii Wildfire Activity "
        title += f"({self.acq_dates[0]} to {self.acq_dates[-1]})"

        fig.update_layout(
            geo=dict(
                scope="north america",
                resolution=50,
                projection=dict(type="conic conformal", rotation_lon=-100),
                lonaxis=dict(
                    showgrid=True, gridwidth=0.5, range=[-180.0, -20.0], dtick=5
                ),
                lataxis=dict(showgrid=True, gridwidth=0.5, range=[10.0, 50.0], dtick=5),
            ),
            title=title,
        )


if __name__ == "__main__":
    # Give a path and make the instance to visualize the data.
    path = "fires_file/MODIS_C6_1_USA_contiguous_and_Hawaii_3d.csv"
    wildfire = WildfirePlotter(path)
