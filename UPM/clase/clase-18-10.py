
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
    def es_finde(self)->bool:
        return self.value >= 6 
        
    def es_laborable(dia)->bool:
        return dia.value <6
    def entre(dia,dia1,dia2)->bool:
        return dia1.value < dia.value < dia2.value
    match dia:
        case DiasSemana.MARTES:
            print('hay prog')
        case DiasSemana.JUEVES:
            print('hay alb')
        case _:
            print('no hay clse')

dia: DiasSemana = DiasSemana.MARTES
nombre_dia: str = dia.name
order_dia: int = dia.value
print(dia)
print(nombre_dia)
print(dia.es_finde())
print(DiasSemana.es_laborable(dia))
print('gols')
print(dia.entre(DiasSemana.LUNES,DiasSemana.JUEVES))
todos_los_dias: list[str]= DiasSemana._member_names_
map: dict[str,DiasSemana] = DiasSemana._member_map_
# print(map)