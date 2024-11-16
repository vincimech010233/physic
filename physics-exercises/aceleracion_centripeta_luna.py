import math

# Datos
T_dias = 27.32  
R_km = 384000   

# Conversión de unidades
T_segundos = T_dias * 24 * 60 * 60  
R_metros = R_km * 1000              

a_n = (4 * math.pi**2 * R_metros) / T_segundos**2

print(f"La aceleración centrípeta de la Luna es: {a_n:.3e} m/s²")
