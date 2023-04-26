import csv
import json

class Registro:
    def __init__(self, fecha: float, servidor: str, usuario: str, contraseña: str):
        self.fecha: float = fecha
        self.servidor: str = servidor
        self.usuario: str = usuario
        self.contraseña: str = contraseña
class Ataque:
    def __init__(self, tipo: str, fecha_det: float, fecha_sol: float, servidores: list[str]):
        self.tipo: str = tipo
        self.fecha_detectado: float = fecha_det
        self.fecha_solucionado: float = fecha_sol
        self.servidores: list[str] = servidores

class ComprobadorSeguridad:
    def __init__(self, fichero: str)->None:
        # self.fichero = fichero            #no hace falta porque no te lo piden en el enunciado
        self.historial:list[Ataque] = []
        self.registros: list[Registro] = []
        try:
            with open(file=fichero,mode='r',encoding='utf8') as file:
                reader : csv.DictReader = csv.DictReader(file)          #lector de fichero en diccionario
                for registro in reader:
                    fecha: float = float(registro['fecha'])
                    servidor: str = registro['servidor']
                    usuario : str = registro['usuario']
                    password: str = registro['contraseña']
                    reg: Registro = Registro(fecha, servidor,usuario,password)
                    self.registros.append(reg)
        except:
            raise Exception('Ha ocurido una excepción')
    def ataque_detectado(self, fichero: str)->list[Registro]:
        try:
            with open(file=fichero,mode='r',encoding='utf8') as file:
                ataque_json: dict = json.load(file)
                if ataque_json.get('fecha_detectada') > ataque_json.get('fecha_solucionada'):
                    raise Exception('Fechas incorrectas')
                ataque = Ataque(tipo=ataque_json['tipo'],
                    fecha_det=float(ataque_json['fecha_detectada']),
                    fecha_sol=float(ataque_json['fecha_solucionada']),
                    servidores=ataque_json['servidores'])
                #aqui tambien se puede poner la excepcion
                self.historial.append(ataque)

        except:
            raise Exception('Algo salió mal')

        expuestos: list[str] = []
        servidores: list[str] = ataque.servidores

        for servidor in servidores:
            for registro in self.registros:
                if registro.servidor == servidor and registro.fecha < ataque.fecha_solucionado:
                    expuestos.append(registro)

        return expuestos

    def informe(self, expuestos: list[Registro],fichero: str)->None:

        tabla: dict[str,list[Registro]] = {}
        for expuesto in expuestos:
            iguales: list[Registro] = []
            for registro in self.registros:
                if expuesto.usuario == registro.usuario and expuesto.contraseña == registro.contraseña: #expuesto.servidor != registro.servidor and 
                    iguales.append(registro)
            tabla[expuesto.servidor] = iguales
        with open(file=fichero,mode='w',encoding='utf8') as file:
            for servidor, lista in tabla.items():
                file.write('Registro del servidor'+servidor+' vulnerado.Se recomienda cambiar su contraseña.\n')
                if len(lista) > 1:
                    file.write('Además, ese usuario y contraseña se repetían en los siguientes servidores:')
                    for duplicado in lista:
                        if servidor != duplicado:
                            file.write('-',duplicado.servidor,'\n')
                    file.write('Por lo que también se recomienda cambiar esas contraseñas.')
                else:
                    file.write('Pero, al menos, ese usuario y contraseña eran únicos. No necesitas cambiar más contraseñas.\n')
                file.write('-'*15,'\n')
if __name__ == '__main__':
    comp = ComprobadorSeguridad('registro.csv')
    print(comp.registros)
    expuestos: list[Registro] = comp.ataque_detectado('ataque.json')
    print(len(expuestos))

