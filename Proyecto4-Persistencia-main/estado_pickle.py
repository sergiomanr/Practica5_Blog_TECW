import os
import pickle
FICHERO = '../estado.pickle'
a = {'contador' : 0}
def leer_estado_pickle(fichero=FICHERO):
    if not os.path.exists(fichero):
        return 0


    with open('estado.pickle', "rb") as f:
        pickle.load(f)
 
def guardar_estado_pickle(estado, fichero=FICHERO):
    with open(fichero,mode= "wb") as f:
        return pickle.dump(a, f, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    estado = leer_estado_pickle()
    print(f"El estado vale {estado}")
    estado["contador"] = estado.get("contador", 0) + 1
    guardar_estado_pickle(estado)
    