import time
from math import radians, sin, cos, asin, sqrt
import unittest
import csv
import logging

RADIO_TIERRA: float = 6378.0 #km
# Ejercicio 1: 1 punto
def distancia_haversine(pos1: tuple[float,float], pos2: tuple[float, float]) -> float:
    lat1 = pos1[0]
    long1 = pos1[1]
    lat2 = pos2[0]
    long2 = pos2[1]
    diff_lat = radians(lat1 - lat2)
    diff_long = radians(long1 - long2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    aux = sin(diff_lat/2)**2 + cos(lat1) * cos(lat2) * sin(diff_long/2)**2
    c = 2 * asin(sqrt(aux))
    return RADIO_TIERRA * c

# Ejercicio 2 
# Ejercicio 2.1: 0.5 punto
class GPS():
    def __init__(self, identificador: str, posicion: tuple[float, float]) -> None:
        self.identificador = identificador
        self.historial: dict[float, tuple[float,float]] = {}
        self.posicion = posicion
        self.historial[time.time()] = self.posicion
        
    # Ejercicio 2.2: 0.5 puntos
    def update(self, latitud: float, longitud: float) -> None:
        self.posicion = (latitud, longitud)
        self.historial[time.time()] = (latitud, longitud)

    # Ejercicio 2.3: 2 puntos
    def distancia_recorrida_desde(self, instante_inicial: float = None) -> float:
        times: list[float] = []
        if not instante_inicial:
            times = list(self.historial.keys())
        else:
            for t in self.historial.keys():
                if t > instante_inicial:
                    times.append(t)
        if len(times) < 2:
            raise Exception("No se dispone de suficientes posiciones para calcular la distancia recorrida por el GPS " + self.identificador)
        else:
            distancia: float = 0.0
            times.sort()
            for i in range(len(times)-1):
                orig: tuple[float, float] = self.historial.get(times[i])
                dest: tuple[float, float] = self.historial.get(times[i+1])
                distancia += distancia_haversine(orig, dest)
            return distancia
                
            

#Ejercicio 3: 1 punto
class TestGPS(unittest.TestCase):
    def test_distancia(self):
        pos = (40.452529529342215, -3.7273750078542682)
        s1 = GPS('s1', pos)
        s1.update(pos[0], pos[1])
        dist = s1.distancia_recorrida_desde()
        assert dist == 0.0
    
if __name__ == '__main__':
    unittest.main()

# Ejercicio 4
# Ejercicio 4.1: 3 puntos
class Supervisor():
    def __init__(self, historial_csv: str) -> None:            
        self.sensores: dict[str, GPS] = {}       
        with open(file=historial_csv, mode='r', encoding='utf8') as file:
            reader = csv.DictReader(file)
            for line in reader:
                id = line['id']
                timestamp = float(line['timestamp'])
                lat = float(line['lat'])
                long = float(line['long'])
                pos = (lat, long)
                if id not in self.sensores.keys():
                    sensor = GPS(id, posicion=None)
                    sensor.historial.clear()
                    self.sensores[id] = sensor
                sensor.historial[timestamp] = pos
        
        for sensor in self.sensores.values():
            most_recent_timestamp: float = max(sensor.historial.keys())
            pos: tuple(float,float) = sensor.historial.get(most_recent_timestamp)
            sensor.posicion = pos
    
    # Ejercicio 4.2: 2 puntos
    def sensor_mayor_distancia_recorrida(self) -> GPS:
        max_sensor: GPS = None
        max_distancia: float = 0
        for sensor in self.sensores.values():
            try:
                distancia = sensor.distancia_recorrida_desde()
                if max_sensor is None or distancia > max_distancia:
                    max_distancia = distancia
                    max_sensor = sensor
            except:
                logging.basicConfig(level=logging.DEBUG, filename='supervisor.log')
                logger = logging.getLogger("Supervisor")
                logger.warning("No se ha podido calcular la distancia recorrida por el sensor " + sensor.identificador)
        return max_sensor
        

# Ejercicio 5: Recuperación del parcial
# Ejercicio 5.1: 2 puntos
class Vehiculo(GPS):
    def __init__(self, id: str, pos: tuple[float, float], dist_seguridad: float = 50.0) -> None:
        super().__init__(identificador=id, posicion=pos)
        self.distancia_seguridad = dist_seguridad
        self.velocidad: float = 0.0
    
    # Ejercicio 5.2: 2.5 puntos
    def update(self, latitud: float, longitud: float) -> None:
        last_pos = self.posicion
        last_time = max(self.historial.keys())
        super().update(latitud, longitud)
        current_pos = self.posicion
        current_time = max(self.historial.keys())
        distancia = distancia_haversine(last_pos, current_pos)
        tiempo = (current_time-last_time)/3600.0
        self.velocidad = distancia/tiempo #km/h
        
    # Ejercicio 5.3: 2.5 puntos
    def get_velocidad_media(self) -> float:
        t_min = min(self.historial.keys())
        t_max = max(self.historial.keys())
        dist = self.distancia_recorrida_desde()
        vel = dist / ((t_max-t_min)/3600.0)
        return vel #km/h
        
    # Ejercicio 5.4: 3 puntos
    def get_amenazas_colision(self, vehiculos: list[GPS]) -> list[GPS]:
        lista: list[GPS] = []
        for v in vehiculos:
            distancia: float = distancia_haversine(self.posicion, v.posicion) / 1000.0
            if distancia < self.distancia_seguridad:
                lista.append(v)
        return lista
    