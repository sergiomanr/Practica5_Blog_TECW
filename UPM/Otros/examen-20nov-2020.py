class Producto:
    def __init__(self, nombre,peso):
        self.nombre = nombre
        self.peso = peso
class Paquete:
    def __init__(self,id= None,peso_max=1.5):
        self.id = id
        self.productos = []
        self.peso_max = peso_max
    def cabe(self,producto: Producto):
        return self.peso()  <= self.peso_max
    def meter(self,producto):
        self.productos.append(producto)
    def peso(self):
        return sum([producto.peso for producto in self.productos])
class Almacen:
    def __init__(self):
        self.stock: dict[str, list[Producto]] = {}
    def reponer(self,nombre:str, peso:int, cantidad:int):
        if nombre not in self.stock: #mira los conjuntos de claves del dic stock
            self.stock[nombre]: list[Producto] =[]
        for i in range(cantidad):
            objeto = Producto(nombre,peso)
            self.stock[nombre].append(objeto)
    def consultar(self,nombre:str=None)->int:
        if not nombre: #si nombre es None
            total = 0
            for lista in self.stock.values():
                total += len(lista)
            return total
        if nombre not in self.stock:
            return 0
        else:
            return len(self.stock[nombre])     
    def servir(self,nombre:str)-> Producto:
        if nombre not in self.stock:
            return None
        elif len(self.stock.get(nombre)) == 0:
            return None
        else:
            return self.stock.get(nombre).pop()
class Pedido:
    def __init__(self,*producto:str):
        self.listado: list[str] = list(producto)
        self.paquetes: list[Paquete] = []
        self.pendientes: list[str] = list(producto) #self.listado[:]
    def incluir(self,paquete: Paquete):
        if paquete not in self.paquetes:
            for producto in paquete.productos:
                self.pendientes.remove(producto.nombre) 
            self.paquetes.append(paquete)
    def mostrar(self)->None:
        if len(self.pendientes) > 0:
            print('faltan', len(self.pendientes),'paquetes')
        else:
            print('Empaquetado en',len(self.paquetes),'paquetes')
pedido = Pedido('ibros','jamon','leche')
print(pedido.listado)