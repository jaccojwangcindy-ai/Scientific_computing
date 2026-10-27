# Function definition
def f(x):
    return x**3 - 4*x + 1

# Initial interval
a = 0
b = 1

# Perform 10 iterations of bisection
for i in range(10):
    c = (a + b) / 2

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    print(f"Iteration {i+1}: root ≈ {c:.6f}")

print("\nApproximate root:", c)