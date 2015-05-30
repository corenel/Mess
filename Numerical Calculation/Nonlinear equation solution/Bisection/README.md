# Basic bisection routine
## Introduction
Find root of a function within an interval.
Basic bisection routine to find a zero of the function f(x) between the x_l and x_u.
## Parameters:
* func : function
    Function to evaluate. Note that f(x_l) and f(x_u) can not have the same signs.
* x_l, x_u : float
    Ends of the bracketing interval [x{l, x_u].
* xtol : float, optional
    Convergence tolerance, defaults to 1e-08.

## Outputs:
* x_r : Zero of f between x_l and x_u.
* err : the error in the approximation
* iter : the times of iteration.

## Example:
`>> [x_r, err, iter]=bisect('- (25*x^4)/216 + 5*x^2 - 30',0.1,5.9,1e-8);`
