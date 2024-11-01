function y = vecsum(x)

  % Inicializar la variable y a 0
  y = 0;

  % Recorrer cada elemento del vector x
  for i = 1:length(x)
    % Sumar el elemento actual al valor de y
    y = y + x(i);
  end

end

