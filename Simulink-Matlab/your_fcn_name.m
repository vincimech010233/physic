function z = your_fcn_name(x,y)
  % Check if vectors have the same dimension
  if length(x) ~= length(y)
    error('Vectors must have the same dimension');
  end
  % Calculate inner product using element-wise multiplication and summation
  z = sum(x .* y);
end


% % Asigna valores a x y y antes de llamar a la función
% x = [1, 2, 3]; % Ejemplo de vector x
% y = [4, 5, 6]; % Ejemplo de vector y con la misma dimensión que x
% 
% % Llama a la función con los vectores x y y
% resultado = your_fcn_name(x,y);
% 
% % Muestra el resultado
% disp(['El producto interno de los vectores es: ', num2str(resultado)]);
