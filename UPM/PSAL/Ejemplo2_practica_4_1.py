import numpy as np
def sintetizador_secuencias(seqArmonia,seqMelodia,fs,L):
    
    # Fusionar las dos secuencias
    seq = seqMelodia
    for i in np.arange(0,len(seq),L):
        seq[i]=seqArmonia[i] 
    
    # Transforma la secuencia de frecuencias en tonos de duración fija
    T = 0.5
    N = int(np.floor(T*fs))
    
    # Crea un array de tonos NO aleatorios
    x = np.zeros((len(seqArmonia),N))
    n = np.arange(0,N)
    
    # Para cada nota, genera un tono: una fila por nota
    for i in range(0,len(seq)):
        x[i,:] = np.sin(2*np.pi*seq[i]/fs*n)
    
    # Devuelve los tonos uno detras de otro
    return x.flatten()


armonias = {
    0: "None",
    1 : "La",
    2 : "Do",
    3 : "Re",
    4 : "Fa"
    }

melodias = {
    0 : "None",
    1 : "La",
    2 : "Fa",
    3 : "Do",
    4 : "Re"
    }

notas = {
    "None" : 0,
    "Do" : 261.62,
    "Re" : 293.66,
    "Mi" : 329.62,
    "Fa" : 349.22,
    "Sol" : 391.88,
    "La" : 440.00,
    "Si" : 987.76
    }



# %% EJEMPLO 2
L = 4
K = 2

# Secuencia aleatoria de notas de armonia (NO cumple las condiciones de la práctica)
x = np.zeros(L*K).astype(int)
for i in np.arange(0,L*K,L):
    x[i] = np.random.randint(4, size=1)+1

# Secuencia aleatoria de notas de melodía (NO cumple las condiciones de la práctica)
y = np.random.randint(4, size=L*K)+1
for i in np.arange(0,L*K,L):
    y[i] = 0

# Llamada al sintetizador
z = sintetizador_secuencias(transformador_armonia(x),transformador_melodia(y),fs,L)

# Almacenamos el resultado en fichero de audio
almacenar_audio('test2.wav',z,fs)

# Reproducimos
reproducir_secuencia(z,fs)