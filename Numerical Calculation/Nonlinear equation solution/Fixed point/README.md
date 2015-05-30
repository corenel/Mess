# Fixed point method
## Introduction
    function [x,iter,err,Solutions] = fixpt(func,x0,xtol,maxiter)

Find a fixed point of the function.

Given a function and a starting point, find a fixed-point of the function: i.e. where func(x0) == x0.
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
* x : the approximation to the function.
* iter : the number of iterations carried out.
* err : the error in the approximation
* Solutions : the list of solutions.

## Example:
    >> [iter,x,err,Solutions] = fixpt('1 + 1 / x',1,1e-8,500);
