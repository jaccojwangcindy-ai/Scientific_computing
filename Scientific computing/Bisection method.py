# Function and derivative
def f(x):
    return x**2 - 3

def df(x):
    return 2*x

# Initial guess
x = 2.0

# Newton iterations
for i in range(5):
    x = x - f(x) / df(x)
    print(f"Iteration {i+1}: x = {x:.6f}")

print("\nApproximate root:", x)