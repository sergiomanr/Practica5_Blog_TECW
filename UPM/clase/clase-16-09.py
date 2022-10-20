# temperaturas = [40.6,42.5,39.4,35.7]
# temperaturas.append(56.4)    
# print(type(temperaturas))
# print(temperaturas.pop(2))   
# decenas = [10,20,30,40,50,60,70,80,90,100]
# print(decenas[1::2]) #el primer número indica en que elemnto empieza y el segundo indica el tamaño del step
# print(decenas[6::-1])
# print(len(decenas))
# decenas[0:2] = [35,43]
# # print(decenas)
# lista_de_listas = [
# [1,2,3],
# [4,5,6],
# [7,8,9],
# [10,11,12,13,14,15]
# ]
# print(len(lista_de_listas[-1]))
# animal = ('gato',)
# print(type(animal[0]))
# mascotas = ('gato','perro','caracol')
# lista = list(mascotas)
# lista.sort()
# print(lista)
# mascotas = tuple(lista)
# print(mascotas)

# # print(mascotas*3)
# objeto = ['cama','sillon','silla']
# tupla = tuple(objeto)
# print(type(objeto))

# for mascota in tupla:
#     print(mascota, f'Se llama {mascota.title()}')

# while True:
#     if number <5:
#         for number in range(10):
# #             print(x**2)

# medidas = [
#     [1.85, 70],
#     [1.59, 80],
#     [1.79, 120]

# ]
# for persona in medidas:
#     print(persona)
#     imc = persona[1]/persona[0]**2
#     print(imc)
#     print('-' * 10 +' \n')
# for i in range(100):
#     print(i, i**2)



# numeros = range(10)
# exponentes = range(6)
# for i in numeros:
#     mensaje = ''
#     for exp in exponentes:
#         mensaje = mensaje + ' ' str(i**exp) # que pasa
#     print(mensaje)

# for i in numeros:
#     mensaje = ''
#     print(I)
#     for exp in exponentes:
#         mensaje = mensaje + str(i**exp)
#     print(mensaje)


# fahre = [-40,60,90,110]
# celsius = [round((f-32)*(5/9), 3) for f in fahre[:2]] #el 3 despues de la coma indica los decimales a los que va a redondear """Hacemos que solo coja los  primeros 3 valores"""
# print(celsius)
# otro_fahre = fahre[:]
# otro_fahre[0] = -21
# print(fahre)
# print(otro_fahre)

#ejercicio para casa
'''
definir matriz de 2 dimensiones de 10*10 (por ejemplo) y hacer el sumatorio de todos los numeros sin usar el sum

'''
from tkinter import Variable
from webbrowser import get



# for numeros in matriz:
#     fila_1ª = numeros[0]
#     fila_2 = numeros[1]
#     fila_3 = numeros[2]
#     suma = fila_1a + fila_2 + fila_3
#     suma_def = suma + suma
#     print(suma_def)
# for numeros in matriz:
#     # for elemento in numeros:
#     uni = matriz[0][0]
#     print(uni)




# filas = len(matriz) 
# columnas = len(matriz[0])


################################
for i in 
matriz = [
    [1,5,9,7,2],
    [6,4,7,3],
    [2,8,9,7]
]
suma = []
x = 0
for fila in matriz:             #sacamos lo que hay en la lista que es otra y lo llamamos fila
    for elemento in fila:       #elemento son los numeros dentro de la lista dimension2
        suma.append(elemento)   #metemos a los elemntos en una lista aparte para que sea de dimension uno
for i in range(len(suma)):      #vamos a aplicar sobre i la operacion cuantos elementos tenga la lista
     x = x + suma[i]            # Al valer x 0 sumamos de la lista 'suma' el elemento denotado por el range que va consecutivamente desde 0 hasta el max
print(x)                        #i toma el valor entre 0 y el numero de variables y se lo indica a la lista suma para que sepa que meter
print(x/len(suma))

'''
matriz = [
    [[1,2,3],[5,7,6]],
    [[1,3,4],[4,6],7],
    [[8,5,9],[2,4]],
    [3]
]
suma = []
x = 0
for fila in matriz:
    if type(fila) == list:        
        for mini_lista in fila:
            if type(mini_lista) == list:
                for elemento in mini_lista: #cuantas más dimensiones mas for in añadimos
                    suma.append(elemento)
            else:
                suma.append(mini_lista)  
    else:
        suma.append(fila) 
for i in range(len(suma)):     
     x = x + suma[i]            
print(x)   
'''