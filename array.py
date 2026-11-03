import numpy as np

# True and approximate values
true_value = 3.14159265
approx_value = 3.14

# Calculate errors
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
percentage_error = relative_error * 100

# Display results
print(f"True value: {true_value}")
print(f"Approximate value: {approx_value}")
print(f"Absolute error: {absolute_error}")
print(f"Relative error: {relative_error}")
print(f"Percentage error: {percentage_error:.4f}%")