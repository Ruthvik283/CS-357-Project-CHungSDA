import matplotlib.pyplot as plt

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

# Paste given input in the form of arrays here!
def parse_input():
    # Drone positions
    drones = [
        (9, 19, 41),   # Drone 0
        (7, 5, 48),    # Drone 1
        (22, 39, 4),   # Drone 2
        (31, 46, 17),  # Drone 3
        (18, 25, 45),  # Drone 4
        (35, 9, 23),   # Drone 5
        (48, 31, 8),   # Drone 6
        (10, 6, 41),   # Drone 7
        (40, 11, 25),  # Drone 8
        (13, 12, 36)   # Drone 9
    ]

    # Waypoint positions
    waypoints = [
        (6, 6, 32),    # Waypoint 0
        (8, 40, 20),   # Waypoint 1
        (2, 47, 11),   # Waypoint 2
        (18, 13, 1),   # Waypoint 3
        (50, 23, 25),  # Waypoint 4
        (32, 48, 24),  # Waypoint 5
        (13, 7, 38),   # Waypoint 6
        (19, 42, 11),  # Waypoint 7
        (44, 13, 42),  # Waypoint 8
        (25, 6, 15)    # Waypoint 9
    ]

    # Assignments (Drone to Waypoint mapping)
    assignments = [
        (0, 2),  # Drone 0 -> Waypoint 2
        (1, 0),  # Drone 1 -> Waypoint 0
        (2, 7),  # Drone 2 -> Waypoint 7
        (3, 5),  # Drone 3 -> Waypoint 5
        (4, 1),  # Drone 4 -> Waypoint 1
        (5, 9),  # Drone 5 -> Waypoint 9
        (6, 4),  # Drone 6 -> Waypoint 4
        (7, 6),  # Drone 7 -> Waypoint 6
        (8, 8),  # Drone 8 -> Waypoint 8
        (9, 3)   # Drone 9 -> Waypoint 3
    ]

    return drones, waypoints, assignments

# Main code
drones, waypoints, assignments = parse_input()

# Call the function to plot
plot_drone_translation(drones, waypoints, assignments)
