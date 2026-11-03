import numpy as np

# Time (hours) and distance (km)
times = np.array([2, 4])
distances = np.array([60, 80])

# Estimate distance at 3:00 PM
distance_at_3 = np.interp(3, times, distances)

print(f"Estimated distance at 3:00 PM: {distance_at_3:.1f} km")