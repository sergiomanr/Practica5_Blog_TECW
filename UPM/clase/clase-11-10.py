class Persona:
    def __init__(self,nombre,dni) -> None:
        self.nombre = nombre
        self.dni = dni
    def info_persona(self):
        msg = 'Nombre' + self.nombre +'\t'+ 'Dni:' + self.dni
        return msg
class Alumno(Persona):
    def __init__(self,lista:list, nombre: str,dni: str,edad:int = 18,):
        super().__init__(nombre,dni)
        # self.nombre: str = nombre
        # self.dni: str = dni 
        self.edad: int = edad 
        self.lista = lista
        self.lista.append(self)
    def __del__(self):
        print("\nBorrando el alumno:",self.info())
        self.nombre = None
        self.dni = None
        self.edad = None
        
        
        # self.lista = None
        # self.lista.remove(self)
        print("Alumno asesinado?")
    def info_alumno(self)-> str:
        msg: str = 'Nombres:'
        msg += str(self.nombre) + '\t' + 'DNI:' + str(self.dni) + '\t' + 'Edad:' + str(self.edad)
        return msg
    def incrmenta_edad(self)->None:
        self.edad += 1
    def alumno_mas_viejo(self,alumno):
        edad_alumno = alumno.edad
        mi_edad = self.edad
        if mi_edad < edad_alumno:
            return alumno
        else:
            return self
listado_alumnos: list[Alumno] = [] 


alumno1: Alumno = Alumno(listado_alumnos,'Juan','06034306l',20)
alumno2: Alumno = Alumno(listado_alumnos,dni="234234",nombre="María",)
nombre1: str = alumno1.nombre
nombre2: str = alumno2.nombre

# print(alumno1.info())
# alumno1.incrmenta_edad()
# print(alumno1.info())
print(alumno1.info_alumno())
print(alumno1.info_persona())
# alumno2.nick = 'Mari'
# print(alumno2.nick)         #Problemita porque ahora alumno1 no tiene el atributo 'nick'
# alumno_mas_viejo: Alumno = alumno1.alumno_mas_viejo(alumno2)
# print(alumno_mas_viejo.info())
# alumno_mas_viejo2: Alumno = alumno2.alumno_mas_viejo(alumno1)
# print(alumno_mas_viejo2.info())
# alumno2.edad = 30
# alumno_mas_viejo3: Alumno = alumno1.alumno_mas_viejo(alumno2)
# print(alumno_mas_viejo3.info())
# print(len(listado_alumnos))'''
# for alumno in listado_alumnos:
#     print(alumno.info())
# del alumno1

# print("Listado de personas que tiene",len(listado_alumnos),"personas")
# for i in listado_alumnos:
#     print(i.info())

# for i in listado_alumnos:
#     i.__del__()
# alumno1.__del__()
# print(len(listado_alumnos))
