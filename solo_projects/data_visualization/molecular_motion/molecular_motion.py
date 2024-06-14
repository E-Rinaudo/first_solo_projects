import matplotlib.pyplot as plt

from molecular_motion_random_walk import MolecularMotion

# Flag to generate multiple walks.
random_walk = True

while random_walk:
    # Generate the random walk.
    mm = MolecularMotion(50000)
    mm.make_walk()

    # Make the plot.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(14, 5.5), dpi=130)
    num_points = range(mm.num_points)
    ax.scatter(mm.x_values, mm.y_values, c=num_points, cmap=plt.cm.Reds, 
        edgecolors='none', s=1)
    ax.set_aspect('equal')
    ax.set_title("Pollen Grain Walk", fontsize=14)

    # Emphasize the start and end points.
    ax.scatter(0, 0, color='green', label='Start Walk', edgecolors='none', s=80)
    ax.scatter(mm.x_values[-1], mm.y_values[-1], color='blue', label='End Walk',
        edgecolors='none', s=80)

    # Make a legend indicating the start and end points.
    ax.legend(loc='upper left', scatterpoints=1, fancybox=True, shadow=True, 
        fontsize=8)

    # Remove the axes for a clearer visualization.
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    plt.show()

    # Make a new walk.
    new_walk = input("\nMake another walk? (y/n) ")

    if new_walk != 'y':
        random_walk = False