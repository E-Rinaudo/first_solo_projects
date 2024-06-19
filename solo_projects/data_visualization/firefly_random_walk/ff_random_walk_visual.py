import plotly.graph_objects as go
import numpy as np

from ff_random_walk import RandomWalk


FONT_SCATTER_POINTS = 5
FONT_MAIN_POINTS = 30
FONT_TITLE = 25
FONT_AXES_LABELS = 10


class Firefly_Walk:
    """A Class to generate the random walk of a Firefly at night."""

    def __init__(self):
        """Initialize the Random Walk attributes and generate it."""
        rw = RandomWalk()
        rw.make_walk()

        self._make_plot(rw)
    
    def _make_plot(self, rw):
        """Create and display the scatter plot for the random walk."""
        fig = go.Figure()

        self._random_walk_trace(rw, fig)
        self._starting_point(fig)
        self._ending_point(rw, fig)
        self._customize_plot(fig)

        fig.show()

    def _random_walk_trace(self, rw, fig):
        """Add the random walk trace."""
        fig.add_trace(
            go.Scattergl(
                x=rw.x_values, 
                y=rw.y_values,  
                name='Random Walk',
                mode='markers', 
                marker=dict(
                    color=np.arange(rw.num_points), 
                    symbol='star', 
                    size=FONT_SCATTER_POINTS, 
                    colorscale='Oranges', 
                    showscale=True
                )
            )
        )

    def _starting_point(self, fig):
        """Add the starting point."""
        fig.add_trace(
            go.Scatter(
                x=[0],
                y=[0],
                name='Start Point',
                mode='markers', 
                marker=dict(
                    color='green', 
                    symbol='circle', 
                    size=FONT_MAIN_POINTS, 
                )
            )
        )

    def _ending_point(self, rw, fig):
        """Add the ending point."""
        fig.add_trace(
            go.Scatter(
                x=[rw.x_values[-1]],
                y=[rw.y_values[-1]],
                name='End Point',
                mode='markers', 
                marker=dict(
                    color='blue', 
                    symbol='circle', 
                    size=FONT_MAIN_POINTS, 
                )
            )
        )

    def _customize_plot(self, fig):
        """Customize the plot."""
        fig.update_layout(
            plot_bgcolor='black',
            title=dict(
                text='Firefly Dance: A Random Walk on a Summer Night', 
                font=dict(
                    family='Arial', 
                    size=FONT_TITLE, 
                    color='darkred'
                )
            ), 
            xaxis_title='X Position', 
            yaxis_title='Y Position',
            font=dict(size=FONT_AXES_LABELS),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            )
        )


if __name__ == '__main__':
    # Make the instance and generate the plot.
    fw = Firefly_Walk()