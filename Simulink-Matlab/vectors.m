function y = vectors(x)
  % Inicializar la variable y a 0
  y = 0;

  % Recorrer cada elemento del vector x
  for i = 1:length(x)
    % Sumar el elemento actual al valor de y
    y = y + x(i);
  end
end

% % Define un vector de prueba
% vectorDePrueba = [1, 2, 3, 4, 5];
% 
% % Llama a la función vecsum pasando el vector de prueba como argumento
% resultado = vectors(vectorDePrueba);
% 
% % Muestra el resultado en la ventana de comandos
% disp(['La suma de los elementos del vector es: ', num2str(resultado)]);
