# -*- coding: utf-8 -*-
"""
PSAL - PRÁCTICA 1

"""

# %% APARTADO A

import random

numero_envios_individuales = 100000
solicitudes_individuales = []
proveedores_individuales = []
solicitudes_por_cliente = []
proveedores_por_cliente = []


for _ in range(0, numero_envios_individuales):
    for i in range(3):

        variable_auxiliar = random.random()
        solicitudes_individuales.append(random.randint(2, 4))

        # if solicitudes_individuales[-1] == 1: 
        #     if variable_auxiliar <= 2/3:
        #         proveedores_individuales.append(1)
        #     else:
        #         proveedores_individuales.append(2)

        if solicitudes_individuales[-1] == 2: 
            if variable_auxiliar <= 2/3:
                proveedores_individuales.append(2)
            else:
                proveedores_individuales.append(3)

        if solicitudes_individuales[-1] == 3: 
            proveedores_individuales.append(3)

        if solicitudes_individuales[-1] == 4:
            if variable_auxiliar <= 2/3:
                proveedores_individuales.append(2)
            else:
                proveedores_individuales.append(3)
        

    solicitudes_por_cliente.append(solicitudes_individuales)
    proveedores_por_cliente.append(proveedores_individuales)
    solicitudes_individuales = []
    proveedores_individuales = []


# %% APARTADO B

envios_individuales = []
envios_por_cliente = []
proveedores_indi = []
provee_por_cliente = []

for solicitud_por_cliente, proveedor_por_cliente in zip(solicitudes_por_cliente, proveedores_por_cliente):
    for solicitud, proveedor in zip(solicitud_por_cliente, proveedor_por_cliente):
        variable_auxiliar = random.random()
        lista = [2,3,4]
        if variable_auxiliar > 9/10:
            lista.remove(solicitud)
            nuevo = random.choice(lista)
            if variable_auxiliar > 19/20:
                envios_individuales.append(0)
                proveedores_indi.append(0)
            else:
                variable_auxiliar = random.random()
                envios_individuales.append(nuevo)
                if nuevo == 1:
                    if variable_auxiliar > 2/3:
                        proveedores_indi.append(2)
                    else:
                        proveedores_indi.append(1)
                if nuevo == 2:
                    if variable_auxiliar > 2/3:
                        proveedores_indi.append(3)
                    else:
                        proveedores_indi.append(2)
                if nuevo == 3:
                    proveedores_indi.append(3)
                if nuevo == 4:
                    if variable_auxiliar > 2/3:
                        proveedores_indi.append(3)
                    else:
                        proveedores_indi.append(2)
        else:
            envios_individuales.append(solicitud)
            proveedores_indi.append(proveedor)
        

    envios_por_cliente.append(envios_individuales)
    envios_individuales = []
    provee_por_cliente.append(proveedores_indi)
    proveedores_indi = []

# %% APARTADO C

producto_1 = 0
producto_2 = 0
producto_3 = 0
producto_4 = 0
no_producto = 0

for envio_cliente in envios_por_cliente:
    for envio in envio_cliente:
        if envio == 1:
            producto_1 += 1
        elif envio == 2:
            producto_2 +=1
        elif envio == 3:
            producto_3 +=1
        elif envio == 4:
            producto_4 +=1
        elif envio == 0:
            no_producto +=1
        

suma_productos = producto_1 + producto_2 + producto_3 + producto_4 + no_producto

print("Producto 1: ", producto_1/suma_productos)
print('Producto 2: ', producto_2/suma_productos)
print('Producto 3: ', producto_3/suma_productos)
print('Producto 0: ', no_producto/suma_productos)
print('Suma total:', suma_productos)




# %% APARTADO D

proveedor_1 = 0
proveedor_2 = 0
proveedor_3 = 0
proveedor_0 = 0
for proveedor_cliente in provee_por_cliente:
    for proveedor in proveedor_cliente:
        if proveedor == 1:
            proveedor_1 += 1
        elif proveedor == 2:
            proveedor_2 += 1
        elif proveedor == 3:
            proveedor_3 += 1
        elif proveedor == 0:
            proveedor_0 +=1

suma_proveedores = proveedor_1 + producto_2 + proveedor_3 +proveedor_0

print("Proveedor 1: " + str(proveedor_1/suma_proveedores))
print("Proveedor 2: " + str(proveedor_2/suma_proveedores))
print("Proveedor 3: " + str(proveedor_3/suma_proveedores))
print("Proveedor 0: " + str(proveedor_0/suma_proveedores))

# %% APARTADO E

producto_1_proveedor_1 = 0
producto_1_proveedor_2 = 0
producto_2_proveedor_2 = 0
producto_4_proveedor_2 = 0
producto_2_proveedor_3 = 0
producto_3_proveedor_3 = 0
producto_4_proveedor_3 = 0

for envio_cliente, proveedor_cliente in zip(envios_por_cliente, provee_por_cliente):
    for envio, proveedor in zip(envio_cliente, proveedor_cliente):
        if envio == 1 and proveedor == 1:
            producto_1_proveedor_1 += 1
        elif envio == 1 and proveedor == 2:
            producto_1_proveedor_2 += 1
        elif envio == 2 and proveedor == 2:
            producto_2_proveedor_2 += 1
        elif envio == 2 and proveedor == 3:
            producto_2_proveedor_3 += 1
        elif envio == 3 and proveedor == 3:
            producto_3_proveedor_3 += 1
        elif envio == 4 and proveedor == 3:
            producto_4_proveedor_3 += 1
        elif envio == 4 and proveedor == 2:
            producto_4_proveedor_2 += 1
suma_productos_proveedores = producto_1_proveedor_1+ producto_1_proveedor_2+producto_2_proveedor_2+producto_2_proveedor_3+producto_3_proveedor_3+producto_4_proveedor_3

print("Producto 1 Proveedor 1: " + str(producto_1_proveedor_1/suma_productos_proveedores))
print("Producto 1 Proveedor 2: " + str(producto_1_proveedor_2/suma_productos_proveedores))
print("Producto 2 Proveedor 2: " + str(producto_2_proveedor_2/suma_productos_proveedores))
print("Producto 2 Proveedor 3: " + str(producto_2_proveedor_3/suma_productos_proveedores))
print("Producto 3 Proveedor 3: " + str(producto_3_proveedor_3/suma_productos_proveedores))
print("Producto 4 Proveedor 3: " + str(producto_4_proveedor_3/suma_productos_proveedores))
print("Producto 4 Proveedor 2: " + str(producto_4_proveedor_2/suma_productos_proveedores))


# %% APARTADO F

def frecuencias(por_cliente,apartado: str ):
    frecuencia = 0
    for i in por_cliente:
        if 1 in i and 2 in i and 3 in i:
            frecuencia +=1
    return f"Frecuencia 1, 2, 3 de {apartado}: " + str(frecuencia/len(por_cliente))

'''frecuencia_1_2_3 = 0

for solicitud_cliente in solicitudes_por_cliente:
    if 1 in solicitud_cliente and 2 in solicitud_cliente and 3 in solicitud_cliente:
        frecuencia_1_2_3 += 1
print("Frecuencia 1, 2, 3: " + str(frecuencia_1_2_3/len(solicitudes_por_cliente)))
'''

print(frecuencias(solicitudes_por_cliente,'solicitados' ))

# %% APARTADO G 

frecuencia_1_2_3_envios = 0

for envio_por_cliente in envios_por_cliente:
    if 1 in envio_por_cliente and 2 in envio_por_cliente and 3 in envio_por_cliente:    
        frecuencia_1_2_3_envios += 1


print("Frecuencia 1, 2, 3 envios: " + str(frecuencia_1_2_3_envios/len(envios_por_cliente)))

# print(frecuencias(envios_por_cliente, 'envios'))


# %% APARTADO H

'''frecuencia_1_2_3_proveedores = 0

for proveedor_por_cliente in proveedores_por_cliente:
    if 1 in proveedor_por_cliente and 2 in proveedor_por_cliente and 3 in proveedor_por_cliente:
        frecuencia_1_2_3_proveedores +=1


print("Frecuencia 1, 2, 3 proveedores: " + str(frecuencia_1_2_3_proveedores/len(proveedores_por_cliente)))'''

print(frecuencias(provee_por_cliente,'proveedores'))

# %% APARTADO I

frecuencia_1_1_1 = 0

for i in envios_por_cliente:
    if  i[0] in [0,1] and i[1] in [0,1] and i[2] in [0,1] and i != [0,0,0]:
        frecuencia_1_1_1 += 1

print("Frecuencia 1, 1, 1: " + str(frecuencia_1_1_1/len(envios_por_cliente)))
frecuencia_2_2_3 = 0
for i in envios_por_cliente:
    if  i == [2,2,3]:
        frecuencia_2_2_3 += 1

print('Frecuencia 2,2,3', (frecuencia_2_2_3*3)/len(envios_por_cliente))

# %% APARTADO J

frecuencia_solo_1_proveedor = 0

for i in provee_por_cliente: 
    if i[0] in [0,1] and i[1] in [0,1] and i[2] in [0,1] and i != [0,0,0]:
        frecuencia_solo_1_proveedor +=1
    # if i == [1,1,1]:
    #     frecuencia_solo_1_proveedor +=1 


print("Frecuencia solo 1 proveedor: " + str(frecuencia_solo_1_proveedor/len(provee_por_cliente)))


#  %% APARTADO K

frecuencia_1_2_3_atleast_one_is_proveedor_1 = 0
contador_1_2_3_con_A = 0
for envio_cliente, proveedor_cliente in zip(envios_por_cliente,provee_por_cliente):
    if 1 in envio_cliente and 2 in envio_cliente and 3 in envio_cliente:
        frecuencia_1_2_3_atleast_one_is_proveedor_1 += 1
        if 1 in proveedor_cliente:
            contador_1_2_3_con_A +=1

print("Frecuencia 1, 2, 3 al menos 1 es del proveedor 1: ",contador_1_2_3_con_A/frecuencia_1_2_3_atleast_one_is_proveedor_1)

# %%
import collections

suma=0
for envio, solicitu in zip(envios_por_cliente,solicitudes_por_cliente):
    if collections.Counter(envio)==collections.Counter(solicitu):
        suma +=1
print('Que llege lo que pidas con cambios',str(suma/numero_envios_individuales))

suma_sin=0
for envio, solicitu in zip(envios_por_cliente,solicitudes_por_cliente):
    if envio == solicitu:
        suma_sin +=1
print('Que llege sin cambio alguno', suma_sin/numero_envios_individuales)
# si se elimina producto se elimina proveedor y si cambia el envio cambia también el proveedor

# %%
