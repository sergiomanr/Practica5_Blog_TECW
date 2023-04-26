import csv

def get_partidos(fichero):
    dict_paises:dict[str,dict[str,list[str]]] = {}
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
    return dict_paises

def probalbilidad_victoria(diccionario,seleccion,contrincante):
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
    print('gmc',gmc,'\tgrc',grc,'\tgmt',gmt,'\tgrt',grt)
    probVictoria = ((gmt-grt)/(gmt+grt))*0.2 + ((gmc-grc)/(gmc+grc))*0.3 + 0.5
    print(probVictoria)
    

class Partido:
    def __init__(self,fecha:str,local:str=None,visitante:str=None):
        self.fecha=fecha
        self.local=local
        self.visitante=visitante
        self.eventos:list=[]

    def registra_evento(self,minuto:int,mensaje:str):
        self.eventos.append(str(str(minuto)+':'+mensaje))
    
    def imprime_ultimos_eventos(self,n=3):
        if n > len(self.eventos):
            print('No hay suficientes eventos')
        else:
            for evento in self.eventos[:n-1]:
                print(evento)


if __name__ =='__main__':
      
    probalbilidad_victoria(get_partidos('local_visitante_resultado.csv'),'España','Italia')   
    s=Partido('14/4','Atleti','Madrid')
    s.registra_evento(minuto=8,mensaje='gol')
    s.registra_evento(minuto=38,mensaje='fuera de juego')
    s.registra_evento(minuto=89,mensaje='roja')
    s.registra_evento(minuto=58,mensaje='corner')
    s.registra_evento(minuto=78,mensaje='gol')
    s.registra_evento(minuto=18,mensaje='amarilla')
    s.registra_evento(minuto=83,mensaje='gol')
    s.registra_evento(minuto=82,mensaje='penalti')
    # s.imprime_ultimos_eventos(3)

