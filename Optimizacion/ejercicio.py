# import time
# lista = [1,2,3,9]
# lista1 = [1,2,4,4]
# objetivo = 8
# def obtener_sumandos(lista,objetivo):
#     for i in lista:
#         resto = objetivo -i
#         if resto in lista:
#             print(i,'+',resto,'=',objetivo)
# def bajo_arriba(lista,objetivo):
#     bajo = 0
#     alto = len(lista)-1
#     while bajo<alto:
#         if lista[bajo]+lista[alto] == objetivo:
#             print('Se encuentran en las posiciones',bajo,'y',alto)
#             break
#         elif lista[bajo]+lista[alto] > objetivo:
#             alto -= 1
#         elif lista[bajo]+lista[alto] < objetivo:
#             bajo +=1

# if __name__ == '__main__':
#     f1 = time.time()
#     obtener_sumandos(lista1,objetivo)
#     f2 = time.time()
#     print('Ha tardado',f2-f1)

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fmin

'''ax = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.09)

# Plot the 3D surface
ax.plot_surface(X, Y, Z, edgecolor='yellow', lw=0.5, rstride=4, cstride=4,
                alpha=0.5)

# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')

ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100),
       xlabel='X', ylabel='Y', zlabel='Z')

plt.show()'''

def f(x, y):
    # return ((x-1)**2+5*(y-1)**2-2*x*y)*2.71**(-x)
    return ((x**2-y**2))

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)
Z = f(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='pink')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.xlim([-25, 25])
plt.ylim([-25, 25])

# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)
# z = ((x-1)**2+5*(y-1)**2-2*x*y)*2.71**(-x)
# ax = plt.axes(projection='3d')
# fig = plt.figure()
# ax.contour3D(x,y,z, 50, cmap='ocean')

# ax.view_init(45)
plt.show()