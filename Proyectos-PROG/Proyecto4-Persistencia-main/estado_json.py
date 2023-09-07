import json
import os

FICHERO_JSON = "estado.json"

estado = {}
def leer_estado_json(fichero=FICHERO_JSON):
    if not os.path.exists(fichero):
        with open('estado.json','w', encoding='utf8') as f: 
            json.dump(estado, f, indent=3)

    with open(fichero, "r", encoding='utf8') as f:
        return json.load(f)

 
def guardar_estado_json(estado, fichero=FICHERO_JSON):
    with open(fichero, "w") as f:
        return json.dump(estado, f, indent=3)


if __name__ == "__main__":
    estado= leer_estado_json()
    print(f"El estado vale {estado}")
    estado["contador"] = estado.get("contador", 0) + 1
    guardar_estado_json(estado)
