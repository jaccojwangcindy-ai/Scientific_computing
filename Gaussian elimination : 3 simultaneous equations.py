import numpy as np

# Successive estimates
estimates = np.array([5.0, 4.5, 4.2, 4.05, 4.01])

# True value
true_value = 4.0

# Absolute errors
errors = np.abs(estimates - true_value)

print("Estimates:", estimates)
print("Errors:", errors)

print("\nFinal estimate:", estimates[-1])
print("Value being approached:", true_value)