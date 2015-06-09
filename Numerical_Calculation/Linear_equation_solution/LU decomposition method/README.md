# LU decomposition method
## Introduction
`function x = LUmethod(A,b)`
Solves the linear system Ax=b using the LU decomposition method.

## Parameter
* A: an n x n nonsingular matrix: coefficient Matrix.
* b: an n x 1 matrix: adjoint Matrix.

## Output
* x is an n x 1 matrix: the SOR approximation to the solution of Ax = b.

## Example
`>> [x,iter] = LUmethod(A,b);`
