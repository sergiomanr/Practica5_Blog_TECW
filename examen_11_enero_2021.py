import json
import csv
from typing import Any

class SensorTemperatura:
	def __init__(self, identificador:int, ciudad:str ='Desconocida')->None:
		self.identificador = identificador
		self.ciudad = ciudad
		self.historial: dict[str,float] = {}
	def registra_temperatura(self,fecha:str,temperatura:float)->None:
		self.historial[fecha]=temperatura
	def guarda_datos(self, nombre:str)->None:
		with open(nombre, mode='w', encoding='utf8') as f:
			dicciona_json: dict[str,Any] ={
			'identificador': self.identificador,
			'ciudad': self.ciudad,
			'historial': self.historial}
			json.dump(dicciona_json,f) 
	def get_día_mas_frio(self)->tuple():
		if len(self.historial)==0:
			return None
		min_temp = min(self.historial.values())
		for clave,valor in self.historial.items():
			if valor == min_temp:
				fecha_temp=[clave,valor]
				return tuple(fecha_temp)

def carga_sensor(nombre:str)->SensorTemperatura:
    with open(nombre, mode='r', encoding='utf8') as f:
        diccionario_json = json.load(f)
        sen: SensorTemperatura = SensorTemperatura(identificador = diccionario_json['identificador'], ciudad = diccionario_json['ciudad'])
        for fecha, temp in diccionario_json['historial'].items():
            sen.registra_temperatura(fecha,temp)
        return sen

class Vehículo:
    def __init__(self, matricula, modelo, color, propietario):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.propietario = propietario

def carga_vehiculos(nombre: str)->list[Vehículo]:
    lista: list[Vehículo]= []
    with open(nombre, mode= 'r',encoding='utf8') as f:
        csv_dictReader = csv.DictReader(f)
        for i in csv_dictReader:
            lista.append(Vehículo(matricula=i['Matrícula'],modelo=i['Modelo'],color=i['Color'], propietario=i['Propietario']))
    return lista

def comprueba_matriculas_duplicadas(lista_vehiculos: list[Vehículo])->str:
    dict_matricus: dict[str, list[Vehículo]] = {}
    for i in lista_vehiculos:
        lista_clon = lista_vehiculos[:]
        lista_vehicu_repe= []
        lista_clon.remove(i)
        for e in lista_clon:
            if e.matricula == i.matricula:
                lista_vehicu_repe.append(e)
        dict_matricus[i.matricula]=lista_vehicu_repe
        lista_vehicu_repe.append(i)
    for matricula, lista_matri in dict_matricus.items():
            if len(lista_matri) > 1:
                print('Matrícula',matricula,'encontrada',len(lista_matri),'veces:')
                for i in lista_matri:
                    print(i.matricula,'-',i.modelo,'-',i.color,'-',i.propietario)
                else:
                    print('-'*10)

if __name__ == '__main__':
    s1 = SensorTemperatura(12356,'Madrid')
    s1.registra_temperatura('12/2/2003',4.1)
    s1.registra_temperatura('1/2/2003',27.1)
    s1.registra_temperatura('12/2/2013',-51.1)
    s1.registra_temperatura('2/8/2003',43)
    s1.registra_temperatura('12/01/2003',16.5)
    # print(s1.historial)
    # print(s1.get_día_mas_frio())
    s1.guarda_datos('sensores.json')
    # print(carga_sensor('sensores.json').historial)
    asca = carga_vehiculos('matriculas.csv')
    comprueba_matriculas_duplicadas(asca)