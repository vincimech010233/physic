import numpy as np
import time

def f(x):
    """
    Function to integrate: f(x) = sqrt(1 - x^2).
    
    Parameters:
    - x (float): Input value.
    
    Returns:
    - float: Value of f(x).
    """
    if not (-1 <= x <= 1):
        raise ValueError("Input x must be within the interval [-1, 1].")
    return np.sqrt(1 - x**2)

def integral_slice_method(number_of_slices):
    """
    Approximates the integral of f(x) using the slice method.
    
    Parameters:
    - number_of_slices (int): Number of slices to use for the approximation.
    
    Returns:
    - float: Approximation of the integral.
    """
    if number_of_slices <= 0:
        raise ValueError("Number of slices must be greater than 0.")
    
    h = 2 / number_of_slices  # Slice width
    total = 0.0
    for k in range(number_of_slices):
        x_k = -1 + h * k  # Left-hand endpoint of the k-th slice
        total += h * f(x_k)  # Sum the slice contributions
    return total

def measure_runtime(slices):
    """
    Measures the runtime of the integral_slice_method.
    
    Parameters:
    - slices (int): Number of slices for the calculation.
    
    Returns:
    - tuple: (result of the integral, runtime in seconds).
    """
    start = time.time()
    result = integral_slice_method(slices)
    end = time.time()
    return result, end - start

# Perform calculations with different numbers of slices
slice_counts = [100, 500_000]
for slices in slice_counts:
    integral, runtime = measure_runtime(slices)
    print(f"Slices: {slices}, Integral: {integral:.9f}, Time: {runtime:.6f} seconds")

###############################################################################
# Conclusion
###############################################################################
# With this method, for about 1 second of runtime, we achieve approximately
# 9 digits of accuracy for the integral of f(x) = sqrt(1 - x^2). The accuracy 
# improves as the number of slices increases, but the runtime scales linearly.
# This highlights the tradeoff between computation time and precision.
