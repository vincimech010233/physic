import numpy as np

def f(x):
    """Function to evaluate."""
    return x * (x - 1)

def derivative(value, delta):
    """
    Approximates the derivative of f(x) using the finite difference method.
    
    Parameters:
    - value (float): The point at which to evaluate the derivative.
    - delta (float): The step size for the finite difference.

    Returns:
    - float: Approximation of the derivative at the given point.
    """
    return (f(value + delta) - f(value)) / delta

# Test different delta values
values = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
results = [derivative(1, delta) for delta in values]

# Print results
for delta, result in zip(values, results):
    print(f"Delta: {delta:.0e}, Derivative: {result:.10f}")

###############################################################################
# Conclusion
###############################################################################
# Initially, reducing the delta improves the approximation of the derivative,
# as it better captures the instantaneous rate of change. However, when delta 
# becomes very small, numerical precision issues arise due to floating-point 
# arithmetic. Specifically, subtracting nearly equal floating-point numbers 
# (as in f(x + delta) - f(x)) leads to significant round-off errors, which 
# degrade the accuracy of the calculation. This phenomenon is a limitation 
# of finite precision in computer arithmetic.
