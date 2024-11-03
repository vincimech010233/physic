from sympy import symbols, Eq, solve, sqrt

# Constantes del problema
Q = 190 * 1.60218e-13  # Energía Q en julios (convertida de MeV)
m1_u = 140  # masa del primer fragmento en unidades de masa atómica (u)
m2_u = 49   # masa del segundo fragmento en unidades de masa atómica (u)
u_to_kg = 1.66054e-27  # Conversión de u a kg

m1 = m1_u * u_to_kg
m2 = m2_u * u_to_kg

v1, v2 = symbols('v1 v2')

momentum_eq = Eq(m1 * v1, m2 * v2)
energy_eq = Eq(Q, (1/2) * m1 * v1**2 + (1/2) * m2 * v2**2)

solution = solve((momentum_eq, energy_eq), (v1, v2))
v1_sol, v2_sol = solution[0]

v1_sol_m_s = v1_sol.evalf()  
v2_sol_m_s = v2_sol.evalf()  
print("Resultados de las velocidades de los fragmentos después de la colisión:")
print("----------------------------------------------------------")
print(f"Velocidad del fragmento 1 (v1): {v1_sol_m_s:.2e} m/s")
print(f"Velocidad del fragmento 2 (v2): {v2_sol_m_s:.2e} m/s")
print("----------------------------------------------------------")
