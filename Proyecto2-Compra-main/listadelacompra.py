from ast import literal_eval

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
  raise NotImplementedError

def borrar(indice):
  '''Borra de la lista el producto que se encuentra en la posición indicada'''
  raise NotImplementedError

def actualizar_precio(indice, precio):
  '''Actualiza el precio del producto con el índice dado'''
  raise NotImplementedError

def cambiar_estado(indice):
  '''Cambia el estado del producto con el índice dado entre comprado o no'''
  raise NotImplementedError

def listar_productos():
  '''Devuelve la lista de los productos'''
  raise NotImplementedError

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
  raise NotImplementedError

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
    raise NotImplementedError


def prueba_manual():
    print('Insertando 3 productos')
    insertar('Desmaquillante', 4.5, ('fiesta', 'teatro'), 'Cosméticos', 5)
    insertar('Garbanzos', 0.68, ('cocido', 'hummus'), 'Alimentación', 3)
    insertar('Hierbabuena', 1.5, ('cocktails', 'postres'), 'Alimentación', 1)

    seccion('Lista de la compra sin ordenar ni formatear')

    print(productos)

    seccion('Lista de la compra sin ordenar ni formatear (con cambio)')
    print('Cambiando un producto a comprado')
    cambiar_estado(0)
    print(productos)


    seccion('Lista de la compra sin ordenar')
    mostrar_productos()

    seccion('Lista de la compra filtradas')
    mostrar_productos(etiquetas=('cocido',))

    seccion('Lista de la compra ordenadas')
    ordenar()
    mostrar_productos()


def seccion(texto):
    print()
    print('-'*10, texto, '-'*40)
    print()


if __name__ == "__main__":
    prueba_manual()
    # menu()