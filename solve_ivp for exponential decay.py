import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Differential equation: dy/dt = -0.5y
def decay(t, y):
    return -0.5 * y

# Time interval
t_span = (0, 10)

# Initial value
y0 = [100]

# Times where solution is desired
t_eval = np.linspace(0, 10, 100)

# Solve the IVP
solution = solve_ivp(decay, t_span, y0, t_eval=t_eval)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(solution.t, solution.y[0],
         color="blue",
         linewidth=2,
         label="Numerical Solution")

plt.title("Exponential Decay: dy/dt = -0.5y")
plt.xlabel("Time")
plt.ylabel("Amount Remaining")
plt.grid(True)
plt.legend()

plt.show()

# Display some values
for i in range(0, len(solution.t), 20):
    print(f"t = {solution.t[i]:.1f}, y = {solution.y[0][i]:.2f}")