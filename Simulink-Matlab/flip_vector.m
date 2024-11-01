function y = flip_vector(x)
    y = x(end:-1:1); % Comienza en el último elemento y procede hacia el primero.
end


% % Definir un vector de prueba
% x = [1, 2, 3, 4, 5];
% 
% % Llamar a la función flip_vector
% y = flip_vector(x);
% 
% % Mostrar el resultado
% disp(y);