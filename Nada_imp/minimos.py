import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

def least_squares(A, B):
    # Solves LS problem A*v = B
    v = np.linalg.solve(np.transpose(A) @ A,
                        np.transpose(A) @ B)
    return v

# ------------------------------------------
    

# 3D quadratic regression problem

# Data
Data = np.array([[0,0,0],
                 [1,0,0],
                 [0,2,3],
                 [2,1,3],
                 [3,1,1],
                 [-1,4,5],
                 [3,3,2]])

X, Y, Z = np.transpose(Data)
num_points = Data.shape[0]
ones = np.ones(num_points)

# Plot data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='b', marker='o')

# Solve LS problem
A = np.transpose(np.array((ones, X, Y, X**2, Y**2, X*Y)))

v = least_squares(A, Z)
a_calc, b_calc, c_calc, d_calc, e_calc, f_calc = v

# Show result
xmin = np.min(X)
xmax = np.max(X)
ymin = np.min(Y)
ymax = np.max(Y)
X, Y = np.meshgrid(np.linspace(xmin,xmax,20), np.linspace(ymin,ymax,20))
Z = a_calc + b_calc*X + c_calc*Y + d_calc*X**2 + e_calc*Y**2 + f_calc*X*Y
ax.plot_wireframe(X, Y, Z)
plt.show()