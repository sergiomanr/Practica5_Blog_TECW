import sys
import numpy as np
import matplotlib.pyplot as plt
import csv
# Definimos rango de valores donde evaluar la sucesión
N = 100
index_set = range(N+1)
x = np.zeros(len(index_set))

# Valor de parámetro
a = 1.0

# Condición inicial
x[0] = 0.5
# Iteraciones
for n in range(1, N+1):
    x[n] = a*x[n-1]*(1-x[n-1])
    # print (n, x[n]) # Imprimimos cada nuevo valor
    
# Dibujamos la sucesión resultante    
plt.plot(index_set,x,'r-',linewidth=2)
plt.xlabel('n')
plt.legend('x(n)')
# plt.show()


def cambiar(fecha):
    fech = fecha.split('/')
    a = fech[0]
    b = fech[1]
    a,b = b,a 
    final= [a,b,fech[2]]
    return '/'.join(final)


with open('cosas.csv','r', encoding='utf8') as f:
    datos = csv.reader(f)
    
    for i in datos:
        print(cambiar(i[0]),',',' '.join(i[1:]))
