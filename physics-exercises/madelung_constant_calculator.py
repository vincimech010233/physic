import numpy as np

def calculate_madelung_constant(number_of_atoms, distance_between_atoms):
    """
    Calculates the Madelung constant for a given ionic lattice.

    Parameters:
    - number_of_atoms (int): Half the size of the lattice along one dimension.
    - distance_between_atoms (float): Distance between two adjacent ions (in meters).

    Returns:
    - float: The calculated Madelung constant.
    """
    if number_of_atoms <= 0:
        raise ValueError("Number of atoms must be greater than zero.")
    if distance_between_atoms <= 0:
        raise ValueError("Distance between atoms must be greater than zero.")

    e = -1.602176634e-19  # Electron charge in Coulombs
    e_0 = 8.8541878128e-12  # Permittivity of vacuum
    a = distance_between_atoms  # Lattice distance
    L = number_of_atoms  # Lattice size
    
    V_total = 0  # Initialize total electric potential
    
    for i in range(-L, L + 1):
        for j in range(-L, L + 1):
            for k in range(-L, L + 1):
                # Skip the central atom (i=j=k=0)
                if i == 0 and j == 0 and k == 0:
                    continue
                
                # Calculate the distance to the ion
                distance = np.sqrt(i**2 + j**2 + k**2)
                
                # Skip invalid distances (avoid division by zero)
                if distance == 0:
                    continue
                
                # Alternate the sign based on parity of (i + j + k)
                charge_factor = -1 if (i + j + k) % 2 else 1
                V_total += charge_factor * e / (4 * np.pi * e_0 * a * distance)
    
    # Calculate the Madelung constant
    madelung_constant = V_total * 4 * np.pi * e_0 * a / e
    return madelung_constant

# Example usage:
# For rocksalt (NaCl), lattice distance = 5.64e-10 m (5.64 Ångstroms)
print(calculate_madelung_constant(10, 5.64e-10))
