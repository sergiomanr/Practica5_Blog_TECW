from enum import Enum
import time
class ModoClimatizador(Enum):
    FAN = 1
    HEAT=2
    COOL=3
class Climatizador:
    def __init__(self, encendido:bool = False, temperatura: int= 20, modo: ModoClimatizador= ModoClimatizador.FAN) -> None:
        self.encendido = encendido
        self.temperatura = temperatura
        self.modo = modo
    def comando(self, modo: ModoClimatizador= None, temperatura: int= None)-> None:
        if modo != None:
            self.modo = modo
        if temperatura != None:
            self.temperatura = temperatura
class Termostato:
    def __init__(self, climatizador: Climatizador, temp_min: float = 16, temp_max:float=30 ):
        self.climatizador = climatizador
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.historico: dict[float, float]= {}
    def actualiza(self, temp_actual: float)->None:
        self.historico[time.time()]=temp_actual
        if temp_actual < self.temp_min:
            self.climatizador.comando(modo=ModoClimatizador.HEAT)
            self.climatizador.encendido = True
            self.climatizador.comando(temperatura=self.temp_min +2)
        elif temp_actual> self.temp_max :
            self.climatizador.comando(modo=ModoClimatizador.COOL, temperatura=self.temp_max-2)
            self.climatizador.encendido= True
        else:
            self.climatizador.encendido= False
    def fecha_temp_max(self)->float:
        if len(self.historico) == 0:
            return None
        temp_max= max(self.historico.values())
        for fecha, temp in self.historico.items():
            if temp == temp_max:
                return fecha
        else:
            return None
    def media_historica(self, inicio:float=None, fin:float=None)->float:
        if len(self.historico) == 0:
            return None
        temps= []
        if (inicio or fin ) == None:
            temps = self.historico.values()
        else:
            for fecha,temp in self.historico.items():
                if fecha < fin and fecha > inicio:
                    temp.append(temp)
        return sum(temps)/len(temps)

if __name__ == '__main__':
    c1: Climatizador = Climatizador()
    c1.comando(modo=ModoClimatizador.HEAT)
    c1.comando(temperatura=12)
    c1.comando(modo=ModoClimatizador.COOL, temperatura=34)
    t1: Termostato = Termostato(c1, temp_min=20, temp_max=36)
    t1.actualiza(23.5)
    t1.actualiza(24.5)
    print('fecha max:', t1.fecha_temp_max())
    print('Media:', t1.media_historica())
    t1.historico[1:]
