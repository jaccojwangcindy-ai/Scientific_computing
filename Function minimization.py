import numpy as np
import matplotlib.pyplot as plt

# Define x values
x = np.linspace(0, 8, 400)

# Function
y = (x - 4)**2 + 1

# Minimum point
x_min = 4
y_min = (x_min - 4)**2 + 1

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x)=(x-4)^2+1$', color='blue')

# Mark the minimum point
plt.scatter(x_min, y_min, color='red', s=100,
            label='Minimum Point (4,1)')

plt.annotate('(4, 1)',
             (x_min, y_min),
             xytext=(4.5, 3),
             arrowprops=dict(arrowstyle='->'))

plt.title('Graph of f(x) = (x - 4)^2 + 1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

plt.show()

print(f"Minimum occurs at x = {x_min}")
print(f"Minimum value = {y_min}")