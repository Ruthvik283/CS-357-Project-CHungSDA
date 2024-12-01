import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_drone_translation(drones, waypoints, assignments):
    # Create a figure and an axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the initial drone positions (blue spheres)
    for i, (drone_x, drone_y, drone_z) in enumerate(drones):
        ax.scatter(drone_x, drone_y, drone_z, color='blue', s=100, label=f'Drone {i} Start' if i == 0 else "")
        ax.text(drone_x, drone_y, drone_z, f'Drone {i}', color='blue', fontsize=12)

    # Plot the waypoints (red spheres)
    for i, (wp_x, wp_y, wp_z) in enumerate(waypoints):
        ax.scatter(wp_x, wp_y, wp_z, color='red', s=100, label=f'Waypoint {i}' if i == 0 else "")
        ax.text(wp_x, wp_y, wp_z, f'Waypoint {i}', color='red', fontsize=12)

    # Draw arrows for each drone's movement to the corresponding waypoint
    for i, assignment in enumerate(assignments):
        drone_index, waypoint_index = assignment
        drone_x, drone_y, drone_z = drones[drone_index]
        wp_x, wp_y, wp_z = waypoints[waypoint_index]

        # Draw a thicker, green arrow with a nice color
        ax.quiver(drone_x, drone_y, drone_z, wp_x - drone_x, wp_y - drone_y, wp_z - drone_z, 
                  color='green', arrow_length_ratio=0.1, linewidth=2)

    # Set labels and title with improved font sizes
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Y', fontsize=14)
    ax.set_zlabel('Z', fontsize=14)
    ax.set_title('Drone Translations', fontsize=16)

    # Enhance the grid and background for clarity
    ax.grid(True, linestyle='--', alpha=0.7)  # Dotted grid for better visibility
    ax.set_facecolor('#f7f7f7')  # Light background for better contrast

    # Set the axes limits for a better view
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_zlim([0, 10])

    # Set a better view angle for 3D
    ax.view_init(elev=30, azim=45)  # Change elevation and azimuth for a better perspective

    # Show the plot with legend
    ax.legend(loc='best', fontsize=12)
    plt.show()

def parse_input():


    # Drone positions
    drones = [
        (3, 2, 1),  # Drone 0
        (2, 3, 4),  # Drone 1
        (1, 4, 7),  # Drone 2
        (5, 1, 10), # Drone 3
        (6, 7, 8),  # Drone 4
        (8, 5, 6),  # Drone 5
        (9, 2, 3)   # Drone 6
    ]

    # Waypoint positions
    waypoints = [
        (6, 4, 6),  # Waypoint 0
        (8, 5, 4),  # Waypoint 1
        (7, 6, 5),  # Waypoint 2
        (10, 9, 3), # Waypoint 3
        (5, 3, 7),  # Waypoint 4
        (4, 2, 8),  # Waypoint 5
        (3, 1, 9)   # Waypoint 6
    ]

    # Assignments (Drone to Waypoint mapping)
    assignments = [
        (0, 3),  # Drone 0 -> Waypoint 3
        (1, 4),  # Drone 1 -> Waypoint 4
        (2, 5),  # Drone 2 -> Waypoint 5
        (3, 6),  # Drone 3 -> Waypoint 6
        (4, 0),  # Drone 4 -> Waypoint 0
        (5, 2),  # Drone 5 -> Waypoint 2
        (6, 1)   # Drone 6 -> Waypoint 1
    ]

    return drones, waypoints, assignments

# Main code
drones, waypoints, assignments = parse_input()

# Call the function to plot
plot_drone_translation(drones, waypoints, assignments)
