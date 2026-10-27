import numpy as np
import matplotlib.pyplot as plt

# Time (hours)
t = np.array([0, 1, 2, 3, 4])

# Flow rate (L/h)
Q = np.array([10, 12, 15, 18, 20])

# Numerical integration using trapezoidal rule
volume = np.trapezoid(Q, t)

print(f"Estimated volume added = {volume:.2f} liters")

# Plot
plt.figure(figsize=(8, 5))

# Flow-rate curve
plt.plot(t, Q, 'bo-', linewidth=2, label='Flow Rate')

# Shade area under curve
plt.fill_between(t, Q, alpha=0.3, color='skyblue',
                 label='Integral (Volume)')

plt.title("Flow Rate vs Time")
plt.xlabel("Time (hours)")
plt.ylabel("Flow Rate (L/h)")
plt.grid(True)
plt.legend()

# Show estimated volume
plt.text(1.5, 16,
         f"Volume ≈ {volume:.1f} L",
         bbox=dict(facecolor='yellow'))

plt.show()