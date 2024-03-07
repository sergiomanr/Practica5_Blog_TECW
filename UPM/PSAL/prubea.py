import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Parámetros del problema
media_z = np.array([0, 0])
covarianza_z = np.array([[1, -0.5], [-0.5, 1]])

# Generar datos para la FDP de segundo orden
x, y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
pos = np.dstack((x, y))
fdp_segundo_orden = -multivariate_normal(mean=media_z, cov=covarianza_z).pdf(pos) * (
    (x - media_z[0]) ** 2 / covarianza_z[0, 0] - 1 +
    (y - media_z[1]) ** 2 / covarianza_z[1, 1] - 1 +
    (covarianza_z[0, 1] / (covarianza_z[0, 0] * covarianza_z[1, 1])) * (x - media_z[0]) * (y - media_z[1])
) / 2

# Crear la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la FDP de segundo orden en 3D
ax.plot_surface(x, y, fdp_segundo_orden, cmap='viridis')

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('FDP de Segundo Orden')
ax.set_title('FDP de Segundo Orden de Z[n] en 3D')

# Mostrar la figura
plt.tight_layout()