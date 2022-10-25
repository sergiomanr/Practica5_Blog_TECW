from typing import Any
class Sensor:
    def __init__(self, id:str, tipos: dict[str, Any]):
        self.id = id
        self.tipos = tipos
        self.datos: dict[str, Any] = {}
    def update_data(self, valores: dict[str, Any])->None:
        for dato,valor in valores.items():
            if dato in self.tipos:
                self.datos[dato] = valor
    def get_all_data(self)-> dict[str, Any]:
        return self.datos.copy()
    def get_data(self, dato:str)-> Any:
        for i in self.datos:
            if i==dato:
                return self.datos[i]
        # return self.datos.get(dato,'dato desconocido')
    def print_info(self)->None:
        print('Datos del sensor:',self.id)
        for dato,valor in self.datos.items():
            print(f'->{dato}({self.tipos.get(dato)})-->{valor}')


salon = Sensor('salon123',{
    'temperatura':'numerico',
    'humedad':'porcentaje',
    'co2':'numerico',
    'localización':'texto',
    'bochorno':'porcentaje'
})
salon.update_data({
    'temperatura':23,
    'humedad':33,
    'co2':786,
    'localización':'suelo',
    'bochorno':10
})
# print(salon.get_all_data())
print(salon.get_data('temperatura'))
salon.print_info()
class Monitor:
    def __init__(self, sensores:list[Sensor], criterios: dict[str, Any]):
        self.sensores = sensores
        self.criterios = criterios
        self.alarmas: dict[str, list[str]] = {}
    def add_sensor(self, sensor:Sensor):
        self.sensores.append(sensor)
    def update_criterio(self, nombre_dato:str, criterio:str):
        self.criterios[nombre_dato]=criterio
    def check(self)->None:
        self.alarmas.clear()
        for sensor in self.sensores:
            datos:dict[str, Any] = sensor.datos
            datos_alarmantes = []
            for dato,valor in sensor.datos.items():
                match sensor.tipos.get(dato):
                    case 'numerico' | 'porcentaje':
                        if valor < self.criterios.get(dato):
                            datos_alarmantes.append(dato)
                    case 'texto' :
                        if valor == self.criterios.get(dato):
                            datos_alarmantes.append(dato)
        if len(datos_alarmantes) > 0:
            self.alarmas[sensor.id]=datos_alarmantes
    def get_sensores_alarmados(self)->list[str]:
        listas =[]
        for i in self.alarmas:
            listas.append(i)
        return listas
        # return list(self.alarmas.keys())
    def print_alarmas(self, identificador:str):
        print('Alarmas para el sensor',identificador)
        for dato,valor in self.alarmas.items():
            print('\t->',dato,'-',valor)
moni = Monitor([],{})
