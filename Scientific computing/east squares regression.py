import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([220, 260, 300, 360, 410])

# Least-squares fit
b, a = np.polyfit(x, y, 1)

# Predicted values
y_fit = a + b * x

# Print equation
print(f"Best-fit line: y = {a:.2f} + {b:.2f}x")

# Plot data points
plt.scatter(x, y, color='blue', label='Measured Data')

# Plot fitted line
plt.plot(x, y_fit, color='red', label='Least-Squares Line')

# Labels and title
plt.xlabel('Hours of Exercise')
plt.ylabel('Calories Burned')
plt.title('Least Squares Regression')
plt.legend()
plt.grid(True)

# Show graph
plt.show()