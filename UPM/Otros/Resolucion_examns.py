# class Producto:
#     '''Clase que representa un producto en un almacén'''
#     def __init__(self, nombre, peso):
#         '''Constructor que recibe el nombre del producto (string) y el peso (float)'''
#         self.nombre = nombre
#         self.peso = peso
# class Paquete:
#     '''Clase que representa un paquete lleno de objetos Producto.
#     El paquete tiene un identificador (int) único que lo representa inequívocamente.'''
#     def __init__(self, id=None, peso_max=1.5):
#         '''El identificador es un int'''
#         self.id = id
#         self.productos = []
#         self.peso_max = peso_max
#     def cabe(self, producto):
#         '''El parámetro producto es un objeto de la clase Producto'''
#         return self.peso() + producto.peso <= self.peso_max
#     def meter(self, producto):
#         '''Añade un producto (objeto Producto) al paquete'''
#         self.productos.append(producto)
#     def peso(self):
#         '''Devuelve el peso total del paquete'''
#         return sum([producto.peso for producto in self.productos])
# class Almacen:
#     def __init__(self):
#         self.stock: dict[str:] = {}
#     def reponer(self,nombre:str,peso:float,cantidad:int):
#         if nombre not in self.stock:
#             self.stock[nombre]= []
#         for i in range(cantidad):
#             self.stock[nombre].append(Producto(nombre,peso))
#         # print(self.stock)    
#     def consultar(self,nombre= None)->int:
#         if not nombre:
#             total = 0
#             for i in self.stock.values():
#                 total += len(i)
#             print(total)
#         elif nombre in self.stock.keys():
#             print(len(self.stock[nombre]))
#         elif nombre not in self.stock:
#             print(0)
#     def servir(self,nombre:str,):
#         if nombre in self.stock:
#             return self.stock.get(nombre).pop()
# class Pedido:
#     def __init__(self,*productos:str):
#         self.listado:list[str] = list(productos)
#         self.lista_compo:list[Paquete] = []
#         self.prod_pen:list[str] = list(productos)
#     def incluir(self, paquete: Paquete):
#         if paquete not in self.lista_compo:
#             for producto in paquete.productos:
#                 self.prod_pen.remove(producto)
#             self.lista_compo.append(paquete)
#         # for i in self.listado:
#         #     self.prod_pen.remove(i)
#         #     self.lista_compo.append(paquete)
#     def mostrar(self):
#         if self.prod_pen != 0:
#             print('Faltan',len(self.prod_pen),'productos')
#         elif self.prod_pen == 0:
#             print('Empaquetafo en',len(self.lista_compo),'paquetes')
# def enviar(almacen:Almacen,pedido:Pedido,id_paquete = 0):
#     paquete = Paquete(id_paquete)
#     lista_prod = []
#     for i in pedido.listado:
#             lista_prod.append(i)
#     for i in lista_prod:
#         if i in pedido.stock.keys():
#             Almacen.servir(i)
#         elif i not in pedido.stock:
#             continue
#         if Paquete.cabe(i) == True:
#             return 
#         elif Paquete.cabe(i) == False:
#             print(' no se')
        
class Libro:
    def __init__(self,titulo:str,autor:str,prestable:bool):
        self.titulo = titulo
        self.autor = autor
        self.prestable = prestable
class Lector:
    def __init__(self,dni:str,nombre:str):
        self.dni = dni
        self.nombre = nombre
class Biblioteca:
    def __init__(self):
        self.inventario:list[Libro] = []
        self.revervas: dict[str('''dni'''):list[str]] = {}
    def catalogar(self,titulo:str, autor:str, cantidad:int):
        for i in range(cantidad-1):
            objeto = Libro(titulo,autor,True)
            self.inventario.append(objeto)
        self.inventario.append(Libro(titulo,autor,False))
    def descatalogar(self,autor:str, titulo:str= None):
        libros_eliminar = []
        if not titulo:
            for i in self.inventario:
                if i.autor == autor:
                    libros_eliminar.append(i)
        else:
            for i in self.inventario:
                if i.titulo == titulo:
                    libros_eliminar.append(i)
        for i in libros_eliminar:
            self.inventario.remove(i)
    def retirar(self, titulo:str):
        libros_q_retirar = []
        for i in self.inventario:
            if i.titulo == titulo and i.prestable == True:
                libros_q_retirar.append(i)
                return True
            else:
                return None
        for i in libros_q_retirar:
            del libros_q_retirar[0]
    def reservar(self, lector:Lector, *titulos:str):
        for j in Reserva(lector.dni).listado_de_libros:
            if j.finalizada == False:
                print('No puede realizar más reservas')
            #   if Reserva(lector.dni).finalizada == False :        #Jeje no como hacer esto
            else:
                reserva_nueva = Reserva(lector.dni)
                for i in titulos:
                    if Biblioteca().retirar(i) == True:
                        for e in self.inventario:
                            if e.titulo == i and e.prestable == True:
                                if reserva_nueva.incluir(e) == False:
                                    print('ha alcanzado numero max')
                                else:
                                    reserva_nueva.incluir(e)
                    else:
                        print('no hay ejemplar prestable')
        self.revervas[lector.dni]=reserva_nueva.listado_de_libros
class Reserva:
    def __init__(self,identificador:str,):
        self.identificador = identificador
        self.listado_de_libros: list[Libro] = []
        self.finalizada = None
    def incluir(self,libro:Libro,):
        if len(self.listado_de_libros)<4:
            self.listado_de_libros.append(libro)
            return True
        else:
            return False
    def mostrar(self):
        print(self.identificador,':')
        for i in self.listado_de_libros:
            print('-',i.titulo,'-',i.autor)
    

holis = Biblioteca()
holis.reservar(Lector('1234567j','joan'),Libro('un titulo beuno','ana de arco',True))