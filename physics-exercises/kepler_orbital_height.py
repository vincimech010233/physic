import numpy as np

def kepler_height(period):
    G = 6.67e-11  
    M = 5.97e24  
    R = 6371e3    

    T = float(period) 
    orbital_radius = (G * M * T**2 / (4 * np.pi**2))**(1/3)
    height = orbital_radius - R
    return height

period = float(input("Write the period of the satellite's orbit in seconds: "))
print(kepler_height(period))
