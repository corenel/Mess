function [x_u,err,iter]=secant(func,x_l,x_u,xtol,ytol,maxiter)
% Find root of a function.
% Secant method to find a zero of the function f(x).
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
% - x_u : Zero of f between x_l and x_u.
% - err : the error in the approximation
% - iter : the times of iteration.
% Example:
% >> [x_u,err,iter]=secant('-(25*x^4)/216 + 5*x^2 - 30',2,3,1e-8,1e-8,500);

% Construct inline function
f = inline(func);

% Initialize solutions
Solutions(1) = x_u;

for iter = 1 : maxiter
    x_r = x_u - feval(f, x_u) * (x_u - x_l) / (feval(f , x_u) - feval(f , x_l));
    err = abs(x_r - x_u);
    relerr = 2 * err / (abs(x_r) + xtol);
    x_l = x_u;
    x_u = x_r;
    fx = feval(f, x_u);
    Solutions(iter + 1) = x_u;
    if (err < xtol) | (relerr < xtol) | (abs(fx) < ytol)
        break;
    end
end

% Plot the graph
Solutions=Solutions';
plot(Solutions);