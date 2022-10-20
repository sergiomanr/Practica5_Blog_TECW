personas = {
    '06034309l': [],
    '06034308l': [],
    '06034307l': [],
    '06034306l': [],
    '06034305l': [],
    '06034304l': [],
    '06034303l': [],
}
if 3>1:
    personas['06034309l'].append(str('pinocho'))
    personas['06034308l'].append(str('capucha azul'))
    personas['06034307l'].append(str('las 3 cerdas'))
    personas['06034309l'].append(str('los 4 mosquegays'))
# for i in personas:
#     print(personas[i])

'''
def catalogar(titulo,autor,cantidad):
    inventario:list[list[str,str]] = []
    inventario_solo_lec = []
    for i in range(cantidad-1):
        inventario.append([titulo,autor])
    else:
        inventario_solo_lec.append([titulo,autor])
    print(inventario)
    print(inventario_solo_lec)'''
# catalogar('don quijote','cervantes',4)
# catalogar('don peyote','cervantes',4)
# catalogar('san cote','cervantes',4)
# catalogar('Sr quite','cervantes',4)
class Libro:
    '''Clase que representa un libro de la biblioteca'''
    def __init__(self, titulo: str, autor: str, prestable: bool):
        '''Constructor que recibe el título del libro (string), el nombre del autor (string),
        si se puede prestar o no (boolean)'''
        self.titulo = titulo
        self.autor = autor
        self.prestable = prestable
class Biblio:
    def catalogar(self,titulo,autor,cantidad):
            self.titulo = titulo
            self.autor = autor
            self.cantidad = cantidad
            self.inventario = []
            for i in range(self.cantidad-1):
                libro = [self.titulo,self.autor,True]
                self.inventario.append(libro)
            else:
                libro = [self.titulo,self.autor,False]
                self.inventario.append(libro)
            print(self.inventario)
libr = Biblio()
libr.catalogar('don quijote','cervantes',4)
listis = []
listis.append(Libro('tit','aut',True))
for i in listis:
    print(i.titulo,i.autor,i.prestable)