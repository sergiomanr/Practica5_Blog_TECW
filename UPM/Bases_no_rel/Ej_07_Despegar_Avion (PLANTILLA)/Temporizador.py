 #Created by aalonso on 29/3/17.
 
import threading, TempAux

class Temporizador():

    def __init__(self, monitor, minutos):
        self.__minutos = minutos
        self.__monitor = monitor

    # Se simula a esperar el numero de segundos del parametro
    def iniciarTemporizador(self):
        #task = Temporizador.Temporizador(monitor, minutos)
        temp = TempAux.TempAux(self.__minutos, self.__monitor)
        temp.start()





 