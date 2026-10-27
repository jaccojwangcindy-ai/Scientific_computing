import numpy as np
import matplotlib.pyplot as plt

# Number of random points
N = 5000

# Generate random points in the unit square
x = np.random.rand(N)
y = np.random.rand(N)

# Check if points are inside the quarter circle
inside = x**2 + y**2 <= 1

# Estimate pi
pi_estimate = 4 * np.sum(inside) / N

print(f"Estimated π = {pi_estimate:.6f}")

# Plot
plt.figure(figsize=(6, 6))

# Points inside the circle
plt.scatter(
    x[inside], y[inside],
    s=5, color='blue',
    label='Inside Quarter Circle'
)

# Points outside the circle
plt.scatter(
    x[~inside], y[~inside],
    s=5, color='red',
    label='Outside Quarter Circle'
)

# Draw quarter circle
theta = np.linspace(0, np.pi/2, 200)
plt.plot(np.cos(theta), np.sin(theta),
         color='black', linewidth=2)

plt.title(f"Monte Carlo Estimate of π ≈ {pi_estimate:.4f}")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.grid(True)
plt.legend()

plt.show()