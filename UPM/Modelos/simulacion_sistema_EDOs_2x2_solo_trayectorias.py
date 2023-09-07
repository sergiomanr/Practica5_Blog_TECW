import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definimos de la funciones que caracterizan el sistema de EDOS
################################################################
# Vector de campo
def f(X, t):
    x1, x2 = X
    return [(-2)*x1+(1)*x2,(4)*x1+(-2)*x2]  

# Para pintar solamente trayectorias que nacen en punto elegido
# Definimos rango del dibujo
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.xlim([-2, 2])
plt.ylim([-2, 2])

# Vector de campo
def f(X, t):
    x1, x2 = X
    return [(-2)*x1+(1)*x2,(4)*x1+(-2)*x2] 

# Elegimos un rango de tiempos y una condición inicial
tspan = np.linspace(0, 8, 2000)
xini=[0.1,-1.5]
xs=odeint(f,xini,tspan)
plt.plot(xs[:,0], xs[:,1], 'b-')
plt.plot([xs[0,0]], [xs[0,1]], 'o') # (círculo para comienzo de trayectoria)
plt.plot([xs[-1,0]], [xs[-1,1]], 's') # (cuadrado para final de trayectoria)

plt.show()
