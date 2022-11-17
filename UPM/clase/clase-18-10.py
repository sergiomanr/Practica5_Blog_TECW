
from enum import Enum
class DiasSemana(Enum):
    LUNES = 1
    MARTES =2
    MIERCOLES =3
    JUEVES =4
    VIERNES =5
    SÁBADO =6
    DOMINGO =7
    def __init__(self,dia):
        self.dia = dia
        self.caca = 23
    def es_finde(self)->bool:
        return self.value >= 6 
        
    def es_laborable(dia)->bool:
        return dia.value <6
    def entre(dia,dia1,dia2)->bool:
        return dia1.value < dia.value < dia2.value
dia: DiasSemana = DiasSemana.MARTES
nombre_dia: str = dia.name
order_dia: int = dia.value
# print(dia)
# print(dia.caca)
# print(nombre_dia)
# print(dia.es_finde())
# print(DiasSemana.es_laborable(dia))
# print('gols')
# print(dia.entre(DiasSemana.LUNES,DiasSemana.JUEVES))
# todos_los_dias: list[str]= DiasSemana._member_names_
# map: dict[str,DiasSemana] = DiasSemana._member_map_
# # print(map)
class MesesAño(Enum):
    ENERO=1
    FEBRERO=2
    MARZO=3
    ABRIL=4
    MAYO=5
    JUNIO=6
    JULIO=7
    AGOSTO=8
    SEPTIEMBRE=9
    OCTUBRE=10
    NOVIEMBRE=11
    DICIEMBRE=12
    def __init__(self,mes):
                self.mes = mes
    def que_mes_es(self):
                return self.value 
    def cacota(self):
        x = 'Hace '
        y = ['calor','frio', 'humedad','tormentas','chuvascos']
        j = x + random.choice(y)
        return j
mes_eleg: MesesAño = MesesAño.ABRIL
import random
random.choice
print(MesesAño.SEPTIEMBRE.que_mes_es())
print(MesesAño.OCTUBRE.que_mes_es())
print(MesesAño.cacota(mes_eleg))
print(mes_eleg.value)
for i in MesesAño:
    print(i.name,':', i.value,'-->',i.cacota())
print((MesesAño._member_names_))    