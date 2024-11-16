import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros
A = 2  
B = 3  
omega_0 = 1  
t = np.linspace(0, 10, 500) 

# Cálculo de E y phi
E = np.sqrt(A**2 + B**2)  
phi = np.arctan2(B, A)  

# Definir funciones x(t)
x_t_original = A * np.cos(omega_0 * t) + B * np.sin(omega_0 * t)
x_t_transformed = E * np.cos(omega_0 * t - phi)

# Graficar con grosores diferentes para resaltar las diferencias
plt.figure(figsize=(10, 6))
plt.plot(t, x_t_original, label=r'Original: $A\cos(\omega_0 t) + B\sin(\omega_0 t)$', linestyle='--', color='blue', linewidth=2)
plt.plot(t, x_t_transformed, label=r'Transformada: $E\cos(\omega_0 t - \phi)$', linestyle='-', color='orange', linewidth=1)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (x)')
plt.title('Comparación de Formas del Movimiento Armónico Simple')
plt.legend()
plt.grid()
plt.show()

