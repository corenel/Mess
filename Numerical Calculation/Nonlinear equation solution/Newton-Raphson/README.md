# Newton-Raphson method
## Introduction
Find a fixed point of the function.
Newton-Raphson method to find a zero of the function f(x).
## Parameters:
* func : function
    Function to evaluate.
* x0 : float, optional.
    Fixed point of function. defaults to 1.
* xtol : float, optional
    Convergence tolerance, defaults to 1e-08.
* maxiter : int, optional
    Maximum number of iterations, defaults to 500.

## Outputs:
* iter : the number of iterations carried out.
* x : the approximation to the function.
* err : the error in the approximation
* Solutions : the list of solutions.

# Example:
`>> [iter,x,err,Solutions] = newton('1 + 1 / x',1,1e-8,500);`
