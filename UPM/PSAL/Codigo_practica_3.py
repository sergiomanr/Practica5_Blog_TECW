'''
PSAL - PRÁCTICA 3

'''
# %%
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def pintar_funcion_densidad(distribucion, tipo):
    fig, ax = plt.subplots(1, 1)
    x = np.arange(distribucion.ppf(0.01), distribucion.ppf(0.99) + 1)
    if tipo == 'discreta':
        ax.plot(x, distribucion.pmf(x), 'bo', ms=8)
        ax.vlines(x, 0, distribucion.pmf(x), colors='b', lw=5, alpha=0.5)
    elif tipo == 'continua':
        ax.plot(x, distribucion.pdf(x), 'bo', ms=2)
    else:
        assert False, 'Indique un tipo de distribución válido'
    plt.show()


def pintar_funcion_distribucion(distribucion, tipo='discreta'):
    fig, ax = plt.subplots(1, 1)
    x = np.arange(distribucion.ppf(0.01), distribucion.ppf(0.99) + 1)
    ax.plot(x, distribucion.cdf(x), 'bo', ms=8)
    if tipo == 'discreta':
        ax.vlines(x, 0, distribucion.cdf(x), colors='b', lw=5, alpha=0.5)
    plt.show()


def pintar_histograma(muestras, titulo='Histograma', bins=0):
    if bins == 0:
        bins = range(int(min(muestras)), int(max(muestras)) + 2)
    plt.hist(muestras, bins=bins)
    plt.title(titulo)
    plt.show()


def pintar_lineas(frecuencia_relativa, labels, titulo='Frecuencias relativas de trayectos de k paradas'):
    for f, l in zip(frecuencia_relativa, labels):
        plt.plot(f, label=l)
    plt.legend()
    plt.xticks(np.arange(len(frecuencia_relativa[0])))
    plt.title(titulo)
    plt.show()


def pintar_histograma_conjunto(variable_x,
                               variable_y,
                               bins,
                               titulo='Histograma conjunto',
                               xlabel='Variable X',
                               ylabel='Variable Y'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].hist2d(variable_x, variable_y, bins=bins)
    ax[0].set_xlabel(xlabel)
    ax[0].set_ylabel(ylabel)
    ax[0].set_title('Histograma 2D conjunto')

    ax[1].hist(variable_x, bins=bins, label=xlabel, color='blue', alpha=0.5)
    ax[1].set_xlabel(xlabel)
    ax[1].set_ylabel('Frecuencia')
    ax[1].set_title('Histograma conjunto')
    ax2 = ax[1].twiny()
    ax2.hist(variable_y, bins=50, label=ylabel, color='red', alpha=0.5)
    ax2.set_xlabel(ylabel)

    fig.suptitle(titulo)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()


# %% APARTADO A
#Apartado A
n_desplazamientos = 100000

N_residentes = random.poisson(lam=1,size=n_desplazamientos)
N_visitantes = random.poisson(lam=4,size=n_desplazamientos)


D_residentes = []
D_visitantes = []
for i in range(n_desplazamientos):

    paradas_res = []
    for e in range(N_residentes[i]):
        paradas_res.append(random.exponential(3))
    else:
        D_residentes.append(paradas_res)
    paradas_vis = []
    for e in range(N_visitantes[i]):
        paradas_vis.append(random.exponential(3))
    else:
        D_visitantes.append(paradas_vis)

# D_residentes_sumado = []
# D_visitantes_sumado = []
# for i in range(n_desplazamientos):

#     paradas_res = 0
#     for i in range(random.poisson(1)):
#         paradas_res += random.exponential(3)
#     else:
#         D_residentes_sumado.append(paradas_res)
#     paradas_vis = 0
#     for i in range(random.poisson(4)):
#         paradas_vis += random.exponential(3)
#     else:
#         D_visitantes_sumado.append(paradas_vis)


# %% APARTADO B
#Apartado B
# lista_desp_sumado = D_visitantes_sumado[:20000]+D_residentes_sumado[20000:]
lista_desp = D_visitantes[:20000] + D_residentes[:80000]
lista_combinada = ['v'] * 20000 + ['r']*80000


# %% APARTADO C
#Apartado C
fr_trayectos_k_paradas = [[], [], []]
rango = range(max(max(N_residentes),max(N_visitantes)))

for k in rango:
    frecuencia_rel_residentes = 0
    frecuencia_rel_visitantes = 0
    frecuencia_relativa_total = 0
    contador_res = 0
    contador_vis = 0

    for tiempos,viajero in zip(lista_desp,lista_combinada):
        if len(tiempos) == k:

            if viajero == 'v':
                contador_vis += 1
                frecuencia_rel_visitantes += sum(np.asanyarray(tiempos))
            else:
                contador_res += 1
                frecuencia_rel_residentes += sum(np.asanyarray(tiempos))
    frecuencia_relativa_total = frecuencia_rel_residentes + frecuencia_rel_visitantes
    contador_tot = contador_vis +contador_res
    # print('\n K = ' + str(k) + ' paradas')
    # print('Frecuencia relativa de trayectos de ' + str(k) + ' paradas (residentes): ' + str(frecuencia_rel_residentes/(1 if contador_res == 0 else contador_res)))
    # print('Frecuencia relativa de trayectos de ' + str(k) + ' paradas (visitantes): ' + str(frecuencia_rel_visitantes/(1 if contador_vis == 0 else contador_vis)))
    # print('Frecuencia relativa de trayectos de ' + str(k) + ' paradas (total): ' + str(frecuencia_relativa_total/(1 if contador_tot == 0 else contador_tot)))

    fr_trayectos_k_paradas[0].append(frecuencia_rel_residentes)
    fr_trayectos_k_paradas[1].append(frecuencia_rel_visitantes)
    fr_trayectos_k_paradas[2].append(frecuencia_relativa_total)

    # plot de las frecuencias relativas
pintar_lineas(frecuencia_relativa=fr_trayectos_k_paradas ,labels=['Residentes','Visitantes','Total'])


# %% APARTADO D
#Apartado D
for hist in fr_trayectos_k_paradas:
    pintar_histograma(hist,bins=max(max(N_residentes),max(N_visitantes)))

# %% APARTADO E
#Apartado E
suma_trayectos = []
for tray,viajero in zip(lista_desp,lista_combinada):
   
    if viajero == 'r':
        suma_trayectos.append(sum(np.asanyarray(tray)))
else:
    print(np.mean(suma_trayectos))
    print(np.std(suma_trayectos))


# %% APARTADO F
# Apartado F

pintar_histograma(fr_trayectos_k_paradas[0],bins=max(max(N_residentes),max(N_visitantes)))

# %% APARTADO G

suma_trayectos_vis = []
for tray,viajero in zip(lista_desp,lista_combinada):
   
    if viajero == 'v':
        suma_trayectos_vis.append(sum(np.asanyarray(tray)))
else:
    print(np.mean(suma_trayectos_vis))
    print(np.std(suma_trayectos_vis))

# %% APARTADO H
# Apartado H

pintar_histograma_conjunto(np.arange(max(max(N_residentes),max(N_visitantes))),fr_trayectos_k_paradas[0],bins=16)

# %% APARTADO I

for tipo in fr_trayectos_k_paradas[:2]:
    pintar_histograma_conjunto(np.arange(len(tipo)),tipo, bins=16)

# %% APARTADO J



# %% APARTADO K
base = 3

precio = []
for i in range(n_desplazamientos):
    valor = 1+len(lista_desp[i])
    precio.append(np.emath.logn(base,valor))

# %% APARTADO L

pintar_histograma(precio, bins=10)
print(np.mean(precio),np.var(precio))

# %% APARTADO M

# pintar_lineas()

# %% APARTADO N
lista_N = []
for i in range(n_desplazamientos):
    lista_N.append(len(lista_desp[i]))
# %%
# Apartado H
import time
star = time.time()
b = 3
a = 4
while True:
    precio_b = np.emath.logn(b,1+np.asanyarray(lista_N))
    if round(np.mean(precio_b),4) == 3:
        print('El valor de b para que la media de precio sea 3 es',b)
        break
    else:
        print(b, np.mean(precio_b))
        b -= (3-np.mean(precio_b))/a
        a += 0.5
        continue
print('Tardó',time.time()-star)

# %% APARTADO O

...

# %% APARTADO P

pintar_histograma_conjunto(...)

# %% APARTADO Q

...

pintar_histograma_conjunto(...)

# %% APARTADO R

pintar_histograma(...)

# %% APARTADO S

...

# %% APARTADO T

...