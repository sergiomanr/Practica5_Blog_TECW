
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
productos_ordenados = []
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
    respuesta_con_x = "[x]",i['categoria'],'-',i['nombre'],'-','*'*int(i['prioridad']),'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1],str(i['comprado'])
    respuesta_sin_x = "[ ]",i['categoria'],'-',i['nombre'],'-','*'*int(i['prioridad']),'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1],str(i['comprado'])
    match comprados,len(etiquetas),len(categorias):
      case (True,0,0):
        if i.get('comprado')==True:
          print("[x]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1],str(i['comprado']))       
        if i.get('comprado')==False:
          print("[ ]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1],str(i['comprado']))
      case (False,0,0):
        if i.get('comprado')==False:
          print(str(' '.join(respuesta_sin_x)))
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
    while True:
      respuesta = input("Que quieres hacer:\n")
      match respuesta.split():
        case ['mostrar']:
          mostrar_productos()
        case ['insertar',nombre,precio,categoria,*etiquetas,prioridad]:
          # etiquetas = tuple(etiquetas.split())
          print(etiquetas)
          insertar(nombre,int(precio),categoria,etiquetas,int(prioridad))
        case ['borrar',indice]:
          borrar(int(indice))
        case ['precio',numero,precio]:
          actualizar_precio(int(numero), int(precio))
        case ['comprado',numero]:
          cambiar_estado(int(numero))
        case ['ayuda']:
          print("""
-  mostrar
-  insertar <nombre>; <precio>; <categoria>; <etiquetas en formato tupla separadas por comas>; <prioridad>
-  borrar <indice>
-  precio <numero>; <precio>
-  comprado <numero>
-  ayuda
-  salir
          """)
        case ['Salir']:
          break


def ordenar():
  '''
  Se ordena la lista de productos, poniendo aquellos con mayor prioridad al principio.
  Los productos ya comprados se colocal al final.
  '''
  prods = []
  for i in productos:
    prods.append(i)
  for i in prods:
    productos.remove(i)
  # for e in range(5,0,-1): # la buena caca
  #   for i in prods:
  #     if i['comprado'] == False:
  #       if int(i['prioridad']) == e:
  #         productos.append(i)
  #         print("[ ]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1])
  # else:
  #   for e in range(5,0,-1):
  #     for i in prods:
  #       if i['comprado'] == True:
  #         if int(i['prioridad']) == e:
  #           # productos.append(i)
  #           print("[x]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1])
  for e in range(5,0,-1):
    for i in prods:
      if i['comprado'] == True:
        if int(i['prioridad']) == e:
          productos.append(i)
          # print("[x]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1])
  else:
    for e in range(5,0,-1):
      for i in prods:
        if i['comprado'] == False:
          if int(i['prioridad']) == e:
            productos.append(i)
            # print("[ ]",i['categoria'],'-',i['nombre'],'-','*'*i['prioridad'],'-',str(i['precio']),'€','-','#'+i['etiquetas'][0],'#'+i['etiquetas'][1])
  
    

def prueba_manual():
    print('Insertando 3 productos')
    insertar('Desmaquillante', 4.5,  'Cosméticos',('fiesta', 'teatro'), 5)
    insertar('Garbanzos', 0.68, 'Alimentación', ('cocido', 'hummus'), 3)
    insertar('Hierbabuena', 1.5,  'Alimentación',('cocktails', 'postres'), 1)
    menu()
    # seccion('Lista de la compra sin ordenar ni formatear')
    listar_productos()
    # print(productos)

    # seccion('Lista de la compra sin ordenar ni formatear (con cambio)')
    # print('Cambiando un producto a comprado')
    # cambiar_estado(0)
    # print(productos)


    # seccion('Lista de la compra sin ordenar')
    # mostrar_productos()

    # seccion('Lista de la compra filtradas')
    # mostrar_productos(etiquetas=('cocido',))

    # seccion('Lista de la compra ordenadas')
    # ordenar()
    # mostrar_productos()

def seccion(texto):
    print()
    print('-'*10, texto, '-'*40)
    print()

if __name__ == "__main__":
    prueba_manual()
    # menu()