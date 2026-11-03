import numpy as np
import matplotlib.pyplot as plt

# Differential equation: dy/dt = 2y
def f(t, y):
    return 2 * y

# Initial condition
t0 = 0
y0 = 1

# Step size
h = 0.1

# Number of steps
n = 10

# Arrays to store results
t = np.zeros(n + 1)
y = np.zeros(n + 1)

t[0] = t0
y[0] = y0

# Euler Method
for i in range(n):
    t[i + 1] = t[i] + h
    y[i + 1] = y[i] + h * f(t[i], y[i])

# Exact solution for comparison
t_exact = np.linspace(0, 1, 100)
y_exact = np.exp(2 * t_exact)

# Print results
for i in range(n + 1):
    print(f"t = {t[i]:.1f}, y ≈ {y[i]:.4f}")

# Plot
plt.figure(figsize=(8, 5))

plt.plot(t_exact, y_exact,
         label='Exact Solution $e^{2t}$',
         color='blue')

plt.plot(t, y,
         'ro--',
         label="Euler's Method")

plt.title("Euler's Method for dy/dt = 2y")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show()