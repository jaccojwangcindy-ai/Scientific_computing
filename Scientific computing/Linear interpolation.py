import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([55, 60, 65, 72, 78])

# Least-squares linear fit
b, a = np.polyfit(x, y, 1)

print(f"Intercept (a) = {a:.2f}")
print(f"Slope (b) = {b:.2f}")

# Predicted values
y_pred = a + b * x

print("\nPredicted scores:")
print(y_pred)