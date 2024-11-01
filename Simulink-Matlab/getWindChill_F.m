function WindChill_F = getWindChill_F(T_F, V_mph)
    % Verificar si algún valor de la velocidad del viento está fuera del rango permitido (0 a 60 mph)
    if any(V_mph(:) < 0) || any(V_mph(:) > 60)
        error('La velocidad del viento debe estar entre 0 y 60 mph.');
    end
    
    % Verificar si la temperatura del aire está dentro del rango permitido (-45 a +45 grados Fahrenheit)
    if any(T_F(:) < -45) || any(T_F(:) > 45)
        error('La temperatura del aire debe estar entre -45 y +45 grados Fahrenheit.');
    end
    
    % Calcular el índice de temperatura de sensación térmica del viento
    WindChill_F = round(35.74 + 0.6215 * T_F - 35.75 * V_mph.^0.16 + 0.4275 * T_F .* V_mph.^0.16);
end

% % Ejemplo de uso
% T_F = 10; % Temperatura del aire en grados Fahrenheit
% V_mph = 15; % Velocidad del viento en millas por hora
% 
% WindChill_F = getWindChill_F(T_F, V_mph);
% disp(['El índice de temperatura de sensación térmica del viento es: ', num2str(WindChill_F), ' grados Fahrenheit.']);
