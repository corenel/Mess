function x = LUmethod(A,b) 
    [L,U] = lu(A);
    y = L \ b;
    x = U \ y;
end