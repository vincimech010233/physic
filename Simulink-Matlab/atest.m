% Ejemplo de uso
T_F = 10; % Temperatura del aire en grados Fahrenheit
V_mph = 15; % Velocidad del viento en millas por hora

WindChill_F = getWindChill_F(T_F, V_mph);
disp(['El índice de temperatura de sensación térmica del viento es: ', num2str(WindChill_F), ' grados Fahrenheit.']);
