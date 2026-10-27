import numpy as np

# Matrix A
A = np.array([
    [4, 0],
    [0, 4]
])

# Vector v
v = np.array([2, 3])

# Compute Av
Av = A @ v

print("Av =", Av)
print("4v =", 4 * v)

# Check if Av = 4v
if np.array_equal(Av, 4 * v):
    print("v is an eigenvector of A with eigenvalue 4")