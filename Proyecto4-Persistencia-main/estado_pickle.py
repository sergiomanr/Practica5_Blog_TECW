import os
import pickle
FICHERO = 'estado.pickle'
estado = {}
def leer_estado_pickle(fichero=FICHERO):
    if not os.path.exists(fichero):
    #    with open('estado.pickle','wb') as f:
    #     pickle.dump(estado,f) 
        return {}


    with open('estado.pickle', "rb") as f:
        return pickle.load(f)
 
def guardar_estado_pickle(estado, fichero=FICHERO):
    with open(fichero,mode= "wb") as f:
        return pickle.dump(estado, f)


if __name__ == "__main__":
    estado = leer_estado_pickle()
    print(f"El estado vale {estado}")
    estado["contador"] = estado.get("contador", 0) + 1
    guardar_estado_pickle(estado)
    