function [x_r, err, iter] = bisect(func, x_l, x_u, xtol)
% Find root of a function within an interval.
% Basic bisection routine to find a zero of the function f(x) between the x_l and x_u.
% Parameters:
% - func : function
%           Function to evaluate. Note that f(x_l) and f(x_u) can not have the same signs.
% - x_l, x_u : float
%           Ends of the bracketing interval [x{l, x_u].
% - xtol : float, optional
%           Convergence tolerance, defaults to 1e-08.
% Outputs:
% - x_r : Zero of f between x_l and x_u.
% - err : the error in the approximation
% - iter : the times of iteration.
% Example:
% >> [x_r, err, iter]=bisect('- (25*x^4)/216 + 5*x^2 - 30',0.1,5.9,1e-8);

% Check inputs and initialize
if nargin < 4
  xtol = 1e-8;
  if nargin < 3
    error('MATLAB:bisect','No Enough Inputs.');
  end
end

% Construct inline function
f = inline(func);

% Check if f(x_l) and f(x_u) have the same signs.
fx_l = feval(f, x_l);
fx_u = feval(f, x_u);
if fx_l * fx_u > 0
    error('MATLAB:bisect','f(x_l) and f(x_u) CANNOT have the same signs..');
end

% Maximum number of iterations
maxiter = 1 + round((log(x_u - x_l) - log(xtol)) / log(2));

% Find the zero of f(x)
for iter = 1:maxiter
    x_r = (x_l + x_u)/2;
    fx_r = feval(f, x_r);
    
    % Plot every lines
    plot([x_l, x_u], [30 - iter, 30 - iter], 'LineWidth', 2);
    hold on;
    
    if fx_r == 0
        x_l = x_r;
        x_u = x_r;  
    elseif fx_u * fx_r > 0
        x_u = x_r;
        fx_u = fx_r;
    else
        x_l = x_r;
        fx_l = fx_r;
    end
    if x_u - x_l < xtol
        break
    end
end

% Warning reaching the maximum iteration times.
if iter == maxiter
    disp('Maximum number of iterations exceeded.')
end

x_r = (x_l + x_u) / 2;
err = abs(x_u - x_l);