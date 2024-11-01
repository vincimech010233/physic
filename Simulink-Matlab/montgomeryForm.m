function ahat = montgomeryForm(a, R, N)
    % Calcular el inverso multiplicativo de R modulo N
    R_inv = modinv(R, N);
    
    % Obtener dimensiones de la matriz de entrada
    [m, n] = size(a);
    
    % Inicializar matriz de salida
    ahat = zeros(m, n);
    
    % Iterar sobre cada elemento de la matriz de entrada
    for i = 1:m
        for j = 1:n
            % Aplicar la transformación de Montgomery a cada elemento
            ahat(i, j) = montgomeryTransform(a(i, j), R, R_inv, N);
        end
    end
end

% Función para calcular la transformación de Montgomery de un solo elemento
function result = montgomeryTransform(x, R, R_inv, N)
    result = mod(x * R, N);
    if result >= N
        result = result - N;
    end
end

% Función para calcular el inverso multiplicativo utilizando el algoritmo extendido de Euclides
function inv = modinv(a, m)
    m0 = m;
    y = 0;
    x = 1;
 
    if (m == 1)
        inv = 0;
        return;
    end
 
    while (a > 1)
        % q es el cociente de a entre m
        q = floor(a / m);
        t = m;
 
        % m es el residuo de a entre m
        m = mod(a, m);
        a = t;
        t = y;
 
        % Actualizar y y x
        y = x - q * y;
        x = t;
    end
 
    % Asegurar que x sea positivo
    if (x < 0)
        x = x + m0;
    end
 
    inv = x;
end


% a = [10, 20, 30; 40, 50, 60];
% R = 2;
% N = 7;
% ahat = montgomeryForm(a, R, N);
% disp(ahat);