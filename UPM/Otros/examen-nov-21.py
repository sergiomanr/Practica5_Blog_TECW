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
        self.inventario = []
        self.reservas = {}
    def catalogar(self,titulo,autor,cantidad):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
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
                    a =0
            if autor == i.autor :
                libros_para_borrar.append(i)
            
        for libro in libros_para_borrar:
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






