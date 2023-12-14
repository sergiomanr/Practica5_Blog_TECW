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


def pintar_lineas(rango,frecuencia_relativa, labels, titulo='Frecuencias relativas de trayectos de k paradas'):
    for f, l in zip(frecuencia_relativa, labels):
        plt.plot(rango,f, label=l)
    plt.legend()
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

D_residentes_sumado = []
D_visitantes_sumado = []

for a, b in zip(D_residentes, D_visitantes):
    D_residentes_sumado.append(sum(a))
    D_visitantes_sumado.append(sum(b))


# %% APARTADO B
#Apartado B
lista_desp_sumado = D_visitantes_sumado[:int(n_desplazamientos/5)]+D_residentes_sumado[:int(n_desplazamientos*4/5)]
lista_desp = D_visitantes[:int(n_desplazamientos/5)] + D_residentes[:int(n_desplazamientos*4/5)]
lista_combinada = ['v']*int(n_desplazamientos/5) + ['r']*int(n_desplazamientos*4/5)


# %% APARTADO C
#Apartado C
fr_trayectos_k_paradas = [[], [], []]
rango = range(max(max(N_residentes),max(N_visitantes))+1)

for k in rango:
    frecuencia_rel_residentes = 0
    frecuencia_rel_visitantes = 0
    frecuencia_relativa_total = 0
    for tiempos,viajero in zip(lista_desp,lista_combinada):
        if len(tiempos) == k:

            if viajero == 'v':
                frecuencia_rel_visitantes += 1
            else:
                frecuencia_rel_residentes += 1

    frecuencia_relativa_total = frecuencia_rel_residentes + frecuencia_rel_visitantes
    print('\n K = ' + str(k) + ' paradas')
    print('Frecuencia relativa de trayectos de ' + str(k) + ' paradas (residentes): ' + str(frecuencia_rel_residentes/n_desplazamientos))
    print('Frecuencia relativa de trayectos de ' + str(k) + ' paradas (visitantes): ' + str(frecuencia_rel_visitantes/n_desplazamientos))
    print('Frecuencia relativa de trayectos de ' + str(k) + ' paradas (total): ' + str(frecuencia_relativa_total/n_desplazamientos))

    fr_trayectos_k_paradas[0].append(frecuencia_rel_residentes/n_desplazamientos)
    fr_trayectos_k_paradas[1].append(frecuencia_rel_visitantes/n_desplazamientos)
    fr_trayectos_k_paradas[2].append(frecuencia_relativa_total/n_desplazamientos)

    # plot de las frecuencias relativas
pintar_lineas(rango,frecuencia_relativa=fr_trayectos_k_paradas ,labels=['Residentes','Visitantes','Total'])


# %% APARTADO D
#Apartado D

# pintar_histograma(fr_trayectos_k_paradas,bins=max(max(N_residentes),max(N_visitantes)))
pintar_histograma(fr_trayectos_k_paradas, bins=15)

# %% APARTADO E
#Apartado E
suma_trayectos = []
for desp,viajero in zip(lista_desp_sumado,lista_combinada):
   
    if viajero == 'r':
        suma_trayectos.append(desp)
        
else:
    print(np.mean(suma_trayectos))
    print(np.var(suma_trayectos))

# %% APARTADO F
# Apartado F

pintar_histograma(suma_trayectos,bins=int(max(D_residentes_sumado)))

# %% APARTADO G
# Apartado G
suma_trayectos_vis = []
for desplazamiento,viajero in zip(lista_desp_sumado,lista_combinada):
   
    if viajero == 'v':
        suma_trayectos_vis.append(desplazamiento)
else:
    print(np.mean(suma_trayectos_vis))
    print(np.var(suma_trayectos_vis))

pintar_histograma(suma_trayectos_vis,bins=int(max(D_visitantes_sumado)))

# %% APARTADO H
# Apartado H

lista_H = []
for i in range(n_desplazamientos):
    lista_H.append(len(lista_desp[i]))

pintar_histograma_conjunto(lista_H,lista_desp_sumado,bins=max(max(N_residentes),max(N_visitantes)))

# %% APARTADO I
# Apartado I
lista_I = []
for i in range(n_desplazamientos):
    lista_I.append(len(D_visitantes[i]))


pintar_histograma_conjunto(lista_H[20000:],lista_desp_sumado[20000:],titulo='Residentes', bins=25 )
pintar_histograma_conjunto(lista_I,D_visitantes_sumado,titulo='Visitantes', bins=25 )


# %% APARTADO J
# Apartado J


# %% APARTADO K
# Apartado K
base = 2

valores_paradas = []
precio = []
for i in range(n_desplazamientos):
    valores_paradas.append(len(lista_desp[i]))
precio = np.emath.logn(base, 1+np.asanyarray(valores_paradas))


# %% APARTADO L
# Apartado L

pintar_histograma(precio, bins=15)
print('Media',np.mean(precio),'\nVarianza',np.var(precio))

# %% APARTADO M
# Apartado M
lista_b = []
medias_b = []
varianza_b = []

for i in np.arange(0.0,3.0,0.1):
    precio = np.emath.logn(i, 1+np.asanyarray(valores_paradas))
    medias_b.append(np.mean(precio))
    varianza_b.append(np.var(precio))

lista_b = [medias_b] + [varianza_b]
pintar_lineas(np.arange(0.0,3.0,0.1),frecuencia_relativa=lista_b, labels=['Media','Varianza','Precio'])

# %% APARTADO N
# Apartado N

lista_N = []
for i in range(n_desplazamientos):
    lista_N.append(len(lista_desp[i]))

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


# %% APARTADO O
# Apartado O
transbordos = []
numeros_de_transbordos = []

for traye in lista_desp:
    if len(traye) >= 2:
        traye_transbordos = []
        contador_parada = 0

        for parada in traye[:-1]:
            if np.random.random() >= 3/4:
                traye_transbordos.append(np.random.uniform(0,9))
                contador_parada +=1
        if len(traye_transbordos) == 0:
            transbordos.append([0])
        else:
            transbordos.append(traye_transbordos)
        numeros_de_transbordos.append(contador_parada)
    else:
        transbordos.append([0])
        numeros_de_transbordos.append(0)

# %% APARTADO P
# Apartado P

pintar_histograma_conjunto(lista_N, numeros_de_transbordos,bins=20)

# %% APARTADO Q
# Apartado Q
duraciones_transbordos = []
for par,trsb in zip(lista_desp, transbordos):
    suma_tot = sum(par)+sum(trsb)
    duraciones_transbordos.append(suma_tot)

pintar_histograma_conjunto(duraciones_transbordos,lista_desp_sumado,bins=max(max(N_residentes),max(N_visitantes)))


# %% APARTADO R
# Apartado R

pintar_histograma(numeros_de_transbordos,bins=20)
print('Media',np.mean(numeros_de_transbordos),'\nVarianza',np.var(numeros_de_transbordos))

# %% APARTADO S
# Apartado S

np.corrcoef(lista_N, numeros_de_transbordos)[0, 1]

# No es mucho ya que solo tenemos un 25% se prob de meter un transbordo y por eso no es tan alto
# %% APARTADO T
# Apartado T
duracion_solo_transbordos = []

for trasb, desplaz in zip(numeros_de_transbordos,lista_desp):
    if trasb > 0: 
        sumatorio_t = [np.random.uniform(0,9) for _ in range(trasb)]
        duracion_solo_transbordos.append(sum(sumatorio_t)+sum(desplaz))

print('Media con todos los trayectos incluyendo los transbordos',np.mean(duraciones_transbordos))
print('Media solo con los viajes que tienen al menos un transbordo',np.mean(duracion_solo_transbordos))
print('Media de los desplazamientos sin transbordos',np.mean(suma_trayectos))


# %%
