#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: José Ignacio Ronda
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def least_squares(A, B):
    # Solves LS problem A*v = B
    v = np.linalg.solve(np.transpose(A) @ A,
                        np.transpose(A) @ B)
    return v

# ------------------------------------------
    
# Experiments:
# 0: Regression line
# 1: Cuadratic regression curve
# 2: Regression plane
experiment = 1

plt.close('all')

if experiment == 0:
    # Linear regression line
    # Generate data for a linear regression problem
    numpoints = 10
    np.random.seed(0)
    x = np.random.uniform(size=(numpoints, 1))
    noise = np.random.normal(size=(numpoints, 1))
    a = 0.5
    b = 1
    sigma = 0.02
    y = a*x + b + sigma*noise
    
    # Plot data
    plt.figure()
    plt.scatter(x, y)
    
    # Solve LS problem
    A = np.concatenate((x, 
                        np.ones((numpoints, 1))),
                       axis=1)
    v = least_squares(A, y)
    a_calc, b_calc = v
    
    # Show results
    xmin = np.min(x)
    xmax = np.max(x)
    xx = [xmin, xmax]
    # Plot calculated line
    plt.plot(xx, a_calc*xx + b_calc, c='r')
    # Plot approximated points
    plt.scatter(x, a_calc*x + b_calc, c='r')
    plt.show()
    
if experiment == 1:
    # Quadratic model
    
    # Generate data
    if 0:
        numpoints = 40
        np.random.seed(0)
        x = np.random.uniform(size=(numpoints, 1))
        noise = np.random.normal(size=(numpoints, 1))
        a = 10
        b = 4
        c = 1
        sigma = 0.4
        z = a*x**2 + b*x + c + sigma*noise
    else:
        x = np.transpose(np.array([[0,1,2,3]]))
        z = np.transpose(np.array([[0,2,4,5]]))
        numpoints = x.shape[0]
    
    # Plot data
    fig = plt.figure()
    plt.scatter(x, z)
    
    # Solve LS problem
    A = np.concatenate((x**2, x, 
                        np.ones((numpoints, 1))),
                       axis=1)
    v = least_squares(A, z)
    a_calc, b_calc, c_calc = v
    
    # Show result
    if 1:
        xmin = np.min(x)
        xmax = np.max(x)
        xx = np.linspace(xmin, xmax, 100)
        #plt.plot(xx, a*xx**2 + b*xx + c)
        plt.plot(xx, a_calc*xx**2 + b_calc*xx + c_calc)
        plt.scatter(x, a_calc*x**2 + b_calc*x + c_calc, c='r')

if experiment == 2:
    # 3D linear regression problem
    
    # Generate data
    numpoints = 100
    np.random.seed(0)
    x = np.random.uniform(size=(numpoints, 1))
    y = np.random.uniform(size=(numpoints, 1))
    noise = np.random.normal(size=(numpoints, 1))
    a = 0.5
    b = 0.3
    c = 1
    sigma = 0.05
    z = a*x + b*y + c + sigma*noise
    
    # Plot data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='b', marker='o')
    
    # Solve LS problem
    A = np.concatenate((x, y, 
                        np.ones((numpoints, 1))),
                       axis=1)
    v = least_squares(A, z)
    a_calc, b_calc, c_calc = v
    
    # Show result
    if 1:
        xmin = np.min(x)
        xmax = np.max(x)
        ymin = np.min(y)
        ymax = np.max(y)
        X, Y = np.meshgrid(np.linspace(xmin,xmax,20), np.linspace(ymin,ymax,20))
        Z = a_calc*X + b_calc*Y + c_calc
        # ax.plot_wireframe(X, Y, Z)
        ax.plot_surface(X, Y, Z)

# -------------------------------------
