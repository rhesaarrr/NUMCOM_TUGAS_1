import math

def f(x):
    return (x**4 + math.exp(-2*x)) / math.log(x + 3) + math.tanh(x) - (5 - x**3) * (1 / math.cosh(x))**2

def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("No root in the given interval.")
        return None
    
    c_old = a
    epsilon_a = float('inf')
    
    while epsilon_a >= tol:
        c = (a + b) / 2
        fc = f(c)
        epsilon_a = abs(c - c_old) / abs(c) * 100 if c != 0 else 0
        
        if epsilon_a < tol:
            print(f"Root: {c:.6f}")
            print(f"Approximate error: {epsilon_a:.6f}%")
            return c
        
        if fc * f(a) < 0:
            b = c
        else:
            a = c
        
        c_old = c
    
    return c

a = 1  #xl
b = 2  #xu
tolerance = 0.05 
root = bisection_method(a, b, tolerance)
