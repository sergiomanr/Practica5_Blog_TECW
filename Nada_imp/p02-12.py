#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 19:29:36 2022

@author: cmp
"""
import matplotlib as mpl 
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize


def f1(x1,x2):
    return x1**2-x2**2

def f2(x1,x2):
    return 2*x1*x2

def equations(p):
    x1,x2=p
    return [f1(x1,x2)-12,f2(x1,x2)-16]

fig, ax = plt.subplots()  # Una figura con un eje
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
x1=np.linspace(-10,10,1000)
x2=np.linspace(-10,10,1000)
X1,X2=np.meshgrid(x1,x2)
Z=f1(X1,X2)
c1=ax.contour(X1,X2,Z,[12],colors='red')
ax.clabel(c1,[12],inline=True, fontsize=10,manual=[(7.5,6),(-7.5,-6)])
c2=ax.contour(X1,X2,f2(X1,X2),[16],colors='blue')
ax.clabel(c2,[16],inline=True, fontsize=10,manual=[(1,5),(-1,-5)])
x,y=scipy.optimize.fsolve(equations,[-10,-10])
ax.plot(x,y,'go',ms=5)
x,y=scipy.optimize.fsolve(equations,[10,10])
ax.plot(x,y,'go',ms=5)
ax.grid(visible=True, axis='both')
plt.savefig('p0509.eps',format='eps',papertype='a6')
plt.show()


