function [x_r,err,iter]=regula(func,x_l,x_u,xtol,ytol,maxiter)
% Find root of a function within an interval.
% False position method to find a zero of the function f(x) between the x_l and x_u.
% Parameters:
% - func : function
%           Function to evaluate. Note that f(x_l) and f(x_u) can not have the same signs.
% - x_l, x_u : float
%           Ends of the bracketing interval [x{l, x_u].
% - xtol : float, optional
%           Convergence tolerance in x axis, defaults to 1e-08.
% - ytol : float, optional
%           Convergence tolerance in y axis, defaults to 1e-08.
% - maxiter : int, optional
%           Maximum number of iterations, defaults to 500.
% Outputs:
% - x_r : Zero of f between x_l and x_u.
% - err : the error in the approximation
% - iter : the times of iteration.
% Example:
% >> [x_r, err, iter]=regula('- (25*x^4)/216 + 5*x^2 - 30',0.1,5.9,1e-8,1e-8,20);

% Check inputs and initialize
if nargin < 6
  maxiter = 500;
  if nargin < 5
    ytol = 1e-8;
    if nargin < 4
      xtol = 1e-8;
      if nargin < 3.0
        error('MATLAB:fixpt', 'No Enough Inputs.');
      end  
    end
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

% Find the zero of f(x)
for iter = 1 : maxiter
    dx = fx_u * (x_u - x_l) / (fx_u - fx_l);
    x_r = x_u - dx;
    length = x_r - x_l;
    fx_r = feval(f, x_r);
    
    % Plot every lines
    plot([x_l, x_u], [maxiter - iter, maxiter - iter], 'LineWidth', 2);
    hold on;

    if fx_r == 0
        break;
    elseif fx_u * fx_r > 0
        x_u = x_r;
        fx_u = fx_r;
    else
        x_l = x_r;
        fx_l = fx_r;
    end
    dx = min(abs(dx), length);
    if abs(dx) < xtol
        break
    end
    if abs(fx_r) < ytol
        break
    end
end

% Warning reaching the maximum iteration times.
if iter == maxiter
    disp('Maximum number of iterations exceeded.')
end

err = abs(x_u - x_l) / 2;
fx_r = feval(f, x_r);