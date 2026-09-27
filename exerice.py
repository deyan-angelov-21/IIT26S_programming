import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Set the limits for x and y axes
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Draw horizontal and vertical lines through the origin
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Set grid lines
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Set labels for axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('2D Cartesian Coordinate Grid')

# Set ticks for both axes
ax.set_xticks(range(-10, 11))
ax.set_yticks(range(-10, 11))

# Show the plot
plt.show()  