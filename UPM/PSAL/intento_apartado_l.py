#  %%
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


class distribucion_pregunta_examen(stats.rv_continuous):
    def _pdf(self, x, **kwargs):
        return 1/(1/(m+1)-1/(m+2))*(x**m)*(1-x)
    
np.random.seed(2023)
experimentos = 10000
m_list = [1, 2, 3]
muestras_X_por_m = []
Bs = []
for i in m_list:
    Bs.append(round(1/(1/(i+1)-1/(i+2))))

for m, B in zip(m_list, Bs):
    distribucion_X = distribucion_pregunta_examen(a=0, b=1)
    muestras_X_por_m.append(distribucion_X.rvs(size=experimentos))

# %%
# Intento de hacer que resuleva una ecuación en vez de el loop pero abandonamos porque tarda demasiado.
from sympy import symbols, solve
for ms,bs in zip(m_list,Bs):
    x = symbols('x')
    print('entra')
    ecuacion = -0.9 + (bs**9*(1/bs-(x**(ms+1)/ms+1)+(x**(ms+2)/ms+2))**9*bs*((x**(ms+1)/ms+1)-(x**(ms+2)/ms+2)))*10 + (bs*(1/bs-(x**(ms+1)/ms+1)+(x**(ms+2)/ms+2)))
    print(solve(ecuacion))
# %% Funcion de b
k = 5

# Algoritmo terminado
# frecuencia < 0.9
import time 
start = time.time()
for muestra_de_m,m_selec in zip(muestras_X_por_m,m_list):
    b = 0.99
    frecuencia = 0
    while True:
        listas_notas = []
        for examenes in np.array_split(muestra_de_m, len(muestra_de_m)/10):
            listas_notas.append(sum(examenes >= b))
        # listaz_notas = [sum(examenes>= b) for examenes in np.array_split(muestra_de_m, len(muestra_de_m)/10) ]
        # contador = 0
        # for nota in listas_notas:
        #     if nota >= k:
        #         contador += 1

        contador = np.sum(np.asarray(listas_notas)>=k)
        frecuencia = contador/(len(muestra_de_m)/10)
        
        if frecuencia >= 0.9:
                print(f'La b para que la Fr de {m_selec} sea {frecuencia} ~ 0.9 es: ',round(b,4))
                break
        else:
            # b -= (0.9-frecuencia)/15
            b -= 0.005
            continue
print('Tiempo', time.time()-start)
# %%
b_l = 0.35
muestras_Y_por_m_bis = []
muestras_Y_por_grupo_por_m_bis = []
for Y_por_m_L in muestras_X_por_m:      #tiene que ser la x luego se cambia 
    lista_notas_m = []
    divison_10 = np.array_split(Y_por_m_L, len(Y_por_m_L)/10)

    for examen_indiv in divison_10:
        lista_notas_m.append(sum(examen_indiv>=b_l))
    else:
        muestras_Y_por_grupo_por_m_bis.append(lista_notas_m)



for conjunto_y_para_m in muestras_Y_por_grupo_por_m_bis:
    contador_nota = 0
    for nota in conjunto_y_para_m:
        if nota >= k:
            contador_nota += 1
    print(f'La frecuencia relativa de que el estudiante tenga {k} o más puntos es :', contador_nota/1000)
# %%
