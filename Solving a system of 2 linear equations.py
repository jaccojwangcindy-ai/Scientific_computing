import numpy as np

# Coefficient matrix
A = np.array([
    [1, 1, 1],
    [2, 3, 1],
    [1, 2, 3]
])

# Constant vector
b = np.array([6, 14, 14])

# Solve Ax = b
solution = np.linalg.solve(A, b)

print("Solution:")
print(f"x = {solution[0]:.0f}")
print(f"y = {solution[1]:.0f}")
print(f"z = {solution[2]:.0f}")