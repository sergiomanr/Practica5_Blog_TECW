# Alejandro Alonso
# 2023 12 15

import threading 
from Temporizador import Temporizador
import time

class GestorDespegue():

    def __init__(self):
        self.__VIPesperando = 0
        self.__avionesperando = 0
        self.__VIPult = False
        self.__Temporizador = Temporizador(self, minutos=3)
        self.__lock = False

        self.__mutex = threading.Lock()
        self.__wait = threading.Condition(self.__mutex)

    def despegarAvion(self, id):
        with self.__mutex:
            self.__avionesperando += 1
            while self.__VIPesperando > 0 and not self.__VIPult or self.__lock:
                print('*** Avión',id,'tiene que esperar\n')
                self.__wait.wait()

            self.__VIPult = False
            self.__lock = True
            self.__avionesperando -= 1
            print('>>> Despega el avión', id,'\n')
            self.__Temporizador.iniciarTemporizador()


    def  despegarAvionVIP(self, id):
        with self.__mutex:
            self.__VIPesperando += 1
            while self.__VIPult and self.__avionesperando > 0 or self.__lock:
                print('*** Avión VIP',id,'tiene que esperar\n')
                self.__wait.wait()

            self.__VIPult = True
            self.__lock = True
            self.__VIPesperando -= 1
            print('>>> Despega el avión VIP', id,'\n')
            self.__Temporizador.iniciarTemporizador()

            

    def  finTemporizador(self):
        with self.__mutex:
            self.__lock = False
            self.__wait.notify_all()
            print('Fin de periodo de turbulencias, se puede despegar')
            

