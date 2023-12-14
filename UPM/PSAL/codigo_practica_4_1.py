'''
PSAL - PRÁCTICA 4 - 2023-2024

'''
# %%
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import sounddevice as sd   # pip install sounddevice --user


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


def pintar_lineas(rango, frecuencia_relativa, labels, titulo='Frecuencias relativas de trayectos de k paradas'):
    for f, l in zip(frecuencia_relativa, labels):
        plt.plot(rango, f, label=l)
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
    
    
def almacenar_audio(fname,seq,fs):
    # Almacena una secuencia en una única pista de audio
    data = np.int16(seq / np.max(np.abs(seq)) * 32767)
    write(fname,fs,data)
    
    
def almacenar_audio_2canales(fname,armonia,melodia,fs,L):
    # Almacena dos secuencias en una única pista de audio
    
    # Fusionar las dos secuencias
    x = melodia
    x[range(0,len(x),L)] = armonia[range(0,len(x),L)]
    
    # Almacena la secuencia única
    almacenar_audio(fname,x,fs)
    
    
def reproducir_secuencia(seq,fs):    
    sd.play(seq, fs)
    
        
def sintetizador_secuencia(seq,fs):
    print()
    # Transforma la secuencia de frecuencias en tonos de duración fija
    T = 0.5
    N = int(np.floor(T*fs))
    
    # Crea un array de tonos
    print(len(seq))
    x = np.zeros((len(seq),N))
    n = np.arange(0,N)
    
    for i in range(0,len(seq)):
        x[i,:] = np.sin(2*np.pi*seq[i]/fs*n)
        
    return x
    
    
def transformador_armonia(seq):    
    return [notas[armonias[s]] for s in seq.tolist()]
    
    
def transformador_melodia(seq):
    return [notas[melodias[s]] for s in seq.tolist()]
    

armonias = {
    1 : "La",
    2 : "Do",
    3 : "Re",
    4 : "Fa"
    }

melodias = {
    1 : "La",
    2 : "Fa",
    3 : "Do",
    4 : "Re"
    }

notas = {
    "Do" : 261.62,
    "Re" : 293.66,
    "Mi" : 329.62,
    "Fa" : 349.22,
    "Sol" : 391.88,
    "La" : 440.00,
    "Si" : 987.76
    }


Tab1 = np.array([[0.480,0.050,0.240,0.230],
                 [0.317,0.221,0.245,0.217],
                 [0.880,0.058,0.050,0.012],
                 [0.120,0.360,0.220,0.300]],np.float32)


Tab2 = np.array([[0.670,0.110,0.090,0.130],
                 [0.880,0.058,0.050,0.012],
                 [0.317,0.221,0.245,0.217],
                 [0.120,0.360,0.220,0.300]],np.float32)

Tab3 = np.array([[0.880,0.058,0.050,0.012],
                 [0.000,0.510,0.000,0.490],
                 [0.551,0.197,0.136,0.116],
                 [0.317,0.221,0.245,0.217]],np.float32)




# %% EJEMPLO

# Frecuencia de muestreo DAC
fs=8000

# Secuencia aleatoria de notas de armonia
x = np.random.randint(2, size=10)+1

# Sintetizamos la secuencia: estructura en array
y = sintetizador_secuencia(transformador_armonia(x),fs)


# Concatenamos las muestras: un sonido detrás de otro
y = y.flatten()

# Almacenamos el resultado en fichero de audio
almacenar_audio('test.wav',y,fs)

# Reproducimos
reproducir_secuencia(y,fs)





# %% APARTADO A
# Apartado A

muestras = 10000
m_m = np.random.randint(low=1,high=5,size=muestras)


# %% APARTADO B
lista = []
for i in m_m:
    e_1 = np.random.choice((1,2,3,4),p=Tab1[i-1])
    e_2 = np.random.choice((1,2,3,4),p=Tab1[e_1-1])
    e_3= np.random.choice((1,2,3,4),p=Tab1[e_2-1])

    lista.append([i,e_1,e_2,e_3])
lista = np.asarray(lista)


# %% APARTADO C
muestras = 10000
m_ar_0 = np.random.randint(low=1,high=5,size=muestras)
m_ar = []

for ma in m_ar_0:
    m_ar.append(np.random.choice((1,2,3,4),p=Tab1[ma-1]))



# %% APARTADO D
lista_a = []
for n0,n1 in zip(m_ar_0,m_ar):
    n2 = np.random.choice((1,2,3,4),p=Tab2[n1-1])
    n3 = np.random.choice((1,2,3,4),p=Tab2[n2-1])

    lista_a.append([n0,n1,n2,n3])
lista_a = np.asarray(lista_a)

# %% APARTADO E
contador_1 = 0
frecuencia_12 = 0
frecuencia_123 = 0
mas_probable = {}
general = {}

for e in lista:
    if e[0] == 1:
        contador_1 +=1
        if e[1]==2:
            frecuencia_12 +=1
            if e[2] == 3:
                frecuencia_123 +=1

        elif [e[1],e[2]] == [1,2]:
            frecuencia_12 +=1
            if e[3] == 3:
                frecuencia_123 += 1
        
        elif [e[2],e[3]] == [1,2]:
            frecuencia_12 +=1

        if e[2] not in mas_probable:
            mas_probable[e[2]] = 0
        mas_probable[e[2]] += 1
    if e[0] not in general:
        general[e[0]] = 0
    general[e[0]] += 1


print('Frecuencia relativa de (M1,M2) es:',frecuencia_12/contador_1)
print('Frecuencia relativa de (M1,M2,M3) es:',frecuencia_123/contador_1)
print('Valor más probable en M[2] cuando M[0]=1 es:',max(mas_probable,key=mas_probable.get))


    
# %% APARTADO F:
pintar_histograma(lista, bins=4)
pintar_histograma(lista_a,bins=8)


# %% APARTADO G
arm = []
mel = []
k = 8
A2 = np.random.randint(low=1,high=5)
arm.append(A2)
mel.append(np.nan)
for i in range(k):
    m = np.random.choice((1,2,3,4),p=Tab3[A2-1])
    m1 = np.random.choice((1,2,3,4),p=Tab1[m-1])
    m2 = np.random.choice((1,2,3,4),p=Tab1[m1-1])
    A2 = np.random.choice((1,2,3,4),p=Tab2[A2-1])
    
    if i+1 == k: 
        mel.extend([ m, m1, m2])
        arm.extend([np.nan, np.nan, np.nan])
    else:
        mel.extend([ m, m1, m2,np.nan])
        arm.extend([np.nan, np.nan, np.nan, A2])

# %%
canciones_a = []
canciones = []
canciones_m = []
for i in m_ar_0:
    arm = []
    mel = []
    k = 8
    A2 = i
    arm.append(A2)
    mel.append(0)
    unica = []
    unica.append(A2)
    for e in range(k):
        m = np.random.choice((1,2,3,4),p=Tab3[A2-1])
        m1 = np.random.choice((1,2,3,4),p=Tab1[m-1])
        m2 = np.random.choice((1,2,3,4),p=Tab1[m1-1])
        A2 = np.random.choice((1,2,3,4),p=Tab2[A2-1])
        if e+1 == k:
            unica.extend([m, m1, m2])
        else:
            unica.extend([m, m1, m2, A2])
    
        if e+1 == k:
            mel.extend([ m, m1, m2])
            arm.extend([0, 0, 0])
        else:
            mel.extend([ m, m1, m2, 0])
            arm.extend([0, 0, 0, A2])

    canciones_a.append(arm)
    canciones_m.append(mel)
    canciones.append(unica)


# %% APARTADO H
contador = 0
contador_2 = 0
arm_comun = {}
for armo,melo in zip(canciones_a,canciones_m):
    for a in range(0,len(armo),4):
        if [armo[a],melo[a+1],melo[a+2],melo[a+3]] == [1,1,2,3]:
            contador += 1
        if [melo[a+1],melo[a+2],melo[a+3]] == [1,2,3]:
            contador_2 += 1 
            if armo[a] not in arm_comun:
                arm_comun[armo[a]] = 0
            arm_comun[armo[a]] +=1

print(max(arm_comun,key=arm_comun.get), arm_comun)
print(contador/80000,'\nEn el ejercicio es 0.0027')
'''No sale ni un dos porque en la tabla 3 la prob de que m sea 1 siendo A2 2 es 0'''
# %% APARTADO I


# %% APARTADO J
def flatten_concatenation(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list
melodia = flatten_concatenation(canciones_m)
armonia = flatten_concatenation(canciones_a)
# np.correlate(np.asanyarray(canciones).flatten(),np.asanyarray(canciones).flatten(), mode='full')
np.correlate(canciones_a[0],canciones_m[0],mode='full')
# %% APARTADO K


# print(Tab1@[0,0,1,0])
# print([1,0,0,0]@Tab1@Tab1)
# print('A2 sabiendo ',Tab2@[0,0,1,0])

# print([0,0,1,0]@np.linalg.inv(Tab2)@np.linalg.inv(Tab2))
# print(Tab1@Tab1@[1,0,0,0])
# print(Tab2@Tab2)
diccionario = {}
for amon in lista_a:
    if amon[2] == 3:
        if amon[0] not in diccionario:
            diccionario[amon[0]] = 0
        diccionario[amon[0]] += 1
print(max(diccionario, key=diccionario.get))


print('b) del escrito',[0.25,0.25,0.25,0.25]@Tab2@Tab2)
print('c) del escrito',[0.25,0.25,0.25,0.25]@Tab1@[1,0,0,0],'\n otro calculo ',[0.25,0.25,0.25,0.25]@Tab2@[0,0,1,0],'\n segunda parte',[0.25,0.25,0.25,0.25]@Tab2@[0,0,1,0])
'''La de A2=3 hay que hacer [1,0,0,0], [0,1,0,0],[0,0,1,0],[0,0,0,1] y luego la multiplicamos por las tablas'''

# Revise el ejemplo del principio

# %% APARTADO K
fs=8000

# Sintetizamos la secuencia: estructura en array
y = sintetizador_secuencia(canciones[0],fs)


# Concatenamos las muestras: un sonido detrás de otro
y = y.flatten()

# Almacenamos el resultado en fichero de audio
almacenar_audio('cancion.wav',y,fs)

# Reproducimos
reproducir_secuencia(y,fs)