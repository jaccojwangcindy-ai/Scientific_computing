import numpy as np

# Matrix B
B = np.array([
    [2, 1],
    [4, 3]
])

# Vector y
y = np.array([7, 2])

# Matrix-vector multiplication
result = B @ y

print("Matrix B:")
print(B)

print("\nVector y:")
print(y)

print("\nBy =")
print(result)