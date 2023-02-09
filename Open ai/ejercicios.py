import csv
import json
import time
import unittest
def leer_de_todo(fichero):
    with open(fichero,mode='r',encoding='utf8') as f:
        csv_reader = csv.reader(f)
        lineas= 0
        palabras = 0
        caracteres = 0
        next(csv_reader)
        for i in csv_reader:
            if len(i) != 0:
                lineas += 1
            palabras += len(i)
            for e in i:
                caracteres += len(e)
        print('Lineas->',lineas,'\nPalabras->',palabras,'\nCaracteres->',caracteres)


def copiar_de_uno_a_otro(fichero):
    with open (fichero,mode='r',encoding='utf8') as f:
        csv_reader = csv.reader(f)
        with open('Open ai/copiado.txt',mode='w',encoding='utf8') as fiche:
            for i in csv_reader:
                if len(i) != 0:
                    fiche.write(' '.join(i)+'\n')
                    print(' '.join(i))

def copia_selecta(fichero):
    with open(fichero, mode='r', encoding='utf8') as f:
        with open('Open ai/nasdumeros.txt',mode='w',encoding='utf8') as fishe:
            for i in f:
                if i.startswith('12'):
                    fishe.write(i)

def pasar_csv_json(fichero):
    # with open(fichero,mode='r',encoding='utf8') as f:
    #     csv_reader = csv.DictReader(f)
    #     with open('Open ai/archivo.json',mode='w',encoding='utf8') as fishe:    
    #         for i in csv_reader:
    #             json.dump(i,fishe)
    #             json.dump('\n',fishe)


    with open(fichero, "r",encoding='utf8') as inf:
        reader = csv.DictReader(inf)
        rows = list(reader)
        print(rows)
    with open('Open ai/archivo.json', "w") as outf:
        json.dump(rows, outf)

def cps_to_cps(fichero):
    with open(fichero, mode='r', encoding='utf8') as f:
        with open('Open ai/escrito.csv', mode='w', encoding='utf8') as fishe:
            csv_reader = csv.reader(f)
            csv_writer = csv.writer(fishe)
            posicio = 0
            for i in csv_reader:
                if len(i) != 0:    
                    i.insert(0,posicio)
                    csv_writer.writerow(i)
                    posicio += 1
def pruebas_json(fichero):
    with open(fichero,mode='r',encoding='utf8') as f:
        cosi = json.load(f)
        alumno= {
            'Nombre' : 'jaf',
            'ID':848932560,
            'Classes':['Algebra','Calculis','telekinesis','Running_around'],
            'Grades':[14,43,35,64]
        }
        temp = cosi['Alumnos']
        temp.append(alumno)
        for i in cosi['Alumnos']:
            print(i['Nombre'])
    with open(fichero,mode='w',encoding='utf8') as f:
        json.dump(cosi,f,indent=4)
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age:int):
        self.age = age
    def set_name(self,name:str):
        self.name = name
    def to_dict(self):
        return {self.name : self.age}

class test_person(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('Pep',22)
    def test_get_name(self):
        assert self.person.get_name() == 'Pep'
        assert self.person.get_name() != 'Josh'
        self.person.set_name('Josh')
        assert self.person.get_name() == 'Josh'
    def test_get_age(self):
        self.assertEqual(self.person.get_age(),22)
        self.assertNotEqual(self.person.get_age(),34)
        self.person.set_age(34)
        assert self.person.get_age() ==34
        assert self.person.age == 35

def contar_ocurrencia(fichero):
    with open(fichero,mode='r',encoding='utf8') as f:
        palabras = {}
        # print(f.read())
        print('#'*50)
        print(f.readline())
        for i in f.read().split():
                if i not in palabras.keys():
                    palabras[i] = 1
                else:
                    palabras[i] +=1 
        numero_vece = sorted(set(palabras.values()), reverse=True)
        for i in numero_vece:
            palan = []
            for palabra,veces in palabras.items():
                if i == veces:
                    palan.append(palabra)
            else:
                # print(palabras[palan[0]],'veces mencionadas',palan)
                a = 0



def xcvccv(fichero,fichero2):
    with open(fichero,mode='r',encoding='utf8') as f:
        csv_reader = csv.DictReader(f)
        grade = []
        for i in csv_reader:
            grade.append(int(i['Grade']))
        print(sum(grade)/len(grade))
    
    with open(fichero2,mode='r',encoding='utf8') as f:
        for i in json.load(f):
            print(i['first_name'],i['last_name'],'-->',i['salary'])
def cambio(fichero):
    with open(fichero,mode='r',encoding='utf8') as f:
        texto = []
        for i in f.readlines():
            for e in i.split():
                if e == 'nulla,':
                    texto.append('??')
                else:
                    texto.append(e)
    with open(fichero,mode='w',encoding='utf8') as fichero:
        fichero.writelines(texto)
def lsita_compra(fichero,fichero2):
    with open(fichero,mode='r',encoding='utf8') as f:
        with open(fichero2,mode='w',encoding='utf8',newline='') as fishe:
            csv_writer = csv.DictWriter(fishe,fieldnames=['ProductID','Name','Price','Quantity'])
            csv_writer.writeheader()
            contador = 1
            for i in csv.DictReader(f):
                if 'an' in i['Name'] :
                    csv_writer.writerow({'ProductID':contador,'Name':i['Name'],'Price':i['Price'],'Quantity':i['Quantity']})
                    contador += 1 

import logging
logging.basicConfig(level=logging.DEBUG, filename='ficheros/loggers.log',encoding='utf8')
logger = logging.getLogger('PruebasCSV Logger')
try:
    with open('Open ai/notas.csv', mode='r',encoding='utf8') as fichero:
        csv_reader = csv.reader(fichero, delimiter=',')
        logger.info('Fichero csv abierto correctamente')       
except:
    logger.critical('No puede accederse al fichero')

class error_autentific(Exception):
	def __init__(self, temperatura:float,localización:str)->None:
		self.temperatura = temperatura
		self.localizacion = localización
	def __str__(self):
		print(f'Se ha producido un error en {self.localizacion} por una temperatura de {self.temperatura}')

def testeo_error(temperatura):
    if temperatura > 24:
        raise error_autentific(temperatura,localización='España')
    else:
        print('temperatura normal')
if __name__ == '__main__':
    testeo_error(32)
#     # leer_de_todo('Open ai/ejercicio.csv')
#     # copia_selecta('Open ai/copiado.txt')
#     # pasar_csv_json('Open ai/ejercicio.csv')
#     # copiar_de_uno_a_otro('Open ai/ejercicio.csv')
#     # cps_to_cps('Open ai/ejercicio.csv')
#     # unittest.main()
#     # pruebas_json('Open ai/archivo.json')
#     # contar_ocurrencia('Open ai/textto.txt')
#     # xcvccv('Open ai/notas.csv','Open ai/salario.json')
#     # cambio('Open ai/textto.txt')
#     lsita_compra('Open ai/escrito.csv','Open ai/lista_def.csv')