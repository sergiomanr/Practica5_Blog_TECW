# x = [1,4,3,8,6,18,225]
# y = [2,4,6,3,1,5,9,7,225,8]
# contador = 0
# for i in x:
#     if i not in y:
#         contador+= 1
# print(contador)
# for i in x:
#     no_reoe = []
#     if i not in y:
#         no_reoe.append(i)
# # print(len(no_reoe))


# x_set = set(x)
# y_set = set(y)
# diff_set = set[int] = x_set.difference(y_set)
# print(len(diff_set))

# palabras = []
# while True:
#     respuseta = input("Pon una palabra:")
    
#     if respuseta not in palabras:
#         palabras.append(respuseta)
#     elif respuseta in palabras:
#         palabras.append(respuseta)
#         break
# for i in palabras:
#     print(i)


# def estiamar(tareas,jornada=8):
#     total = sum(tareas.values())
#     return total/jornada

# def estimar(tareas,jornada =8):
#     horas_totales = []
#     for num_tarea,horas in tareas.items():
#         x = tareas[num_tarea]
#         horas_totales.append(x)
#     print(horas_totales)
#     jornadas = sum(horas_totales)/jornada
#     return jornadas
tareas = {
    'comer': 10,
    'cantar': 9,
    'morir':23
}
# print(estimar(direc))


actual = [(1,15),(2,16),(3,19),(4,17),(5,11),(6,19,),(7,22)]
historico = [(1,11),(3,14),(3,29),(4,14),(5,9),(6,10,),(7,12)]
print(actual[0][1])

###########################################################

def calcular(actuals,historicos):
    actual_lista = []
    for i in actuals:
        x = list(i)
        actual_lista.append(x)
    historico_lista = []
    for i in historicos:
        x = list(i)
        historico_lista.append(x)

    if len(actual_lista) > len(historico_lista):
        print("La longitud de las listas son dif")
        return -1

    for i in range(len(actual_lista)):
        if actual_lista[-(i+1)][0] != actual_lista[-(i+1)][0]:
            return -2

    for i in range(len(actual_lista)):
        dias = []
        if actual_lista[-(i+1)][1] > actual_lista[-(i+1)][1]:
            dias.append(actual_lista[-(i+1)][1])
        if len(dias) >= 3:
            print(len(dias))
        else:
            dias = []
    return actual_lista[0][1]

print(calcular(actual,historico))

###########################################################

def calcula_duracion_ola_de_calor(actual: list[tuple[str,float]],historico: list[tuple[str,float]])->int:
    if len(actual) > len(historico):
        print("longitud de listas es diff")
        return -1
    contador = 0
    for i in range(len(actual)):
        pos = -(i+1)
        tupla_actual: tuple[str,float] = actual[pos]
        tupla_histo: tuple[str,float] = historico[pos]
        if tupla_actual[0] != tupla_histo[0]:
            print("no cuadran")
            return -2
        elif tupla_actual[1] > tupla_histo[1]:
            contador += 1
        else:
            break
    if contador < 3:
        return -3
    else:
        return contador
##########################################################

