import re

'''
Módulo de gestión la lista de la compra

Un producto es un diccionario con las siguientes claves:

* nombre, prioridad, precio, etiquetas, categoria, comprado

Por ejemplo:

producto = {
  "nombre": "Huevo",
  "precio": 12.50,
  "etiquetas": ("huevos fritos", "empanada"),
  "categoria": "Alimentación",
  "comprado": False
}

En lecciones posteriores veremos cómo transformar esto en una estructura más elegante.
'''

productos: list[dict[str,str]] = []

def insertar(nombre, precio, categoria, etiquetas=(), prioridad=3):
  '''Añade un producto nuevo a la lista con los parámetros dados'''
  productos.append({
    "nombre": nombre,
    "precio": precio,
    "categoria":categoria,
    "etiquetas":etiquetas,
    "prioridad":prioridad,
    "comprado":False
  })

def borrar(indice):
  '''Borra de la lista el producto que se encuentra en la posición indicada'''  
  if 'a' in indice or 'e' in indice or 'i' in indice or 'o' in indice or 'u' in indice:
      for i in productos:
        if i['nombre'] == indice:
          del productos[productos.index(i)]
  else:
    del productos[int(indice)]

def actualizar_precio(indice, precio):
  '''Actualiza el precio del producto con el índice dado'''
  productos[indice]["precio"] = precio

def cambiar_estado(indice):
  '''Cambia el estado del producto con el índice dado entre comprado o no'''
  productos[indice]["comprado"] = True

def listar_productos():
  '''Devuelve la lista de los productos'''
  for i in productos:
    for str,valor in i.items():
      print(str,'->',valor)
    else:
      print('\n')

def mostrar_productos(comprados=True, etiquetas=(), categorias=[]):
  '''
  Muestra por pantalla todos los productos con su información. 
  '''  
  print('\n','-'*20,f'Lista de la compra {1}','-'*20,'\n')
  for i in productos: 
    hay_etiquetas = False
    if len(etiquetas) == 0:
      hay_etiquetas = True
    else:
      x = 0
      for etiqueta in etiquetas:
        if etiqueta in i.get('etiquetas'):
          x += 1
      if x == len(etiquetas):
        hay_etiquetas = True
      
    hay_categorias = False
    if len(categorias) == 0:
        hay_categorias = True
    else:
        for categoria in categorias:
          if categoria == i.get('categoria'):
            hay_categorias = True
            break
    if not (comprados == False and i.get('comprado') == True ) and hay_categorias and hay_etiquetas:
        if i.get('comprado') == True:
          respuesta = '[x]'+' '+ f'({str(productos.index(i))})'+' '+i['categoria']+' - '+i['nombre']+' - '+'*'*int(i['prioridad'])+' - '+str(i['precio'])+' € - '
        else:
          respuesta = '[ ]'+' '+ f'({str(productos.index(i))})'+' '+i['categoria']+' - '+i['nombre']+' - '+'*'*int(i['prioridad'])+' - '+str(i['precio'])+' € - '
        for etiqueta in i.get('etiquetas'):
          respuesta += '#'+etiqueta +' '
        print(respuesta)

def menu():
    '''
    Menú interactivo para modificar la lista de la compra.
    Acciones:
    -  mostrar
    -  insertar <nombre>; <precio>; <categoria>; <etiquetas en formato tupla separadas por comas>; <prioridad>
    -  borrar <indice>
    -  precio <numero>; <precio>
    -  comprado <numero>
    -  ayuda
    -  salir
    '''
    diccionario = {
      "mostrar" : mostrar_productos,
      "insertar" : insertar,
      "borrar": borrar,
      "ordenar" : ordenar,
      "actualizar" : actualizar_precio,
      "comprado" : cambiar_estado
    }
    while True:
      respuesta = input("Escriba un comando:\n")
      if respuesta == 'ayuda':
        print("""
-  mostrar
-  insertar <nombre>; <precio>; <categoria>; <etiquetas en formato tupla separadas por comas>; <prioridad>
-  borrar <indice>
-  precio <numero>; <precio>
-  comprado <numero>
-  ayuda
-  Salir\n""")
      elif respuesta == 'Salir':
        break
      elif diccionario.get(re.split('; | ',respuesta)[0]) != None:
        match re.split('; | ',respuesta):
          case ['mostrar']:
            mostrar_productos()
          case ['insertar']:
            nombre = input('Nombre del producto--> ')
            precio = input('Precio del producto--> ')
            categoria = input('Categoría del producto--> ')
            etiquetas = input('etiquetas del producto--> ')
            etiquetas = list(etiquetas.split())
            prioridad = input('Prioridad--> ')
            insertar(nombre,float(precio),categoria,etiquetas,int(prioridad))
          case ['borrar',indice]:
            borrar(indice) 
          case ['ordenar']:
            ordenar()
          case ['precio',numero,precio]:
            actualizar_precio(int(numero), int(precio))
          case ['comprado',numero]:
            cambiar_estado(int(numero))
      else:
        print('Mostrar:'.capitalize(),'\n',mostrar_productos.__doc__.strip(),'\n')
        print('insertar:'.capitalize(),'\n',insertar.__doc__.strip(),'\n')
        print('ordenar:'.capitalize(),'\n',ordenar.__doc__.strip(),'\n')
        print('actualizar:'.capitalize(),'\n',actualizar_precio.__doc__.strip(),'\n')
        print('comprado:'.capitalize(),'\n',cambiar_estado.__doc__.strip(),'\n')

def ordenar():
  '''
  Se ordena la lista de productos, poniendo aquellos con mayor prioridad al principio.
  Los productos ya comprados se colocal al final.
  '''
  prods = productos[:]
  productos.clear()
  max_prioridad = [i['prioridad'] for i in prods]
  for e in range(max(max_prioridad),0,-1):
    for i in prods:
      if i['comprado'] == True:
        if int(i['prioridad']) == e:
          productos.append(i)
  else:
    for e in range(max(max_prioridad),0,-1):
      for i in prods:
        if i['comprado'] == False:
          if int(i['prioridad']) == e:
            productos.append(i) 
def prueba_manual():
    insertar('Arroz integral', 0.72, 'Alimentación', ('risotto', 'arroz a la cubana'))
    insertar('Huevos', 1.20, 'Alimentación', ('arroz a la cubana', 'tortilla'), 1)
    insertar('Desmaquillante', 4.5, 'Cosméticos', ('fiesta', 'teatro'), 5)
    print('popo')
    mostrar_productos(etiquetas=('arroz a la cubana',))
    

def seccion(texto):
    print()
    print('-'*10, texto, '-'*40)
    print()

if __name__ == "__main__":
    prueba_manual()
    # menu() 