import csv
def get_partidos(fichero):
    dict_paises = {}
    with open(fichero, mode='r', encoding='utf8') as f:
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

    for pais, result in dict_paises.items():
        print(pais,'->',result)
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
    return probVictoria

class Partido:
    def __init__(self,fecha:str,local:str = None,visitante:str = None)->None:
        self.fecha = fecha
        self.local = local
        self.visitante = visitante
        self.eventos: list[str] = []

    def registra_evento(self, minuto: int, descripción: str)->None:
        msg = f'{str(minuto)}: {descripción}'
        self.eventos.append(msg)
    def imprime_ultimos_eventos(self,numero: int = 3)->str:
        if len(self.eventos) < numero:
            print('No hay suficientes eventos')
        else:
            for i in self.eventos[-numero:]:
                print(i)

if __name__ =='__main__':
    parts = Partido('12/02/23','España','Mundo')
    parts.registra_evento('32','gol del delantero ')
    parts.registra_evento('35','entrenado se regatea a defensa')
    parts.registra_evento('45','defensa expulsado')
    parts.registra_evento('67','amarilla al arbitro')
    parts.registra_evento('92','suplente falla penalti')
    print(parts.eventos)
    parts.imprime_ultimos_eventos(4)