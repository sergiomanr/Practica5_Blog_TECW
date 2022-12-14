import pickle
import os
import csv
import json
import inspect
import shutil
from typing import Any
from datetime import datetime
from habilidades_pro4 import HabilidadSubcomandos

FICHERO_PICKLE = "estado.pickle"
FICHERO_JSON = "estado.json"
FICHERO_CSV = 'estado.csv'
TEST_JSON_FILE = 'testeo.json'

def leer_estado_pickle(fichero=FICHERO_PICKLE):
    if not os.path.exists(fichero):
        with open(fichero,'wb') as f:
            pickle.dump('',f)
    with open(fichero, "rb") as f:
        return pickle.load(f)


def guardar_estado_pickle(estado, fichero=FICHERO_PICKLE):
    with open(fichero, "wb") as f:
        pickle.dump(estado,f)


def leer_estado_json(fichero=FICHERO_JSON):
    """Recupera el estado desde un JSON"""
    if not os.path.exists(fichero) or comprobar_tamaño(fichero) == 1:
        with open(fichero, mode='w', encoding='utf8') as f:
            json.dump('', f, indent=3)

    with open(fichero, mode="r", encoding="utf8") as f:
        return json.load(f)
    return {}


def guardar_estado_json(estado, fichero=FICHERO_JSON):
    """Guarda el estado proporcionado en un JSON"""
    with open(fichero, "w", encoding="utf8") as f:
        json.dump(estado, f, indent=3)


class Almacen:
    """Clase genérica para los almacenes de estado"""

    def guardar(self, estado):
        """Guarda el valor del estado."""
        raise NotImplementedError
        
    def leer(self, defecto=None):
        """Devuelve el valor guardado del estado"""
        raise NotImplementedError


class EnMemoria(Almacen):
    """Guarda valores en memoria (sin persistencia en disco)"""

    def __init__(self):
        self.estado = {}

    def guardar(self, estado):
        self.estado = estado.copy()

    def leer(self, defecto=None):
        return self.estado or defecto


class AlmacenFichero(Almacen):
    """Clase para heredar en los almacenes que usen un fichero"""

    def __init__(self, fichero):
        self.fichero = fichero


class AlmacenPickle(Almacen):
    def __init__(self, fichero):
        self.fichero = fichero

    def guardar(self, estado):
        guardar_estado_pickle(estado=estado)

    def leer(self, defecto=None):
        if comprobar_tamaño(FICHERO_PICKLE) == 1:
            return defecto
        elif comprobar_tamaño(FICHERO_PICKLE) == 0:
            return leer_estado_pickle(self.fichero)


class AlmacenJSON(Almacen):
    def __init__(self, fichero):
        self.fichero = fichero

    def guardar(self, estado):
        guardar_estado_json(estado=estado,fichero=self.fichero)

    def leer(self, defecto={}):
        if comprobar_tamaño(FICHERO_JSON) == 1:
            return defecto
        elif comprobar_tamaño(FICHERO_JSON) == 0:
            return leer_estado_json(fichero=self.fichero)

class AlmacenCSV:
    def guardar(self, diccioanrio):
        if not os.path.exists(FICHERO_CSV):
            with open(FICHERO_CSV,mode='w',encoding='utf8') as f:
                cabecera = ['clave','valor']
                csv_writer = csv.DictWriter(f,fieldnames=cabecera, delimiter=',')
                csv_writer.writeheader()
                csv_writer.writerow(diccioanrio)
        else:
            with open(FICHERO_CSV,mode='a', encoding='utf8') as f:
                csv_writer = csv.DictWriter(f,fieldnames=['clave','valor'])
                csv_writer.writerow(diccioanrio)


# class MultiAlmacen(Almacen):
#     def __init__(self, almacenes):
#         # self.almacenes = almacenes
#         raise NotImplementedError
#     def guardar(self, estado):
#         # for i in self.almacenes:
#         #     guardar_estado_pickle(estado=estado)
#         raise NotImplementedError
#     def leer(self, *args, **kwargs):
#         leer_estado_pickle()
#         raise NotImplementedError


class ListaDeLaCompra(HabilidadSubcomandos):
    """Gestión de lista de la compra que incluye excepciones"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.productos = []

    def subcomandos(self):
        return {
            "insertar": self.insertar,
            "borrar": self.borrar,
            "listar": self.listar,
            "cantidad": self.cantidad,
        }

    def insertar(self, producto):
        """Insertar un producto nuevo, lanzando una excepción si el producto es nulo o contiene un string vacío"""
        if producto == None or producto == '':
            # ErrorProductoError(producto).problema()
            raise Exception       
        else:
            self.productos.append(producto)


    def listar(self):
        """Mostrar el listado de productos"""
        for ix, producto in enumerate(self.productos):
            print(f"{ix}: {producto}")

    def borrar(self, numero):
        """Borrar un producto, lanzando una excepción si el número de producto recibido no existe"""
        if numero > len(self.productos):
            raise Exception
        else:
            del self.productos[numero]
        # try:
        #     del self.productos[numero]
        # except Exception as e:
        #     print('El número',numero,'no está en la lista','\nError tipo',f'"{e}"')

    def cantidad(self):
        """Mostrar el número de productos en la lista"""
        return len(self.productos)
'''
class ErrorProductoError(Exception):
    def __init__(self, producto):
        self.producto = producto
    def problema(self)->str:
        if self.producto == None:
            print('Se ha introducido un producto None')
        elif self.producto == '':
            print('Se ha introducido un valor vacio')'''

class ListaDeLaCompraAlmacenada(ListaDeLaCompra):
    def __init__(self, *args, almacen= EnMemoria, **kwargs):
        super().__init__(*args, **kwargs)
        self.almacen = almacen
        if self.almacen.__doc__ == None: #selecciona la clase json y no EnMemoria
        # if type(self.almacen) == '__main__.AlmacenJSON': 
            if self.almacen.leer():
                self.productos = self.almacen.leer()['lista1']
        else:
            if self.almacen.estado.keys():
                self.productos = self.almacen.estado['lista1']

    def insertar(self, producto):
        super().insertar(producto)
        self.almacen.guardar({'lista1':self.productos})

    def borrar(self, numero):
        super().borrar(numero)

        
def comprobar_tamaño(fichero):
    if os.path.getsize(fichero) == 0:
        return 1
    else:
        return 0

class ListaContactos(HabilidadSubcomandos):
    def guardar_contacto(self, informacion: dict[str,dict[Any,Any]]):
        guardar_estado_json(informacion)

if __name__ == '__main__':
    # p = EnMemoria()
    # print(p.estado)
    # t = ListaDeLaCompraAlmacenada(nombre="mis productos", almacen=p)
    # t.invocar("insertar", "probando")
    # # t.insertar('probando')
    # t2 = ListaDeLaCompraAlmacenada(nombre="mis productos", almacen=p)
    # print(t.productos)
    # print(t2.productos)
    # print(p.estado)
    leer_estado_json(fichero=TEST_JSON_FILE)
    p = AlmacenJSON(fichero=TEST_JSON_FILE)
    # print(type())
    t = ListaDeLaCompraAlmacenada(nombre="mis productos", almacen=p)
    t.invocar("insertar", "probando")
    print(t.productos)
    p = AlmacenJSON(fichero=TEST_JSON_FILE)
    t2 = ListaDeLaCompraAlmacenada(nombre="mis productos", almacen=p)
    print(t2.productos) 