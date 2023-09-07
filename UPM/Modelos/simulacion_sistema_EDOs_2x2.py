import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definimos de la funciones que caracterizan el sistema de EDOS
################################################################
# Vector de campo
def f(X, t):
    x1, x2 = X
    return [(-2)*x1+(1)*x2,(4)*x1+(-2)*x2]  


# Valores de las variables (coordenadas en el plano de fases) donde evaluaremos el vector de campo
x1 = np.linspace(-2.0, 2.0, 20)
x2 = np.linspace(-2.0, 2.0, 20)

# Creación de una malla a partir de los valores indicados
X1, X2 = np.meshgrid(x1, x2)

u, v = np.zeros(X1.shape), np.zeros(X2.shape)

# Número de valores evaluados en cada eje
NI, NJ = X1.shape

# Cómputo del vector de campo en las coordenadas elegidas (para el intante inicial t=0)
t = 0
for i in range(NI):
    for j in range(NJ):
        x = X1[i, j]
        y = X2[i, j]
        xprime = f([x, y], t)
        u[i,j] = xprime[0]
        v[i,j] = xprime[1]

# Pintamos los vectores de campo eligiendo como origen los puntos donde se han evaluado  
Q = plt.quiver(X1, X2, u, v, color='r')

plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.xlim([-2, 2])
plt.ylim([-2, 2])
#plt.show()


# Integración de trayectorias durante un intervalo de tiempo a partir de condiciones iniciales en una malla
tspan = np.linspace(0, 50, 2000) #Genera una lista con el rango de tiempos donde queremos evaluar las soluciones
for x10 in [-2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5]:  #Generamos las concidiones iniciales
    for x20 in [-2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5]:
        x0 = [x10, x20]
        xs = odeint(f, x0, tspan)
        plt.plot(xs[:,0], xs[:,1], 'b-') # (pintamos de azul los puntos de las trayectorias)
        plt.plot([xs[0,0]], [xs[0,1]], 'o') # (círculo para comienzo de trayectoria)
        plt.plot([xs[-1,0]], [xs[-1,1]], 's') # (cuadrado para final de trayectoria)
    

#Trayectoria que nace de un punto concreto a elegir:
tspan = np.linspace(0, 2, 20) #Rango de tiempos
xini=[-1,1.5]
xs=odeint(f,xini,tspan)
plt.plot(xs[:,0], xs[:,1], 'b-')

plt.xlim([-2, 2])
#plt.savefig('images/phase-portrait-2.png')
plt.show()
