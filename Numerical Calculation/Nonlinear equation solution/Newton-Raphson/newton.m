function [x_r,err,iter, Solutions] = newton(func,x0,xtol,maxiter)
% Find a fixed point of the function.
% Newton-Raphson method to find a zero of the function f(x)..
% Parameters:
% - func : function
%           Function to evaluate.
% - x0 : float, optional.
%           Fixed point of function. defaults to 1.
% - xtol : float, optional
%           Convergence tolerance, defaults to 1e-08.
% - maxiter : int, optional
%           Maximum number of iterations, defaults to 500.
% Outputs:
% - iter : the number of iterations carried out.
% - x : the approximation to the function.
% - err : the error in the approximation
% - Solutions : the list of solutions.
% Example:
% >> [iter,x,err,Solutions] = newton('1 + 1 / x',1,1e-8,500);

% Check inputs and initialize
if nargin < 4
  maxiter = 500;
  if nargin < 3
    xtol = 1e-8;
    if nargin < 2
      x0 = 1;
      if nargin < 1
        error('MATLAB:fixpt', 'No Enough Inputs.');
      end  
    end
  end
end

% Construct inline function
syms x;
func = sym(func);
g = inline(x - func/diff(func));

% Initialize solutions
Solutions(1) = x0;

% Find the fixed-point of the function and do interation
for iter = 2 : maxiter
    Solutions(iter) = feval(g, Solutions(iter - 1));
    err = abs(Solutions(iter) - Solutions(iter - 1));
    relerr = err / (abs(Solutions(iter)) + eps);
    x_r = Solutions(iter);
    if (err < xtol) | (relerr < xtol)
        break;
    end
end

% Warning reaching the maximum iteration times.
if iter == maxiter
    disp('Maximum number of iterations exceeded.')
end

% Plot the graph
Solutions=Solutions';
plot(Solutions);