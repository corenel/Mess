# False position method
## Introduction
    function [x_r,err,iter]=regula(func,x_l,x_u,xtol,ytol,maxiter)

Find root of a function within an interval.

False position method to find a zero of the function f(x) between the x_l and x_u.
## Parameters
* func : function
    Function to evaluate. Note that f(x_l) and f(x_u) can not have the same signs.
* x_l, x_u : float
    Ends of the bracketing interval [x{l, x_u].
* xtol : float, optional
    Convergence tolerance in x axis, defaults to 1e-08.
* ytol : float, optional
    Convergence tolerance in y axis, defaults to 1e-08.
* maxiter : int, optional
    Maximum number of iterations, defaults to 500

## Outputs
* x_r : Zero of f between x_l and x_u.
* err : the error in the approximation
* iter : the times of iteration.

## Example
`>> [x_r, err, iter]=regula('- (25*x^4)/216 + 5*x^2 - 30',0.1,5.9,1e-8,1e-8,20);`
