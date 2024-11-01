print("y'' = x - y, y(0) = 1, y'(0) = 0, h = 0.05, where x varies from 0 to 1.")
print("Find the values of y using Euler's numerical method.")
print("\n")

# Initial conditions
x0 = 0.0
y0 = 1.0
z0 = 0.0  # y'(0)

# Final value of x
xn = 1.0

# Step size
h = 0.05

# Number of steps
N = int((xn - x0) / h)

# Initialize variables
x = x0
y = y0
z = z0

# Print initial values
print("Initial Values:")
print(f"x = {x:.4f}, y = {y:.4f}, y' = {z:.4f}")
print("--------------------------")

# Iteration using Euler's Method
for i in range(1, N + 1):
    # Compute derivatives
    dy = z
    dz = x - y  # From y'' = x - y
    
    # Update y and z
    y_new = y + h * dy
    z_new = z + h * dz
    
    # Update x
    x_new = x + h
    
    # Print current step
    print(f"Iteration {i}")
    print(f"x = {x_new:.4f}, y = {y_new:.4f}, y' = {z_new:.4f}")
    print("--------------------------")
    
    # Prepare for next iteration
    x, y, z = x_new, y_new, z_new
