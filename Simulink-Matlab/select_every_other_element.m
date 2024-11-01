function y = select_every_other_element(x)
  % Use slicing with a step of 2 to get every other element
  y = x(1:2:end);
end

% % Example 1
% x = [1 3 2 4 3 5];
% y = select_every_other_element(x);
% disp(y) % Output: [1 2 3]
% 
% % Example 2
% x = [5 9 3 2 2 0 -1];
% y = select_every_other_element(x);
% disp(y) % Output: [5 3 2 -1]