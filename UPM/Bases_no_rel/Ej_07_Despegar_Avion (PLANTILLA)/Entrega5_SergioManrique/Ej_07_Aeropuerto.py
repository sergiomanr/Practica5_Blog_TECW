import threading, time, random, datetime
import Gestor_Despegar, Avion, AvionVIP

nAviones     =  2
nAvionesVIP  =  2
retardo      =  0.5
retardoVip   =  1
numTimes     =  2
taskCons     =  []
taskProd     =  []



second = datetime.datetime.now().second
random.seed(second)

monitor  =  Gestor_Despegar.GestorDespegue()



# Crear hebras del la clase Avion
for i in list(range(nAviones)):
    delay = random.uniform(0, retardo)
    task = Avion.Avion(i, delay, numTimes, monitor)
    task.start()
    taskCons.append(task)


# Crear hebras del la clase AvionVIP
for i in list(range(nAvionesVIP)):
    delay = random.uniform(0, retardoVip)
    task = AvionVIP.AvionVIP(i, delay, numTimes, monitor)
    task.start()
    taskProd.append(task)
    

# Esperar hebras de la clase Avion
for i in list(range(nAviones)):
    taskCons[i].join()

# Esperar hebras de la clase Avion
for i in list(range(nAvionesVIP)):          
    taskProd[i].join()

