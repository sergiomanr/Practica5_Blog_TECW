import threading, time, random, datetime

second = datetime.datetime.now().second
random.seed(second)

class AvionVIP(threading.Thread):               
    def __init__(self, id, retardo, numTimes, monitor):  
        threading.Thread.__init__(self)    
        self.__id        = int(id)
        self.__name      = "Avion_VIP_" + str(id)                      
        self.__retardo   = retardo
        self.__numTimes  = numTimes
        self.__num       = 0
        self.__monitor   = monitor
                                                   
    def run(self):
        time.sleep(self.__retardo * 5)
        
        for i in list(range(self.__numTimes)):
            print('+++ Hebra sensor ' + self.__name + ' envía el valor' , self.__id)
            self.__monitor.despegarAvionVIP(self.__id)

            time.sleep(random.uniform(0, self.__retardo))
            self.__num = self.__num + 1

        # print('Finished thread Avion VIP %s.' % (self.name))

