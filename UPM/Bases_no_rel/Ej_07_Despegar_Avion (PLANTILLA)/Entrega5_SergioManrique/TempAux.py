import threading, time

class TempAux(threading.Thread):               
    def __init__(self, minutos, monitor):     
        threading.Thread.__init__(self)      
        self.__minutos   = minutos
        self.__monitor   = monitor
                                                   
    def run(self):
        time.sleep(self.__minutos)
        self.__monitor.finTemporizador()