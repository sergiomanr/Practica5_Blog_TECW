import csv
dict_paises:dict[str,dict[str,list[str]]] = {}
def get_partidos(fichero):
    
    with open(file=fichero, mode='r', encoding='utf8') as f:
            csv_dictreader = csv.DictReader(f)
            for i in csv_dictreader:
                if i['Local'] not in dict_paises.keys():
                    dict_paises[i['Local']]={}
                if i['Visitante'] not in dict_paises.keys():
                    dict_paises[i['Visitante']]={}
                if i['Visitante'] not in dict_paises[i['Local']]:
                    dict_paises[i['Local']][i['Visitante']] = []
                if i['Local'] not in dict_paises[i['Visitante']]:    
                    dict_paises[i['Visitante']][i['Local']] = []
                dict_paises[i['Local']][i['Visitante']].append(i['Resultado'])
                dict_paises[i['Visitante']][i['Local']].append(i['Resultado'][::-1])
            print(dict_paises)

def probalbilidad_victoria(diccionario,seleccion,contrincante):
    diccionario=dict_paises
    gmc=0
    grc=0
    gmt=0
    grt=0
    for clave,valor in diccionario.items():   
        if seleccion == clave: 
            if contrincante not in diccionario[clave] or valor[contrincante]==['0-0']*len(valor[contrincante]):
                grc=0
            elif contrincante in diccionario[clave]:
                resultados_entresi=valor[contrincante]
                for e in resultados_entresi:
                    gmc+=int(e[0])
                    grc+=int(e[2])
        elif seleccion not in diccionario.keys():
            probVictoria=-1.0   
        
        if clave==seleccion:
            for val in valor.values():
                for e in val:
                    gmt+=int(e[0])
                    grt+=int(e[2])
    probVictoria = ((gmt-grt)/(gmt+grt))*0.2 + ((gmc-grc)/(gmc+grc))*0.3 + 0.5
    print(probVictoria)
    

if __name__ =='__main__':
    get_partidos('resultados.csv')  
    probalbilidad_victoria('resultados.csv','Espana','Italia')   


