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
# reproducir_secuencia(y,fs)



# %% APARTADO A
ruido_blanco = np.random.randint(low=1, high=8,size=1000)

# %% APARTADO B
frecuencias_f = []
frecuencias = [261.62, 293.66, 329.62, 349.22,391.88, 440.00, 987.76]
for i in ruido_blanco:
    frecuencias_f.append(frecuencias[i-1])

# %% APARTADO C

lista_x = []

for frec in frecuencias_f:
    normal = np.random.normal(0,0.1)
    theta = np.random.uniform(0,2*np.pi)
    x = 1*np.sin(2*np.pi*frec*np.linspace(0,0.5,4000)+theta) + normal
    lista_x.append(x)

lista_x = np.asanyarray(lista_x)

# %% APARTADO D

secuencia_sonido = lista_x.flatten()
almacenar_audio('audioD.wav',secuencia_sonido,fs)
reproducir_secuencia(secuencia_sonido,fs)

# %% APARTADO E
pintar_histograma(frecuencias_f, bins=20)
pintar_histograma(np.random.normal(0,0.1,size=1000), bins=20)
pintar_histograma(lista_x[0], bins=20)

print('\n'+ str(np.mean(frecuencias_f)))
print(np.mean(np.random.normal(0,0.1,size=4000)))
print(np.mean(lista_x[0].flatten()),'\n')

print(np.correlate(frecuencias_f, frecuencias_f, mode='full'))
print(np.correlate(ruido_blanco, ruido_blanco))
print(np.correlate(lista_x[0], lista_x[0]))


# %% APARTADO F

# y = np.random.normal(0,1, size=1000)
sec_por_nota = {
    1:[],
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[]
}
for secuencia, nota in zip(lista_x, ruido_blanco):
    sec_por_nota[nota].append(np.array(secuencia))

autocorr_X = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0
}
for nota, secu in sec_por_nota.items():

    secu = np.asarray(secu)
    autocorr_X[nota] = np.correlate(secu.flatten(), secu.flatten(), mode='full')



# %% APARTADO G

y = np.random.normal(0, 1, size=(1000,4000))

# %% APARTADO H

mean = [0, 0]
cov = np.array([[1, -0.5],[-0.5, 1]])
z = np.random.multivariate_normal(mean, cov, size = (1000, 4000))

# %% APARTADO I

print('Media Y[n]:',np.mean(y),'\nVarianza Y[n]:', np.var(y))
print('\nMedia Z[n]:',np.mean(z),'\nVarianza Z[n]:',np.var(z))

# %% APARTADO J

pintar_histograma(y.flatten(), bins=20)
pintar_histograma(z.flatten(), bins=20) 

z = (z[:,:,0]+z[:,:,1])/2
pintar_histograma_conjunto(y.flatten(),y.flatten(), bins=20)
pintar_histograma_conjunto(z.flatten(),z.flatten(), bins=20)

# %% APARTADO K

correla_y = np.correlate(y.flatten(),y.flatten())
correla_z = np.correlate(z.flatten(),z.flatten())

# %% APARTADO L

h = np.array([1, -0.5])

W = np.zeros_like(y)

for i in range(1000):
    W[i, :] = np.convolve(y[i, :], h, mode='same')

print('Media W[n]', round(np.mean(W),4), 'Media Z[n]',round(np.mean(z),4))
print('Var W[n]', round(np.var(W),4), 'Var Z[n]',round(np.var(z),4))

# %% APARTADO M
# import math

d = []

for i in frecuencias_f:
    d.append(np.floor(8000/i))
d = np.asarray(d)

y_2 = []

for pos,e in enumerate(y):
    y_1 = np.zeros(4000)
    y_1[:int(d[pos])+4] = e[:int(d[pos])+4]
    y_2.append(y_1)

y_2 = np.asarray(y_2)
U = np.zeros_like(y)

for i in range(1000):
    for n in range(4000):
        U[i,n] = y_2[i,n] + 1/2 * (U[i, n - int(d[i]) + 1] + U[i, n - int(d[i]) + 2])


# %% APARTADO N
a = sintetizador_secuencia(U,fs)
secuencia_sonido = a.flatten()
almacenar_audio('audioP.wav',secuencia_sonido,fs)
reproducir_secuencia(secuencia_sonido, fs)
# %% APARTADO O


notas = {
    1:[],
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[]
}

for sec, nota in zip(U,ruido_blanco):
    notas[nota].append(sec[:800])

for nota, valores in notas.items():
    valores = np.asarray(valores)
    print('Nota es',nota,'media',np.mean(valores))
    print('Autocorrelación',np.correlate(valores.flatten(), valores.flatten(), mode='full'))
