import os
import unittest
import csv
import pickle
import json
import time
import random
with open('ficheros/pi.txt',mode='w',encoding='utf8') as f:
    f.write('')
def leer():
    lista_nombres = []
    with open('ficheros/numeros.txt','r',encoding='utf8') as f:
        for numero,line in enumerate(f):
            lista_nombres.append(line.rstrip().split(',')[0])
            return numero,'-->',line.rstrip()
        lineas = f.readlines()
        for linea in lineas:
            linea.rsplit(',')
    while '' in lista_nombres:
        lista_nombres.remove('')
    with open('ficheros/pi.txt',mode='a',encoding='utf8') as f:
        for i in lista_nombres:
            f.write(f'{i}\n')

def cassa(fiche):
    # with open(fiche, mode='a',encoding='utf8') as f:
    #     csv_written = csv.writer(f,delimiter=',')
    #     cabeceras = ['Matrícula','Modelo','Color','Propietario']
    #     csv_written.writerow(cabeceras)
    #     csv_written.writerow(['6543 BDF','Seat Fiesta','Amarillo','Pepe'])
    #     listis = [['Jesus','quintana','jq@gmail.com'],['Pepe','Armoso','Peposo@hotmail.com']]
    #     for i in listis:
    #         csv_written.writerow(i)

    #     csv_dict = csv.DictWriter(f,fieldnames=['Matrícula','Modelo','Color','Propietario'])
    #     csv_dict.writeheader()  #Solo poner si es la primera vez que se escribe en el docu
    #     csv_dict.writerow({'Matrícula':'1245 OHG','Modelo':'Dacia Sandero','Color':'Rosa','Propietario':'Dios'})
        
    with open(fiche,mode='r',encoding='utf8') as f:
        # for i in f.readlines():   #lo pone literal como viene
            # print(i.rstrip())
            # print(i)
            # a = 0

        for e in csv.reader(f):     #Lo pone todo con listas de str
            if len(e) > 0:
                print(e)
                a=0

        # for i in csv.DictReader(f): #Lo pone en modo de diccionario 
        #     print(i['Email'])
        #     a = 8

def textamen(fichero):
    with open(fichero, mode='r',encoding='utf8') as f:
        f.read()                    #Lo pone literal
        f.readlines()               #Lo pone como listas de 1 str que acaba al finalizar la linea        
        f.readable()                #Devuelve un bool
        f.readline()                #Lee solo la primera linea
        for i in f:                 #Cada i es una linea 
            print(i)
    
    with open(fichero, mode='w',encoding='utf8') as fishe:
        fishe.write('\nLorettta esta chetada')          #Reemplaza lo que hay por 'asd'
        fishe.writable()           #Devulve un bool no recive nada
        fishe.writelines(['MLK','.kihb\n','dxkj.x'])     #Escribe concantenados los str de dentro 
    
    with open(fichero, mode='a',encoding='utf8') as fil:
        fil.write('asd')          #Reemplaza lo que hay por 'asd'
        fil.writable()           #Devulve un bool no recive nada
        fil.writelines(['emkl','.kihb\n','dxkj.x'])     #Escribe concantenados los str de dentro 


def picklet(ficheris):
    with open(ficheris,mode='wb') as f:
        coas = 'Oh no'
        pickle.dump(coas,f)
    with open(ficheris,mode='rb') as f:
        print(pickle.load(f))

def json_derulo(disco):
    with open(disco,mode='a',encoding='utf8') as f:
        cancion = 'ouououououu'
        x = json.dumps(cancion, indent=3)
        print(x)
        f.write(x)
        json.dump(cancion,f)
    with open(disco,mode='r',encoding='utf8') as f:
        print(json.load(f))
        print(f.read())
        x = f.read()
        print(json.loads(x))

def excepciones():
    try:
        with open('jiberto.txt',mode='r') as f:
            print(f.read())
    except Exception as e:
        print('Hay una excaeccoon de tippo',e.__class__)
    finally:
        print('al final todos murieron ahogados')

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

def funcion(words):
    palindromes = []
    for i in words:
            wordis = words[:]
            for e in wordis:
                if i[::-1] == e and i not in palindromes:
                    if i == e:
                        palindromes.insert(int(round(len(palindromes)/2,1)), i)
                    else:
                        palindromes.insert(0,e)
                        palindromes.append(i)
    return len(''.join(palindromes))

def otris():
    lista = []
    for i in range(22):
        lista.append(random.choice(range(1000)))
    lista.insert(int(round(len(lista)/2,1)),'asd')
    # print()
    print(lista)
    print(lista.index('asd'))

def twoSum(nums: list[int], target: int) -> list[int]:
        for i in nums:
            for e in nums[nums.index(i)+1:]:
                if i+e == target:
                    lsita = []
                    lsita.append(nums.index(i))
                    lsita.append(nums.index(e))
                    print(lsita)
                    lsita.clear()
                    return list(nums.index(i),nums.index(e))



if __name__ == '__main__':
    # unittest.main()
    # cassa('nombrecitos.csv')
    # print(int(0b00000000000000000000011111111000))
    # print(bin(0xE2813002))
    '''for i in range(6500000): # Kaprekar Constant
        numbers = []
        for e in str(i):
            numbers.append(e)
        if (int(''.join(sorted(numbers, reverse=True)))-int(''.join(sorted(numbers)))) == i:
            print(i)'''
    twoSum([2,7,11,15],9)
    # print(time.time())
    # time.sleep(1)
    # print(time.time())
    # print(time.time())
    
    # otris()
    # textamen('Open ai/textto.txt')
    # pruebas('matriculas.csv','ficheros/cositis.csv')
    # picklet('ficheros/piquet.pickle')
    # print(funcion(["lc","cl","gg"]))
    # print(otris(121))
    # json_derulo('ficheros/jesus.json')
    # excepciones()
    # print('Lorem ipsum  ')

    