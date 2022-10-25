
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

productos = []

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
  del productos[indice]

def actualizar_precio(indice, precio):
  '''Actualiza el precio del producto con el índice dado'''
  producto = productos[indice]
  producto["precio"] = precio

def cambiar_estado(indice):
  '''Cambia el estado del producto con el índice dado entre comprado o no'''
  producto = productos[indice]
  producto["comprado"] = True

def listar_productos():
  '''Devuelve la lista de los productos'''
  for i in productos:
    # print(productos[i].i)
    # print(i['nombre'])
    for str,valor in i.items():
      print(str,'->',valor)
    else:
      print('\n')
def mostrar_productos(comprados=True, etiquetas=(), categorias=[]):
  '''
  Muestra por pantalla todos los productos con su información. Si un producto ya ha sido comprado, se marca con una x al comienzo.
  La prioridad se indicará mediante el uso de asteriscos (*), es decir, un artículo con prioridad 5 se representará mediante cinco asteriscos (*****).
  Si comprados es False, no se muestran los productos ya comprados.
  Etiquetas es una tupla o lista con etiquetas o aclaraciones. Si está vacía, se muestran
  todos los productos. Si contiene alguna etiqueta, sólo se muestran los productos
  que tengan todas las etiquetas proporcionadas.
  Categorias es una lista con las categorías que se quieren obtener. Si está vacía, se muestran
  todos los productos. Si contiene alguna categoría, solo se muestran los productos cuya categoría
  esté contenida en la lista.
  Ejemplo en que sólo un producto ha sido comprado:
  >>> mostrar_productos()
  [x] Alimentación - Arroz integral - *** - 0.72 € - #risotto #arrozalacubana
  [ ] Alimentación - Huevos - * - 1.20 € - #arrozalacubana #tortilla 
  [ ] Cosméticos - Desmaquillante - ***** - 4.50 € - #fiesta #teatro

  >>> mostrar_productos(etiquetas=('arrozalacubana'))
  [x] Alimentación - Arroz integral - *** - 0.72 € - #risotto #arrozalacubana
  [ ] Alimentación - Huevos - * - 1.20 € - #arrozalacubana #tortilla
  '''
  for i in productos:  
    respuesta_con_x = "[x]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1]
    respuesta_sin_x = "[ ]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1]
    match comprados,len(etiquetas),len(categorias):
      case (True,0,0):
        if i.get('comprado')==True:
          print(' '.join(respuesta_con_x))        
        if i.get('comprado')==False:
          print(' '.join(respuesta_sin_x))
      case (False,0,0):
        if i.get('comprado')==False:
          print(' '.join(respuesta_sin_x))
      case (True,0,1):
          if categorias[0] in i['categoria']:
            if i.get('comprado')==True:
              print(' '.join(respuesta_con_x))        
            if i.get('comprado')==False:
              print(' '.join(respuesta_sin_x))
      case (False,0,1):
          if categorias[0] in i['categoria']:       
            if i.get('comprado')==False:
              print(' '.join(respuesta_sin_x))
      case (True,1|2,0):
        if len(etiquetas)==2:
          if etiquetas[0] in i['etiquetas'] and etiquetas[1] in i['etiquetas']:
            if i.get('comprado')==True:
              print(' '.join(respuesta_con_x))        
            if i.get('comprado')==False:
              print(' '.join(respuesta_sin_x))       
        elif len(etiquetas)==1:
          if etiquetas[0] in i['etiquetas']:
            if i.get('comprado')==True:
              print(' '.join(respuesta_con_x))        
            if i.get('comprado')==False:
              print(' '.join(respuesta_sin_x))
      case (False,1|2,0):
        if len(etiquetas)==2:
          if etiquetas[0] in i['etiquetas'] and etiquetas[1] in i['etiquetas']:        
            if i.get('comprado')==False:
              print(' '.join(respuesta_sin_x))       
        elif len(etiquetas)==1:
          if etiquetas[0] in i['etiquetas']:       
            if i.get('comprado')==False:
              print(' '.join(respuesta_sin_x)) 
      case (True,1|2,1):
        if len(etiquetas)==2:
          if etiquetas[0] in i['etiquetas'] and etiquetas[1] in i['etiquetas']:
            if categorias[0] in i['categoria']:
              if i.get('comprado')==True:
                print(' '.join(respuesta_con_x))        
              if i.get('comprado')==False:
                print(' '.join(respuesta_sin_x))       
        elif len(etiquetas)==1:
          if etiquetas[0] in i['etiquetas']:
            if categorias[0] in i['categoria']:
              if i.get('comprado')==True:
                print(' '.join(respuesta_con_x))        
              if i.get('comprado')==False:
                print(' '.join(respuesta_sin_x))
      case (False,1|2,1):
        if len(etiquetas)==2:
          if etiquetas[0] in i['etiquetas'] and etiquetas[1] in i['etiquetas']:
            if categorias[0] in i['categoria']:        
              if i.get('comprado')==False:
                print(' '.join(respuesta_sin_x))       
        elif len(etiquetas)==1:
          if etiquetas[0] in i['etiquetas']:
            if categorias[0] in i['categoria']:        
              if i.get('comprado')==False:
                print(' '.join(respuesta_sin_x))
          

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


    Por ejemplo:

    #-> mostrar
    #-> insertar Garbanzos; 0.68; Alimentación; ('cocido', 'hummus'); 3
    #-> insertar Hierbabuena; 1.5; Alimentación; ('cocktails',);  1
    #-> mostrar
    [ ] Alimentación - Garbanzos - *** - 0.68 € - #cocido #hummus
    [ ] Alimentación - Hierbabuena - * - 1.5 € - #cocktails
    #-> comprado 0
    #-> mostrar
    [x] Alimentación - Garbanzos - *** - 0.68 € - #cocido #hummus
    [ ] Alimentación - Hierbabuena - * - 1.5 € - #cocktails

    '''
    raise NotImplementedError

def ordenar():
  '''
  Se ordena la lista de productos, poniendo aquellos con mayor prioridad al principio.
  Los productos ya comprados se colocal al final.
  '''
  contador_prio =5
  while contador_prio >0:
    for i in productos:
      respuesta_con_x = "[x]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1]
      respuesta_sin_x = "[ ]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1]
      if int(i['prioridad']) == contador_prio:
        contador_prio = contador_prio -1
        if i['comprado']==True:
          print(' '.join(respuesta_con_x))
          continue
        elif i['comprado']==False:
          print(' '.join(respuesta_sin_x))
          continue

def prueba_manual():
    print('Insertando 3 productos')
    insertar('Desmaquillante', 4.5, 'Cosméticos', ('fiesta', 'teatro'), 1)    #fiesta
    insertar('Garbanzos', 0.68, 'Alimentación', ('cocido', 'hummus'), 3)
    insertar('Hierbabuena', 1.5, 'Alimentación', ('cocktails', 'postres'),1)
    insertar('Purpurina', 20, 'Cosméticos', ('fiesta', 'cocktails'),4)

    # seccion('Lista de la compra sin ordenar ni formatear')
    # listar_productos()

    # seccion('Lista de la compra sin ordenar ni formatear (con cambio)')
    # print('Cambiando un producto a comprado')
    cambiar_estado(0)
    cambiar_estado(1)
    # listar_productos()
    # seccion('Lista de la compra sin ordenar')
    
    # mostrar_productos()

    # seccion('Lista de la compra filtradas')
    # mostrar_productos(etiquetas=('cocido',))

    seccion('Lista de la compra ordenadas')
    ordenar()
    # mostrar_productos()


def seccion(texto):
    print()
    print('-'*10, texto, '-'*40)
    print()
# prueba_manual()
# print(productos)
# cambiar_estado(1)
# print(productos)


if __name__ == "__main__":
    prueba_manual()
    # menu()