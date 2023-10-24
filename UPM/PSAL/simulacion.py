import random

numero_envios_individuales = 10000
solicitudes_individuales = []
proveedores_individuales = []
solicitudes_por_cliente = []
proveedores_por_cliente = []


for _ in range(0, numero_envios_individuales):
    for i in range(3):

        variable_auxiliar = random.random()
        solicitudes_individuales.append(random.randint(1, 4))

        if solicitudes_individuales[-1] == 1: 
            if variable_auxiliar < 2/3:
                proveedores_individuales.append(1)
            else:
                proveedores_individuales.append(2)

        if solicitudes_individuales[-1] == 2: 
            if variable_auxiliar < 2/3:
                proveedores_individuales.append(2)
            else:
                proveedores_individuales.append(3)

        if solicitudes_individuales[-1] in [3,4]: 
            proveedores_individuales.append(3)

    solicitudes_por_cliente.append(solicitudes_individuales)
    proveedores_por_cliente.append(solicitudes_por_cliente)
    solicitudes_individuales = []
    proveedores_individuales = []