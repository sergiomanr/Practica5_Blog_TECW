#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Introducción a Numpy
"""

import numpy as np

# Vectors and matrices

# Creation of a vector
x0 = np.zeros((3))
x1 = np.ones((3))
x2 = np.array([1,2,3])
# print(x0,'\n',x1,'\n',x2)
# print('Fin de vectores')
# Creation of a matrix
A0 = np.zeros((3,3))
A1 = np.ones((3,3))
A2 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
A3 = np.random.rand(3,3)

# Creation of matrix by blocks
B0 = np.zeros((2,2))
B1 = np.ones((2,2))
B = np.concatenate((B0,B1),axis=0)
B = np.block([[B0, B1], [B1, B0]])

x_list = [x0, x1, x2, A0, A1, A2]
for x in x_list:
    print(x)
    print('Dimensión',np.ndim(x))
    print('Forma',np.shape(x))
    print()
    
# Obtaining elements of a vector or matrix
x2[0] 
x2[-1]
A2[0,0]
A2[-1,-1]


# Obtaining subvectors and submatrices
x2[0:1]
x2[0:2]
A2[0:2,1]
A2[0:1,1:2]

# Transposition
np.transpose(x0) # Does nothing
x0.T
np.transpose(A2)
A2.T

# Arithmetic operations with vectors and matrices
x1 + x2
x1 * x2
x2 ** 2
A1 + A2
A2 * A2
A2 @ x1
x1 @ A2
A1 @ A2
A2 ** 2

# -----------------------------

# Matrix functions
np.linalg.inv(A3)
np.linalg.eig(A3)
np.linalg.matrix_rank(A3)
np.linalg.solve(A3,x1)
    
# -----------------------------------

# Mathematical functions

np.exp(1)
np.exp(x2)
np.exp(A2)

# -----------------------------------
# -----------------------------------
