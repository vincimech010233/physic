from sympy import symbols, Eq, solve, sqrt

# Datos iniciales
m_bala = 0.02  # masa de la bala en kg
v_bala = 600   # velocidad de la bala en m/s
m_bloque = 1.0  # masa del bloque en kg
g = 9.8         # aceleración debida a la gravedad en m/s^2
L = 1.0         # longitud del hilo en metros


m_total = m_bala + m_bloque
v0 = (m_bala * v_bala) / m_total
print(f"Velocidad después del choque (v0): {v0:.2f} m/s")


v = symbols('v', real=True, positive=True)  # Definimos v como positivo
energy_eq = Eq((1/2) * m_total * v0**2, (1/2) * m_total * v**2 + m_total * g * (2 * L))
v_sol = solve(energy_eq, v)[0]  
v_sol_m_s = v_sol.evalf()
print(f"Velocidad en el punto más alto (v): {v_sol_m_s:.2f} m/s")


T = symbols('T')
tension_eq = Eq(T + m_total * g, m_total * v_sol_m_s**2 / L)
T_sol = solve(tension_eq, T)[0]
T_sol_N = T_sol.evalf()
print(f"Tensión del hilo en el punto más alto (T): {T_sol_N:.2f} N")
