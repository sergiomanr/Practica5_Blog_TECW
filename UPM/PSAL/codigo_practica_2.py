# -*- coding: utf-8 -*-
"""
PSAL - PRÁCTICA 2

"""
# %% APARTADO 0
# Apartado 0
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def pintar_funcion_densidad(distribucion, tipo):
    fig, ax = plt.subplots(1, 1)
    x = np.arange(distribucion.ppf(0.01), distribucion.ppf(0.99) + 1)
    if tipo == "discreta":
        ax.plot(x, distribucion.pmf(x), 'bo', ms=8)
        ax.vlines(x, 0, distribucion.pmf(x), colors='b', lw=5, alpha=0.5)
    elif tipo == "continua":
        ax.plot(x, distribucion.pdf(x), 'bo', ms=2)
    else:
        assert False, "Indique un tipo de distribución válido"
    plt.show()


def pintar_funcion_distribucion(distribucion, tipo="discreta"):
    fig, ax = plt.subplots(1, 1)
    x = np.arange(distribucion.ppf(0.01), distribucion.ppf(0.99) + 1)
    ax.plot(x, distribucion.cdf(x), 'bo', ms=8)
    if tipo == "discreta":
        ax.vlines(x, 0, distribucion.cdf(x), colors='b', lw=5, alpha=0.5)
    plt.show()


def pintar_histograma(muestras, titulo="Histograma", bins=0):
    if bins == 0:
        bins = range(int(min(muestras)), int(max(muestras)) + 2)
    plt.hist(muestras, bins=bins )
    plt.title(titulo)
    plt.show()
    plt.close()


def pintar_histograma_acumulado(distribucion, xlabel="x", ylabel="F(x)"):
    valores_ordenados = np.sort(distribucion)
    p = 1. * np.arange(len(valores_ordenados)) / (len(valores_ordenados) - 1)
    plt.plot(valores_ordenados, p)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    plt.close()


class distribucion_pregunta_examen(stats.rv_continuous):
    def _pdf(self, x, **kwargs):
        return 1/(1/(m+1)-1/(m+2))*(x**m)*(1-x)


# %% APARTADO A
# Apartado A
np.random.seed(2023)
experimentos = 10000
m_list = [1, 2, 3]
muestras_X_por_m = []
Bs = []
for i in m_list:
    Bs.append(round(1/(1/(i+1)-1/(i+2))))

for m, B in zip(m_list, Bs):
    distribucion_X = distribucion_pregunta_examen(a=0, b=1)
    muestras_X_por_m.append(distribucion_X.rvs(size=experimentos))

# %% APARTADO B
# Apartado B
for m, muestras_X in zip(m_list, muestras_X_por_m):
    pintar_histograma(muestras_X, titulo='Histograma', bins=100)

# %% APARTADO C: Calcule con qué frecuencia relativa obtiene valores menores o iguales a 0.5 para los distintos valores de m.
# Apartado C
for muestras_x in muestras_X_por_m:
    print('Frecuencia relativa :',sum(muestras_x <= 0.5)/experimentos)

# %% APARTADO D: Calcule la media, varianza y desvía típica muestrales para m=1, 2, y 3.
# Apartado D
for muestras_x in muestras_X_por_m:
    print(np.mean(muestras_x))
    print(np.var(muestras_x))
    print(np.std(muestras_x))
    print('\n')

# %% APARTADO E: Calcule los valores de los estadísticos superiores skewness y kurtosis para m=1 y 2 y 3.
# Apartado E
for muestras_x in muestras_X_por_m:
    print(stats.skew(muestras_x))
    print(stats.kurtosis(muestras_x))
    print('\n')

# %% APARTADO F: Tome grupos independientes de 3 preguntas con m=2. Calcule la frecuencia relativa de aprobar individualmente las 3 preguntas (calificación ≥0.5 puntos en cada una).
# Apartado F
# poner multiplos de 3 para que no de error
muestras_X_m2 = []
muestras_X_por_grupo = []
expermientos_m2 = 10002
lista_m = [2]
for m in lista_m:
    distribucion_X_m2 = distribucion_pregunta_examen(a=0,b=1)
    muestras_X_m2.append(distribucion_X_m2.rvs(size=expermientos_m2))

contador = 0
muestras_X_por_grupo = np.array_split(muestras_X_m2[0], len(muestras_X_m2[0])/3)

for i in muestras_X_por_grupo:
    if sum(i>=0.5)==3:
        contador +=1
print(contador/(expermientos_m2/muestras_X_por_grupo))

# %% APARTADO G: Se cambia el modo de calificación: Y=1 si X≥b, Y=0 si X <b. En un examen de 10 preguntas independientes e idénticamente distribuidas.
# Apartado G
# Copie las 30.000 realizaciones y aplique la transformación indicada. Asuma que b=0.5


b = 0.5
muestras_Y_por_m = []

for muestras_xg in muestras_X_por_m:
    lista_muestras = []
    for muestra in muestras_xg:
        if muestra >= b:
            lista_muestras.append(1)
        else:
            lista_muestras.append(0)
    else:
        muestras_Y_por_m.append(lista_muestras)

# %% APARTADO H: Calcule el histograma y el histograma acumulado sobre los valores enteros, para cada valor de m, respectivamente.
# Apartado H

for m, muestras_Y_h in zip(m_list, muestras_Y_por_m):
    pintar_histograma(muestras_Y_h, titulo='Histograma', bins=25)
    pintar_histograma_acumulado(muestras_Y_h)
    # print(np.mean(muestras_Y_h))

# %% APARTADO I: Agrupe los realizaciones en grupos de 10 calificaciones.
# Apartado I

muestras_Y_por_grupo_por_m = []

for muestras_x in muestras_X_por_m:
    lista = np.array_split(muestras_x, len(muestras_x)/10)
    muestraY_m = []
    for e in lista:
        muestraY_m.append(sum(e>=b))
    else:
        muestras_Y_por_grupo_por_m.append(muestraY_m)


# %% APARTADO J: Para cada uno de los 3.000 grupos, calcule la suma de las calificaciones. Represente los respectivos histogramas de valores, en función de m.
# Apartado J
import collections

for m, muestras_Y_j in zip(m_list, muestras_Y_por_grupo_por_m):
    pintar_histograma(muestras_Y_j, titulo='Histograma', bins=10)
    pintar_histograma_acumulado(muestras_Y_j)
    # print((collections.Counter(muestras_Y_j)))
    print(np.mean(muestras_Y_j))
    # pintar_funcion_densidad(distribucion_pregunta_examen(a=0,b=1),tipo='continua')
# %% APARTADO K: Calcule la frecuencia relativa con la que un estudiante obtiene una calificación de al menos k puntos. Indique el rango de k. Relacione este valor con la función de distribución y el histograma.
# Apartado K

k = 5
numero_m = 1
for notas_por_m in muestras_Y_por_m:
    calificacion_mayor_k = 0
    for notas in np.array_split(notas_por_m, len(notas_por_m)/10):
        if sum(notas)  >= k:
            calificacion_mayor_k += 1 
    print(f'La frecuencia relativa de que el estudiante tenga {k} o más puntos en m={numero_m} es :', calificacion_mayor_k/1000)
    numero_m += 1
    # pintar_funcion_distribucion(distribucion=)

# %% APARTADO L:
# Apartado L

for muestra_de_m,m_selec in zip(muestras_X_por_m,m_list):
    b = 0.99
    frecuencia = 0
    while True:
        listas_notas = []
        for examenes in np.array_split(muestra_de_m, len(muestra_de_m)/10):
            listas_notas.append(sum(examenes >= b))
  
        contador = np.sum(np.asarray(listas_notas)>=k)
        frecuencia = contador/(len(muestra_de_m)/10)
        
        if frecuencia >= 0.9:
                print(f'La b para que la Fr de {m_selec} sea {frecuencia} ~ 0.9 es: ',round(b,3))
                break
        else:
            b -= 0.005
            continue

# for m, muestras_Y_bis in zip(m_list, muestras_Y_por_grupo_por_m_bis):
#     pintar_histograma(muestras_Y_bis, titulo=f'Histograma de {m}', bins=10)
#     pintar_histograma_acumulado(muestras_Y_bis)



# %% APARTADO M: Se observa que la calificación obtenida en la segunda pregunta está directamente relacionada con la primera, de forma que Z=X**2.
# Apartado M
# Copie las 30.000 realizaciones y aplique la nueva transformación.

muestras_Z_por_m = []
for muestraZ_m in muestras_X_por_m:
    listaZ = []
    for valor in muestraZ_m:
        listaZ.append(valor**2)
    else:
        muestras_Z_por_m.append(listaZ)


# %% APARTADO N: Calcule la media y la desviación típica de la nueva calificación en función de la entrada.
# Apartado N

for Z_N_m in muestras_Z_por_m:
    print(np.mean(Z_N_m))
    print(np.std(Z_N_m),'\n')

# %% APARTADO O: Calcule los histogramas de las 30.000 realizaciones e interprete sus diferencias, separándolas en función del valor de m.
# Apartado O

for valores in muestras_Z_por_m:
    pintar_histograma(valores, titulo='Z por m',bins=25)
    pintar_histograma_acumulado(valores)
    

