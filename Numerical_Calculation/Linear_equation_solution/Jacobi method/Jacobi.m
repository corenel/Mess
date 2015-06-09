function [x, iter] = Jacobi(A,b,x0,tol,maxiter)
    % Solves the linear system Ax=b using the Jacobi Method.
    % Parameter
    %   - A: an n x n nonsingular matrix
    %   - b: an n x 1 matrix
    %   - x0: an n x 1 matrix; the initial guess
    %	- tol: the tolerance for P
    %	- maxiter: the maximum number of iterations
    % Output
    %   - x is an n x 1 matrix: the jacobi approximation to 
    %   the solution of Ax = b
    %   - iter: the times of iterations.

    n = length(b);

    % Check inputs and initialize
    if nargin < 5
        maxiter = 500;
        if nargin < 4
            tol = 1e-16;
            if nargin < 3
                x0 = zeros([n 1]);
                if nargin < 2
                    error('MATLAB:Jacobi', 'No Enough Inputs.');
                end
            end
        end
    end

    % Solves the linear system
    for iter = 1 : maxiter
        for j = 1 : n
            x(j) = (b(j) - A(j,[1 : j-1, j + 1 : n]) * x0([1 : j - 1, j + 1 : n])) / A(j,j);
        end
        err = abs(norm(x' - x0));
        relerr = err / (norm(x) + eps);
        x0 = x';
        if (err < tol) | (relerr < tol)
            break
        end
    end

    x = x';
end