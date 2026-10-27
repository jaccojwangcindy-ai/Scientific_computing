import numpy as np
import matplotlib.pyplot as plt

# Time (seconds) and distance (meters)
time = np.array([0, 3])
distance = np.array([50, 65])

# Average rate of change
speed = (distance[1] - distance[0]) / (time[1] - time[0])

print(f"Average speed = {speed:.2f} m/s")

# Plot
plt.figure(figsize=(6,4))
plt.plot(time, distance, 'bo-', linewidth=2)

plt.title("Distance vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.grid(True)

# Annotate the points
plt.annotate("(0, 50)", (0, 50))
plt.annotate("(3, 65)", (3, 65))

# Display slope on graph
plt.text(1, 57, f"Slope = {speed:.2f} m/s",
         bbox=dict(facecolor='yellow', alpha=0.5))

plt.show()