import shlex
import sys
import inspect

class Habilidad:
    '''Abstracción del concepto de habilidad en un asistente.'''

    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion or self.__doc__

    def _invocar(self):
        '''Invocar la habilidad. No acepta parámetros'''
        print('Se ha invocado la habilidad',self.nombre)

    def _ayuda(self):
        '''Devolver la descripción de la habilidad'''
        # texto = self.descripcion or self.invocar.__doc__
        texto = self._invocar.__doc__
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

    def _invocar(self, cantidad):
        '''Convertir una cantidad la divisa original a la divisa objetivo'''
        return round(float(cantidad)*self.tasa,2) #hay que poner return para que funcione
class Contador(Habilidad):
    def _invocar(self, palabra):
        '''Devuelve el número de vocales que tiene el texto dado.'''
        vocales = 0
        if type(palabra) == list:
            palabra = ''.join(palabra)
        for x in palabra.lower():
            if x == 'a' or x== 'e' or x== 'i' or x== 'o' or x== 'u':
                vocales += 1
        return vocales


class DetectorPalindromos(Habilidad):
    def _invocar(self, palabra):
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
        if not habilidad :
            print('Habilidades disponibles:')
            for hab in self.habilidades.values():
                print(f'\t{hab.nombre}:\t{hab.descripcion}')
            return
        if habilidad not in self.habilidades:
            print(f'Habilidad no encontrada: {habilidad}')
            return
        self.habilidades[habilidad]._ayuda()

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

        if comando == 'ayuda':
            if len(args) != 0:
                self.ayuda(args[0])
            else:
                self.ayuda()

        elif comando in self.habilidades:
            if len(args) >1:                                                #funcion accedida a través de el m = Menu(habilidades) m.emular('listadelacompra insertar "cebolla"')
                self.habilidades.get(comando)._invocar(args[0], args[1])
            else:
                self.habilidades.get(comando)._invocar(args[0])     #poner con el print() para que funcione lo de las divisas y sin para que no salga None en ListacompraP2 listar
    
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
    def __init__(self, *args, prompt=">", **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt = prompt
    def emular(self, linea):
        '''Ejecuta una línea, mostrando por pantalla el comando'''
        self.ejecutar(linea)
    def lanzar(self):
        '''Recibe instrucciones del usuario en bucle.'''
        while True:
            linea = input(self.prompt + " ")
            if self.ejecutar(linea):
                break


class MenuPreguntas(Menu):
    def convertir_linea(self, linea):
        comando = linea.strip()
        ix = 0
        args = []
        while True:
            arg = input(f"Argumento {ix}: ")
            if not arg:
                return comando, args
            args.append(arg)
            ix += 1


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

class ListaDeLaComp(Habilidad):
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

    def _subcomandos(self):
        '''
        Devuelve un diccionario de subcomandos a funciones.
        
        p.e.:
            {
            'insertar': self.insertar_producto,
            'borrar': self.borrar_producto,
            }
        '''
        return {
            'insertar': self.insertar,
            'borrar': self.borrar,
            'listar': self.listar,
            'cantidad': self.cantidad
                }

    def _invocar(self, subcomando, *args):
        self._subcomandos()[subcomando](*args)
        '''# if len(args) == 0:
        #     if subcomando == 'listar':
        #         self.listar()
        #     elif subcomando == 'cantidad':
        #         self.cantidad()
        # elif type(args[0]) == str or type(args[0]) == int: #Se accede através de objeto ListaDeLaCompra
        #     # self.subcomandos().get(subcomando)(args[0]) #Funciona con el ejemplo de m = Menu(habilidades) m.emular('listadelacompra insertar "cebolla"')
        #     self.subcomandos[subcomando](args[0])'''

    def _ayuda(self):
        if True:
            print('Comando:\t', self.nombre)
            print('Descripción:\t', self.descripcion)
            print('Subcomandos:')  
            for clv,vlr in self._subcomandos().items():
                print('\t',clv+':',vlr.__doc__)

    def decir_subcomandos(self):
        for i in inspect.getmembers(ListaCompraP2):
            if inspect.isfunction(i[1]) and not(i[0].startswith('_')): #Solo selecciona las que son funciones(porque no metodos?) y las que no empiezan por '_' por lo que solo las no privadas
                print(i[0])
        

# Descomentar para desarrollar el apartado de subcomandos
class ListaCompraP2(HabilidadSubcomandos):
    '''lista de la compra avanzada'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.productos = []
        self.subcomandos = {
    'insertar': self.insertar,
    'borrar': self.borrar,
    'listar': self.listar,
    'cantidad': self.cantidad}

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
        if len(self.productos) >= int(numero):
            self.productos.pop(int(numero))
        else:
            print('No hay suficientes productos')
    def cantidad(self):
        '''Mostrar el número de productos en la lista'''
        print(len(self.productos))

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

  def insertar(self, producto, precio=0, categoria='', etiquetas=[], prioridad="1"):
    '''Insertar un producto nuevo'''
    self.productos.append(producto)
  def listar(self):
    '''Mostrar el listado de productos'''
    for ix, producto in enumerate(self.productos):
      print(f'{ix}: {producto}')

  def borrar(self, numero):
    '''Borrar un producto'''
    self.productos.pop(int(numero))

  def cantidad(self):
    '''Mostrar el número de productos en la lista'''
    print(len(self.productos))

def prueba_menu_subcomandos():
    habilidades = [
        Divisas('bitcoin2euro', tasa=49929.38),
        Divisas('euro2bitcoin', tasa=1/49929.38),
        Contador('contarvocales', 'contador de vocales'),
        DetectorPalindromos('detectorpalindromo','Detecta si una palabra es palindroma'),
        ListaCompraP2('listacompraP2', 'Gestión de la lista de la compra'),
        Divisas('usd2euro', tasa=0.85, descripcion='Conversión de dólares a euros')
        ]
    # habilidades = [
    #         Divisas('usd2euro', tasa=0.85, descripcion='Conversión de dólares a euros'),
    #         Divisas('euro2usd', tasa=1/0.85, descripcion='Conversión de euros a dólares'),
    #     ]
    # m = Menu(habilidades)
    # print('#' * 10, 'Ayudas')
    # m.emular('ayuda')
    # m.emular('ayuda usd2euro')
    # m.emular('ayuda noexiste')
    # print('\n','#' * 10, 'Conversión')
    # m.emular('bitcoin2euro 3')
    # m.emular('euro2bitcoin 30000')
    # print('\n','#' * 10, 'Palíndromo')
    # m.emular('detectorpalindromo anitalavalatina')
    # m.emular('detectorpalindromo albertoesgordo')
    # print('\n','#' * 10, 'listacompraP2')
    # m.emular('listacompraP2 insertar "plátanos canarios"')
    # m.emular('listacompraP2 insertar Pimientos')
    # m.emular('listacompraP2 listar')
    # m.emular('listacompraP2 borrar 0')
    # m.emular('listacompraP2 listar')
    # # mp = MenuPreguntas(habilidades=habilidades)
    # # mp.lanzar()
    # m.emular('ayuda')
    # m.emular('usd2euro 100')
    # m.emular('euro2usd 100')
    # m.emular('ayuda noexiste')
    # m.emular('ayuda usd2euro')
    # round(117.65 - Divisas('euro2usd', tasa=1/0.85)._invocar(100))




    lis = ListaCompraP2(habilidades)
    # lis._invocar('insertar','platano') 
    # lis._invocar('insertar','pan')
    # lis._invocar('insertar','jamon')
    # lis._invocar('listar')
    # lis._invocar('cantidad')
    # lis._invocar('borrar', 0)
    # lis._invocar('listar')
    # print('\n','#' * 10, 'Directamente a los métodos')
    # lis.cantidad()
    # lis.insertar('arroz')
    # lis.insertar('albondigas')
    # lis.insertar('escabeche')
    # lis.listar()
    # lis.borrar(1)
    # lis.listar()
    # lis._ayuda()
    lis.decir_subcomandos()
    

   

if __name__ == '__main__':
    # print('#' * 10, 'Prueba menú simple')
    # prueba_menu_simple()
    # Descomentar para probar el apartado de subcomandos
    print('#' * 10, 'Prueba menú con subcomandos')
    prueba_menu_subcomandos()