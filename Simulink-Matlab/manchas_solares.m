% Cargar datos de ejemplo de manchas solares directamente en MATLAB
load sunspot.dat;

%% Asignar los datos 
anio = sunspot(:,1);
manchasSolares = sunspot(:,2);


%% Visualizar los datos de manchas solares
figure;
plot(anio, manchasSolares);
title('Actividad Solar (Manchas Solares) a lo Largo del Tiempo');
xlabel('Año');
ylabel('Número de Manchas Solares');
grid on;

%% Analizar los datos 
mediaMovil = movmean(manchasSolares, [11 0]); % Media móvil para suavizar la serie temporal
hold on; % Mantener el gráfico actual para superponer la media móvil
plot(anio, mediaMovil, 'r', 'LineWidth', 2);
legend('Datos Originales', 'Media Móvil (12 meses)');

%% Identificar y marcar el pico más alto de actividad solar
[maxManchas, indiceMax] = max(manchasSolares);
hold on;
plot(anio(indiceMax), maxManchas, 'kp', 'MarkerSize', 10, 'MarkerFaceColor', 'g');
legend('Datos Originales', 'Media Móvil (12 meses)', 'Máximo Pico de Actividad');
