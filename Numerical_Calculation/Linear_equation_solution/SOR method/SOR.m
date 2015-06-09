function [x, iter] = SOR(A, b, x0, tol, maxiter, w)
    % Solves the linear system Ax=b using the Successive Over-Relaxation 
    % Method (Gauss-Seidel method when omega = 1 ).
    % Parameter:
	%   - A: an n x n nonsingular matrix: coefficient Matrix
	%   - b: an n x 1 matrix: adjoint Matrix
    %   - x0: an n x 1 matrix; the initial guess
    %	- tol: the tolerance for P
    %	- maxiter: the maximum number of iterations
    %   - w: relaxation scalar
    % Output
    %   - x is an n x 1 matrix: the SOR approximation to 
    %   the solution of Ax = b
    %   - iter: the times of iterations.
    
    n = length(A);

    % Check inputs
    if nargin < 6
        w = 1.5;
        if nargin < 5
            maxiter = 500;
            if nargin < 4
                tol=1e-16;
                if nargin < 3
                    x0 = zeros([n 1]);
                    if nargin < 2
                        error('MATLAB:Jacobi', 'No Enough Inputs.');
                    end
                end
            end
        end
    end
    
    % Initialization
    D = diag(diag(A));
    L = -tril(A, -1);
    U = -triu(A, 1);
    G = (D - L) ^ -1 * U;
    f = (D - L) ^ -1 * b;

    % Solve
    x = x0;
    for iter = 1 : maxiter
        for j = 1 : n
            x(j) = x0(j) + w / A(j,j) * (b(j) - A(j, 1 : j-1) * x(1 : j-1)...
                    - A(j, j : n) * x0(j : n));
        end
        if norm(x - x0) / norm(x) < tol
            break;
        else
            x0 = x;
        end
    end
end