class Libro:
    '''Clase que representa un libro de la biblioteca'''
    def __init__(self, titulo: str, autor: str, prestable: bool):
        '''Constructor que recibe el título del libro (string), el nombre del autor (string),
        si se puede prestar o no (boolean)'''
        self.titulo = titulo
        self.autor = autor
        self.prestable = prestable
class Lector:
    '''Clase que representa un lector de la biblioteca'''
    def __init__(self, dni: str, nombre: str):
        self.dni = dni
        self.nombre = nombre

class Biblioteca():
    def __init__(self):
        self.inventario:dict[str, dict[list[Libro]]] = {}
        self.reservas: dict[str, list[Reserva]]= {}
    def catalogar(self,titulo,autor,cantidad):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        hay_libro = 0
        for i in self.inventario:
            if i.titulo == titulo:
                hay_libro = 1
        if hay_libro == 1:    
            for i in range(cantidad): 
                self.inventario.append(Libro(self.titulo,self.autor,True))
        elif hay_libro == 0:
            for i in range(cantidad-1): 
                self.inventario.append(Libro(self.titulo,self.autor,True))
            else:
                self.inventario.append(Libro(self.titulo,self.autor,False))
    '''def catalogar(self,titulo,autor,cantidad):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        for i in range(cantidad-1):
            self.inventario.append([self.titulo,self.autor,True])
        self.inventario.append([self.titulo,self.autor,False])'''
    def lista(self):
        for i in self.inventario:
            print(i.titulo,i.autor,i.prestable)
            # print(i)
            # print(i)
    def descatalogar(self,autor:str,titulo:str = ''):
        libros_para_borrar = []
        for i in self.inventario:
            if titulo == i.titulo:
                libros_para_borrar.append(i)
            if autor == i.autor :
                libros_para_borrar.append(i)
            
        for libro in set(libros_para_borrar):
            self.inventario.remove(libro)

    def retirar(self,titulo:str):
        for i in self.inventario:
            if titulo==i.titulo and i.prestable==True:
                print('se ha sacado',i.titulo,'de',i.autor)
                self.inventario.remove(i)
                break
            if titulo==i.titulo and i.prestable==False:
                print(None)
    def reservar(self, lector:Lector,*titulos:str):
        if Reserva(lector.dni).finalizada ==False:
            print("no puedes hacer mas reservas")
        if Reserva(lector.dni).finalizada ==True:
            new_res = Reserva(lector.dni)
            # Biblioteca.retirar(titulos)
            # Reserva.incluir(Libro(titulos))
            if len(self.reservas[lector.dni]) ==5:
                x=7

class Reserva:

    def __init__(self,identificador:str):
        self.identificador=identificador
        self.listado=[]
        self.implementacion = None
        self.finalizada = None
    def incluir(self,libro: Libro,):
        if len(self.listado) <=4:
            self.listado.append(libro)
            self.implementacion = True
            self.finalizada=False
            print(self.implementacion)
        else:
            self.implementacion = False
            print(self.implementacion)
    def mostrar(self):
        print(self.identificador,':')
        for i in self.listado:
            print('\n','-',i.titulo,'-',i.autor,)



# catalogar('don quijote','cervantes',4)
librito = Biblioteca()
librito.catalogar('don quijote','cervantes',1)
librito.catalogar('el principito','reverte',2)
librito.catalogar('girasoles ciegos','mendoza',3)
librito.catalogar('riña gatos','reverte',5)
# librito.catalogar('girasoles ciegos','mendoza',4)
# librito.catalogar('cielos blancos','reverte',2)
librito.lista()
librito.descatalogar('reverte')
# librito.retirar('riña gatos')
# librito.retirar('don quijote')
print('----------------------------------')
librito.lista()

# book=Reserva('03064310654l')
# book.incluir(Libro('don quijote','cervantes',True))
# book.incluir(Libro('don quijote','cervantes',True))
# book.incluir(Libro('don quijote','cervantes',True))
# book.incluir(Libro('don quijote','cervantes',True))
# book.incluir(Libro('don quijote','cervantes',True))
# book.incluir(Libro('don quijote','cervantes',True))
# book.incluir(Libro('don quijote','cervantes',True))
# book.mostrar()




class Biblioteca2:
    def __init__(self):
        self.inventario = {}
        self.reservas = {}
    def catalogar(self, titulo, autor, cantidad):
        if autor not in self.inventario:
            self.inventario[autor]= {}
        libros = self.inventario.get(autor)
        if titulo not in libros:
            libros[titulo] = []
        libros_objetivo: list[Libro] = libros.get(titulo)
        cantidad = len(libros_objetivo)
        if cantidad == 0:
            libros_objetivo.append(titulo= titulo,autor= autor, prestable= False)
            for i in range(cantidad-1):
                libros_objetivo.append(titulo= titulo,autor= autor, prestable= True)
        else:
            for i in range(cantidad):
                libros_objetivo.append(titulo= titulo,autor= autor, prestable= True)
    def descatalogar(self, autor:str, titulo:str = None):
        if autor in self.inventario:
            if not titulo:
                del self.inventario[autor]
            else:
                libros_autor = self.inventario.get(autor)
            if titulo in libros_autor:
                del libros_autor[titulo]
    def retirar(self, titulo: str):
        for autor in self.inventario:
            for titulo_libro in autor:
                if titulo_libro == titulo:
                    lista_libros = autor.get(titulo_libro)
                    if len(lista_libros)> 1:
                        return lista_libros.pop()
        return None
        
            