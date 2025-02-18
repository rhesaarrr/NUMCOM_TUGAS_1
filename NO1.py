import math

def f(x):
    return (x**4 + math.exp(-2*x)) / math.log(x + 3) + math.tanh(x) - (5 - x**3) * (1 / math.cosh(x))**2

def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("No root in the given interval.")
        return None
    c_old = a
    iteration = 0
    while True:
        iteration += 1
        c = (a + b) / 2
        fc = f(c)
        epsilon_a = abs(c - c_old) / abs(c) * 100 if c != 0 else 0  # Calculate epsilon_a
        print(f"Iteration {iteration}:")
        print(f"  Interval: [{a}, {b}]")
        print(f"  Midpoint: c = {c}")
        print(f"  f(c) = {fc}")
        print(f"  Approximate error (epsilon_a): {epsilon_a}%")  # Print epsilon_a
        if epsilon_a < tol:
            print(f"  Approximate error is within tolerance. Root found: {c}")
            return c
        if fc == 0:
            print(f"  Exact root found: {c}")
            return c
        elif fc * f(a) < 0:
            b = c
            print(f"  New interval: [{a}, {b}]")
        else:
            a = c
            print(f"  New interval: [{a}, {b}]")
        c_old = c

# Example usage
a = 1  # Initial guess for a
b = 2  # Initial guess for b
tolerance = 0.05  # 0.05% tolerance
root = bisection_method(a, b, tolerance)
print(f"The root is approximately: {root}")