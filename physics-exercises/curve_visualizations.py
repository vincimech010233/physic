import numpy as np
import matplotlib.pyplot as plt

# Part a: Deltoid Curve
def deltoid_curve(theta_limit):
    """
    Generates the x and y coordinates for a deltoid curve.

    Parameters:
    - theta_limit (int): Number of points to calculate the curve.

    Returns:
    - tuple: Arrays of x and y coordinates.
    """
    if theta_limit <= 0:
        raise ValueError("Theta limit must be greater than 0.")
    
    theta = np.linspace(0, 2 * np.pi, theta_limit)
    x = 2 * np.cos(theta) + np.cos(2 * theta)
    y = 2 * np.sin(theta) - np.sin(2 * theta)
    return x, y

# Plot deltoid curve
x, y = deltoid_curve(1000)
plt.plot(x, y)
plt.title("Deltoid Curve")
plt.show()

# Part b: Galilean Spiral
def polar_to_cartesian(r, theta_array):
    """
    Converts polar coordinates to Cartesian coordinates.

    Parameters:
    - r (array): Array of radial distances.
    - theta_array (array): Array of angles in radians.

    Returns:
    - tuple: Arrays of x and y Cartesian coordinates.
    """
    if len(r) != len(theta_array):
        raise ValueError("Arrays for r and theta must have the same length.")
    
    x = r * np.cos(theta_array)
    y = r * np.sin(theta_array)
    return x, y

def galilean_spiral(theta_limit, theta_steps):
    """
    Generates the radial and angular coordinates for a Galilean spiral.

    Parameters:
    - theta_limit (float): Maximum angle for the spiral in radians.
    - theta_steps (int): Number of points in the spiral.

    Returns:
    - tuple: Arrays of radial distances and angles.
    """
    if theta_limit <= 0 or theta_steps <= 0:
        raise ValueError("Theta limit and steps must be greater than 0.")
    
    theta = np.linspace(0, theta_limit, theta_steps)
    r = theta**2
    return r, theta

# Plot Galilean spiral
r, theta = galilean_spiral(10 * np.pi, 100)
x, y = polar_to_cartesian(r, theta)
plt.plot(x, y)
plt.title("Galilean Spiral")
plt.show()

# Part c: Fey's Function
def feys_function(theta_limit, theta_steps):
    """
    Generates the radial and angular coordinates for Fey's function.

    Parameters:
    - theta_limit (float): Maximum angle for the plot in radians.
    - theta_steps (int): Number of points in the plot.

    Returns:
    - tuple: Arrays of radial distances and angles.
    """
    if theta_limit <= 0 or theta_steps <= 0:
        raise ValueError("Theta limit and steps must be greater than 0.")
    
    theta = np.linspace(0, theta_limit, theta_steps)
    r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + (np.sin(theta / 12))**5
    return r, theta

# Plot Fey's function
r, theta = feys_function(24 * np.pi, 10000)
x, y = polar_to_cartesian(r, theta)
plt.plot(x, y)
plt.title("Fey's Function")
plt.show()
