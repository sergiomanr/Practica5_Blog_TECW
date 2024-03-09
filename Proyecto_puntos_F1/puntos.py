import random
import csv
pilotos = {
    'Ver' : 'RB',
    'Per' : 'RB',
    'Sai' : 'Fer',
    'Lec' : 'Fer',
    'Ham' : 'Mer',
    'Rus' : 'Mer',
    'Lan' : 'Mcl',
    'Pia' : 'Mcl',
    'Ric' : 'Aph',
    'Tsu' : 'Aph',
    'Alo' : 'Ast',
    'Str' : 'Ast',
    'Hul' : 'Has',
    'Mag' : 'Has',
    'Alb' : 'Wil',
    'Sar' : 'Wil',
    'Oco' : 'Alp',
    'Gas' : 'Alp',
    'Vot' : 'Rom',
    'Gua' : 'Rom'
}

puntos = {
    1 : 26,
    2 : 18,
    3 : 15,
    4 : 12,
    5 : 10,
    6 : 8,
    7 : 6,
    8 : 4,
    9 : 2,
    10 : 1
}
resultados = []
for i in range(100000):
    puntos_camp = {
        'Ver' : 0,
        'Per' : 0,
        'Sai' : 0,
        'Lec' : 0,
        'Ham' : 0,
        'Rus' : 0,
        'Lan' : 0,
        'Pia' : 0,
        'Ric' : 0,
        'Tsu' : 0,
        'Alo' : 0,
        'Str' : 0,
        'Hul' : 0,
        'Mag' : 0,
        'Alb' : 0,
        'Sar' : 0,
        'Oco' : 0,
        'Gas' : 0,
        'Vot' : 0,
        'Gua' : 0
    }
    
    for carrera in range(26):
        puntos_camp['Ver'] += 26
        lista_pilotos = ['Per','Sai','Lec','Ham','Rus','Lan','Pia','Ric','Tsu',
                    'Alo','Str','Hul','Mag','Alb','Sar','Oco','Gas','Vot','Gua']
        
        for i in range(2,11):
            pilo = random.choice(lista_pilotos)
            lista_pilotos.pop(lista_pilotos.index(pilo))
            puntos_camp[pilo] += puntos[i]
    
    sorted_pilotos = sorted(puntos_camp.items(), key=lambda x:x[1], reverse=True)
    resultados.append([sorted_pilotos[0][1]-sorted_pilotos[1][1],sorted_pilotos])
resultados_sorted = sorted(resultados, key=lambda x: x[0], reverse=True)
with open('Proyecto_puntos_F1/resultados.csv', encoding='utf8',mode='w') as f:
        csv_written = csv.writer(f,delimiter=',')
        for e in resultados_sorted[:30]:
            csv_written.writerow(e)