import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the cycloid
R = 10  # Radius of the larger circle
r = 1  # Radius of the smaller circle
l = 1  # Distance from the point to the center of the smaller circle

# Number of points in the cycloid
num_points = 1000

# Generate the cycloid points
t = np.linspace(0, 2 * np.pi, num_points)
x = (R + r) * np.cos(t) - l * np.cos(((R + r) / r) * t)
y = (R + r) * np.sin(t) - l * np.sin(((R + r) / r) * t)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2 * (R + r), 2 * (R + r))
ax.set_ylim(-2 * (R + r), 2 * (R + r))

# Plot the larger circle
large_circle = plt.Circle((0, 0), R, color='b', fill=False)
ax.add_artist(large_circle)

# Plot the path of the cycloid
path, = ax.plot([], [], 'r-', lw=2)

# Initialize the smaller circle
small_circle, = ax.plot([], [], 'g-', lw=2)
point, = ax.plot([], [], 'go')


# Function to initialize the animation
def init():
    path.set_data([], [])
    small_circle.set_data([], [])
    point.set_data([], [])
    return path, small_circle, point


# Function to update the animation
def update(frame):
    # Update the path
    path.set_data(x[:frame], y[:frame])

    # Position of the smaller circle center
    cx = (R + r) * np.cos(t[frame])
    cy = (R + r) * np.sin(t[frame])

    # Position of the point tracing the cycloid
    px = x[frame]
    py = y[frame]

    # Update the smaller circle
    small_circle_x = cx + r * np.cos(t)
    small_circle_y = cy + r * np.sin(t)
    small_circle.set_data(small_circle_x, small_circle_y)

    # Update the point
    point.set_data(px, py)

    return path, small_circle, point


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_points, init_func=init, blit=True, interval=20, repeat=True)

plt.title('Cycloidal Profile Animation')
plt.show()
