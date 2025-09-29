%%writefile ejercicio1.lean
-- Definición de constantes para el modelo de satélite
def k : Float := 0.05
def s0 : Float := 100.0 -- Desplazamiento inicial

-- Constantes para la perturbación externa (presión solar periódica)
def A_pert : Float := 8.0 -- Amplitud de la perturbación
def omega_pert : Float := 0.3 -- Frecuencia angular de la perturbación

-- Función exponencial aproximada usando la serie de Taylor (primeros 10 términos)
def exp_approx (x : Float) : Float :=
  1.0 + x + x*x/2.0 + x*x*x/6.0 + x*x*x*x/24.0 + x*x*x*x*x/120.0 +
  x*x*x*x*x*x/720.0 + x*x*x*x*x*x*x/5040.0 + x*x*x*x*x*x*x*x/40320.0 +
  x*x*x*x*x*x*x*x*x/362880.0

-- Función Seno (sin(x)) aproximada usando la serie de Taylor (primeros 3 términos)
-- sin(x) ≈ x - x^3/3! + x^5/5!
def sin_approx (x : Float) : Float :=
  x - (x*x*x) / 6.0 + (x*x*x*x*x) / 120.0

-- Función de Perturbación Externa f(t) = A_pert * sin(omega_pert * t)
def f (t : Float) : Float := A_pert * sin_approx (omega_pert * t)

-- Función de Desplazamiento Total: s(t) = s0 * exp(-k * t) + f(t)
def s_perturbed (t : Float) : Float := (s0 * exp_approx (- k * t)) + f t

-- 1. Evaluar a t = 10.0 para ver el desplazamiento con la perturbación
#eval s_perturbed 10.0

-- 2. Evaluar la cota superior (s0 + A_pert), que debe ser el máximo absoluto en t=0
def s_max_cota := s0 + A_pert
#eval s_max_cota

-- 2b. Verificación de la cota: Comprobar que la cota calculada es igual a 108.0
#eval s_max_cota == 108.0

-- 3. Verificación: Comprobar que el desplazamiento en t=10.0 (s_perturbed 10.0)
-- es menor que la cota máxima teórica s_max_cota.
-- Este es un chequeo de la propiedad de acotamiento.
#eval s_perturbed 10.0 <= s_max_cota

