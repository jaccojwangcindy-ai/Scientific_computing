import numpy as np

# Coefficient matrix
A = np.array([
    [3, 2],
    [5, -1]
])

# Constant vector
b = np.array([12, 7])

# Solve Ax = b
solution = np.linalg.solve(A, b)

print("Solution:")
print(f"x = {solution[0]:.0f}")
print(f"y = {solution[1]:.0f}")