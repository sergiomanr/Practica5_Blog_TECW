'''class Receta:
  def __init__(self, nombre:str, ingredientes: dict[str, str] = {}, pasos: list[str] = []):
    self.nombre = nombre
    self.ingredientes = ingredientes
    self.pasos = pasos
class LibroRecetas:
    def __init__(self, nombre: str, recetas: list[Receta] = [], descripción: str = None):
      self.nombre = nombre
      self.recetas = recetas
      self.descripción = descripción
    def listar(self)-> str:
      print('Listado de Recetas')
      contador = 1
      for i in self.recetas:
        print('Receta número',str(contador)+':',i.nombre)
        contador +=1
    def mostrar_ingredientes(self, número: int):
      print('Ingredientes para',self.recetas[número].nombre)
      caca = self.recetas[número].ingredientes
      for clave,valor in caca.items():
          print(clave+':', valor)
    def mostra_pasos(self, número: int):
      print('Pasos para',self.recetas[número].nombre)
      print(self.recetas[número].pasos)
      x = 0
      for i in self.recetas[número].pasos:
        print('Paso',str(x)+':',self.recetas[número].pasos[x])
        x +=1

r1 = Receta('Patatas fritas',
  {'Patatas': '300 gramos',
    'Aceite': '300 ml'},
  ['Pelar y cortar las patatas',
    'Calentar el aceite en una sarten',
    'Freir las patatas hasta el punto deseado']
  )
r2 = Receta('Café en cafetera italiana',{'Café molido': '50 gramos','Agua': '300 ml'},
  [
'Poner el agua en el compartimento inferior (depósito) de la cafetera',
'Poner el café en el compartimento medio y cerrar la cafetera',
'Dejar que hierva el agua',
'Retirar del fuego cuando no quede agua en el depósito de la cafetera'
]
)
libro = LibroRecetas(
  nombre='recetario',
  recetas=[r1,r2],
  descripción='Libro de cocina para sobrevivir en el día a día'
)
if __name__ == '__main__':
  r2.ingredientes = {'Café molido': '55 gramos','Agua': '300 ml'} 
  print(r2.ingredientes)
  print(libro.recetas[libro.recetas.index(r1)].ingredientes)
  # libro.mostra_pasos(0)

'''
import json

class SensorTemperatura:
	def __init__(self, identificador:int, ciudad:str ='Desconocida')->None:
		self.indentificador = identificador
		self.ciudad = ciudad
		self.historial: dict[str,float] = {}
def carga_sensor(nombre:str)->SensorTemperatura:
	with open(nombre, mode='r', encoding='utf8') as f:
		diccionario_json = json.load(f)
		return SensorTemperatura(identificador = diccionario_json['identificador'], ciudad=diccionario_json['ciudad'])

    