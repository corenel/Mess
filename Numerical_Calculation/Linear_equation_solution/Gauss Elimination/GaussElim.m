function x = GaussElim(A,b) 
	% Solve linear equations system by Gaussian Elimination.
	% Parameter:
	% - A: Coefficient Matrix
	% - b: Adjoint Matrix
	% Output:
	% - x: The solution of Ax=b

    % Check if A and b are compatible
    n = max(size(A)); 
    l = max(size(b));
    if n ~= l
        error('MATLAB:Gauss', 'Invalid argument: incompatible sizes between A and b.'); 
    end
    
    % Initialize x
    % x = single(zeros(n, 1));
    x = zeros(n, 1);
    
    % Eliminate the elements
    for k = 1 : n -1 
        if A(k,k) == 0 
           error('MATLAB:Gauss', 'An Exception occured that algorithm failed. Element should not be zero.'); 
        end 
        for i = k + 1 : n 
            factor = A(i,k) / A(k,k); 
            for j = k : n 
                A(i,j) = A(i,j) - factor * A(k,j); 
            end 
            b(i,1) = b(i,1) - factor * b(k); 
        end 
        %A    % Print A in every step
        %b    % Print b in every step
    end 
    
    % Calculate each variable
    
    x(n,1) = b(n,1) / A(n,n); 
    for i = n-1 : -1 : 1
        sum = b(i,1);
        for j = i+1 : n
            sum = sum - A(i,j) * x(j);
        end
        x(i) = sum / A(i,i);
    end