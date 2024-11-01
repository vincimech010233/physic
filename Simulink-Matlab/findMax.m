function y = findMax(x)
  % Check if the input is a vector or matrix
  if ~isvector(x) && ~ismatrix(x)
    error('Input must be a vector or matrix.');
  end

  % Find the maximum value considering potential emptiness
  if isempty(x)
    y = NaN; % Return NaN for empty input
  else
    y = max(x(:)); % Find the maximum element after flattening 
  end
end
