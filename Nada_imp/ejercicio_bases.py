# x = [9,8,6,3,4,5,0]
# y = [3,3,8,6,0,4,2]
# lista=[]

# for i in x:
#     if i not in y:
#         lista.append(i)

# x = set(x)
# y = set(y)

# dif = x-y

# print(dif)
# # print(lista)

# tareas= {
#     '1': 10,
#     '4' : 15
# }
# def estimar(tareas, jornada=8):
#     suma = sum(tareas.values())

#     print(float(suma/jornada))

# estimar(tareas)

import csv
contador_despejado = 0
contador_nublado = 0
fecha_desp = 0
fecha_nub = 0

with open('AccidentesBicicletas_2021.csv', encoding='utf8', mode='r') as f:
    for i in csv.reader(f, delimiter=';'):
        if i[8] == 'Despejado':
            contador_despejado += 1
        elif i[8] == 'Nublado':
            contador_nublado += 1


print(contador_nublado,contador_despejado)