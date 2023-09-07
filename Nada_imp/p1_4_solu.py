#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:46:33 2023

@author: J.I.R.
"""

"""
   Queremos hallar el polinomio de la foraa 
     a + b*z + c*z^2
   que multiplicado por 
     1 + z + z**2
   nos dé un polinomio lo más cercano posible a
     z**2
"""
import sympy as sp

z = sp.symbols('z')
a,b,c = sp.symbols('a b c')
p = 1 + z + z**2
q = a + b*z + c*z**2
target = sp.poly(z**2, z)

r = sp.expand(p*q)
R = sp.poly(r,z)
grado = sp.polys.polytools.degree(R)
coefs = R.all_coeffs()
var = [a,b,c]
A = sp.zeros(grado+1, len(var))
for i in range(grado+1):
    for j in range(len(var)):
        A[i,j] = coefs[i].diff(var[j])
target_coefs = target.all_coeffs()        
# b = sp.Matrix([0] * (len(coefs)-len(target_coefs)) + target_coefs)
b = sp.Matrix([0,0,1,0,0])

x = (A.T*A).inv()*A.T*b
print(x)

    



