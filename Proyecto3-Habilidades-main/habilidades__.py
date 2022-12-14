import shlex
import sys
class Habilidad:
    '''Abstracción del concepto de habilidad en un asistente.'''

    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion or self.__doc__

    def invocar(self):
        '''Invocar la habilidad. No acepta parámetros'''
        print('Se ha invocado la habilidad',self.nombre)

    def ayuda(self):
        '''Devolver la descripción de la habilidad'''
        # texto = self.descripcion or self.invocar.__doc__
        texto = self.invocar.__doc__
        print(texto)

class Saludar(Habilidad):
    '''Saludar, dando el nombre indicado en el self.nombre'''
    def invocar(self):
        '''Saludar al usuario'''
        print('Hola, soy',self.nombre)

class Despedir(Habilidad):
    def invocar(self):
        print('Adiós desde',self.nombre)



class SaludarAAlguien(Habilidad):
    def invocar(self, nombre='anónimo'):
        print('Hola',nombre,'yo soy',self.nombre)

 
class Divisas(Habilidad):
    '''Conversión de divisas'''
    def __init__(self, *args, tasa=0.85, **kwargs):
        super().__init__(*args, **kwargs)
        self.tasa = tasa

    def invocar(self, cantidad):
        '''Convertir una cantidad la divisa original a la divisa objetivo'''
        return round(float(cantidad)*self.tasa,2)
class Contador(Habilidad):
    def invocar(self, palabra):
        '''Devuelve el número de vocales que tiene el texto dado.'''
        vocales = 0
        if type(palabra) == list:
            palabra = ''.join(palabra)
        for x in palabra.lower():
            if x == 'a' or x== 'e' or x== 'i' or x== 'o' or x== 'u':
                vocales += 1
        return vocales
class DetectorPalindromos(Habilidad):
    def invocar(self, palabra):
        '''Detecta si un texto es palíndromo o no'''
        if type(palabra) == list:
            palabra = ''.join(palabra)
        c = palabra.replace(',',' ')
        b = c.replace('.',' ')
        a = list(b.lower())
        while ' ' in a:
            a.remove(' ')
        if a == a[::-1]:
            return True
        else:
            return False


class Menu:
    '''Menú interactivo de gestión de habilidades.'''

    def __init__(self, habilidades: list):
        # habilidades es una LISTA
        # self.habilidades es un diccionario de nombre -> habilidad
        self.habilidades = {}
        for i in habilidades:
            self.habilidades[i.nombre] = i
        
    def ayuda(self, habilidad=None):
        '''
        Muestra ayuda del uso del menú. Si no se especifica una habilidad,
        se muestra la ayuda general. Esta ayuda general muestra la lista
        de habilidades, una por línea, y la descripción de cada habilidad.

        Si se especifica una habilidad, se muestra su ayuda específica.
        '''
        if not habilidad or habilidad == 'ayuda':
            print('Habilidades disponibles:')
            for hab in self.habilidades.values():
                print(f'\t{hab.nombre}:\t{hab.descripcion}')
            return
        if habilidad not in self.habilidades:
            print(f'Habilidad no encontrada: {habilidad}')
            return
        self.habilidades[habilidad].ayuda()

    def lanzar(self):
        '''Recibe instrucciones del usuario en bucle.'''
        while True:
            linea = input('> ')
            if self.ejecutar(linea):
                break

    def convertir_linea(self, linea):
        comando, *args = shlex.split(linea)
        return comando, args

    def ejecutar(self, linea):
        '''
        Recibe una línea del usuario y ejecuta la acción requerida

        Devuelve True cuando se desea parar la ejecución.
        '''
        comando, args = self.convertir_linea(linea)
        if comando in self.habilidades:
            if comando == 'listadelacompra':
                if len(args) >1: #funcion accedida a través de el m = Menu(habilidades) m.emular('listadelacompra insertar "cebolla"')
                    self.habilidades.get(comando).invocar(args[0], args[1])
                else:
                    self.habilidades.get(comando).invocar(comando, args)
            elif '2' in comando:
                print(self.habilidades.get(comando).invocar(int(args[0])))
            else:
                print(self.habilidades.get(comando).invocar(args[0]))
        elif comando.startswith('ayuda'):
            if len(args) == 0:
                self.ayuda(habilidad=comando)
            else:
                self.ayuda(habilidad=args[0])
    def emular(self, linea):
        '''Ejecuta una línea, mostrando por pantalla el comando'''
        print('>', linea)
        self.ejecutar(linea)
    def deshabilitar(self,palabra):
        del self.habilidades[palabra]
    def añadir_habilidad(self,nombre_clase):
        return getattr(sys.modules[__name__], nombre_clase)
        

class MenuComas(Menu):
    def convertir_linea(self, linea):
        comando, *args = linea.split(',')
        return comando, args
    

class MenuPrompt(Menu):
    def __init__(self, habilidades: list, prompt):
        super().__init__(habilidades)
        self.prompt = prompt
    def emular(self, linea):
        '''Ejecuta una línea, mostrando por pantalla el comando'''
        # print(self.prompt, linea)
        self.ejecutar(linea)
    def lanzar(self):
        '''Recibe instrucciones del usuario en bucle.'''
        while True:
            linea = input(f'{self.prompt} ')
            # print(linea)
            if self.ejecutar(linea):
                break


class MenuPreguntas(Menu):
    def lanzar(self):
        '''Recibe instrucciones del usuario en bucle.'''
        while True:
            linea = []
            argumento0 = input('Argumento 0: ')
            if argumento0 == 'salir':
                break
            argumento1 = input('Argumento 1: ')
            if argumento1 == 'salir':
                break
            if argumento1 == 'insertar' or argumento1 == 'borrar':
                argumento2 = input('Argumento 2: ')
                linea.append(argumento0)
                linea.append(argumento1)
                linea.append(argumento2)
            else:
                linea.append(argumento0)
                linea.append(argumento1)
            
            if self.ejecutar(linea):
                break
    def convertir_linea(self, linea):
        comando = linea[0]
        args = linea[1:]
        return comando, args

def prueba_menu_simple():
    habilidades = [
        Divisas('bitcoin2euro', tasa=49929.38, descripcion='Conversión de bitcoins a euros'),
        Divisas('euro2bitcoin', tasa=1/49929.38, descripcion='Conversión de euros a bitcoins'),
    ]
    m = Menu(habilidades)
    m.emular('ayuda')
    m.emular('bitcoin2euro 100')
    m.emular('euro2bitcoin 100')
    m.emular('ayuda noexiste')
    m.emular('ayuda bitcoin2euro')

class ListaDeLaCompra(Habilidad):
    """Gestión muy simple de lista de la compra"""
    def __init__(self, nombre, descripcion=None):
        super().__init__(nombre, descripcion)    
        self.productos = []

    def invocar(self, *args):
        argum = args[0]
        if len(args) == 1:
            if argum[0] == 'insertar':
                    self.productos.append({
                        "nombre": argum[1],
                        "precio": argum[2],
                        "categoria": argum[3],
                        "etiquetas": '',
                        "prioridad": 3,
                        "comprado":False})
            elif argum[0] == 'mostrar':
                for i in self.productos:
                    print("[ ]",i['categoria'],'-',i['nombre'],'-','*'*int(i['prioridad']),'-',(i['precio']),'€','-', f'({self.productos.index(i)})',i['etiquetas']) 
            elif argum[0] == 'listar':
                for i in self.productos:
                    for str,valor in i.items():
                        print(str,'->',valor)
                    else:
                        print('\n')
            elif argum[0] == 'borrar':
                num = argum[1]
                del self.productos[int(num)]
        else:
            if args[0] == 'insertar':
                self.productos.append(args[1])
    def ayuda(self):
        print("Acepta las acciones: insertar, borrar, listar y cantidad")


# Descomentar para desarrollar el apartado de Subcomandos
class HabilidadSubcomandos(Habilidad):
    '''Un tipo de habilidad que permite invocar varios sub-comandos'''
    def __init__(self, nombre, descripcion=None):
        super().__init__(nombre, descripcion)
        self.diccionario = {}
        # self.subcomandos = {}
    def subcomandos(self):
        '''
        Devuelve un diccionario de subcomandos a funciones.
        
        p.e.:
            {
            'insertar': self.insertar_producto,
            'borrar': self.borrar_producto,
            }
        '''
        return {


        }

    def invocar(self, subcomando, *args):
        raise NotImplementedError

    def ayuda(self):
        if True:
            print('Comando:\t', self.nombre)
            print('Descripción:\t', self.descripcion)
            print('Subcomandos:\n')
            # Muestra información de cada uno de los subcomandos
# Descomentar para desarrollar el apartado de subcomandos

class ListaDeLaCompra(HabilidadSubcomandos):
  '''Gestión muy simple de lista de la compra'''

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.productos = []

  def subcomandos(self):
    return {
      'insertar': self.insertar,
      'borrar': self.borrar,
      'listar': self.listar,
      'cantidad': self.cantidad,
      }

  def insertar(self, producto):
    '''Insertar un producto nuevo'''
    self.productos.append(producto)

  def listar(self):
    '''Mostrar el listado de productos'''
    if len(self.productos) == 0:
        print('No hay productos')
    else:
     for ix, producto in enumerate(self.productos):
      print(f'{ix}: {producto}')

  def borrar(self, numero):
    '''Borrar un producto'''
    self.productos.pop(int(numero))

  def cantidad(self):
    '''Mostrar el número de productos en la lista'''
    return len(self.productos)
    
  def invocar(self, subcomando, *args):
        if type(args[0]) == str:
            self.subcomandos().get(subcomando)(args[0]) #Funciona con el ejemplo de m = Menu(habilidades) m.emular('listadelacompra insertar "cebolla"')
        else:
            # args[0][0] != None:
            accion = args[0][0]
            if accion == 'listar':
                return self.listar()
  def ayuda(self):
    if True:
        print('Comando:\t', self.nombre)
        print('Descripción:\t', self.descripcion)
        print('Subcomandos:')  
        for clv,vlr in self.subcomandos().items():
            print(clv+':',vlr.__doc__)
            
class ListaCompraP2(HabilidadSubcomandos):
    def invocar(self):
        a = 0


def prueba_menu_subcomandos():
    habilidades = [
        Divisas('bitcoin2euro', tasa=49929.38),
        Divisas('euro2bitcoin', tasa=1/49929.38),
        Contador('contarvocales', 'contador de vocales'),
        DetectorPalindromos('detectorpalindromo','Detecta si una palabra es palindroma'),
        ListaDeLaCompra('listadelacompra', 'Gestión de la lista de la compra')
    ]
    m = Menu(habilidades)
    c = MenuComas(habilidades)
    p = MenuPrompt(habilidades,prompt='$$')
    pr = MenuPreguntas(habilidades)
    # p.lanzar()
    m.emular('ayuda')
    m.deshabilitar('bitcoin2euro')
    m.emular('listadelacompra insertar cacas')
    m.añadir_habilidad('ListaDeLaCompra')
    m.emular('ayuda')
    m.emular('listadelacompra listar')
    # pr.emular('ayuda noexiste')
    

   

if __name__ == '__main__':
#     print('#' * 10, 'Prueba menú simple')
#     # prueba_menu_simple()
#     # Descomentar para probar el apartado de subcomandos
    print('#' * 10, 'Prueba menú con subcomandos')
    prueba_menu_subcomandos()
