from sympy import *
A = Matrix([[0,1,1],
            [1,0,1],
            [1,1,0]])
l = symbols('l')
# A-l*eye(3)
B = Matrix([[-2,-1],
            [-1,-2]])
print()
poly = det(B-l*eye(2))
print(solve(poly,l))        #para que resuelva en 1 (en vez de 0) le ponemos poly-1

