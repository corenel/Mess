# Gauss-Seidel method
## Introduction
`function [x, iter] = Jacobi(A,b,x0,tol,maxiter)`
Solves the linear system Ax=b using the Jacobi method.

## Parameter
* A: an n x n nonsingular matrix: coefficient Matrix.
* b: an n x 1 matrix: adjoint Matrix.
* x0: an n x 1 matrix; the initial guess. default ALL ZERO MATRIX.
* tol: the tolerance for P. default 1e-16.
* maxiter: the maximum number of iterations. default 500.

## Output
* x is an n x 1 matrix: the SOR approximation to the solution of Ax = b.
* iter: the times of iterations.

## Example
`>> [x,iter] = Jacobi(A,b);`
