import os

FICHERO = "estado.txt"


def leer_estado(fichero=FICHERO):
    if not os.path.exists(fichero):
        return 0

    with open(fichero, "r") as f:
        return float(f.read())

 
def guardar_estado(estado, fichero=FICHERO):
    with open(fichero, "w") as f:
        # Usar el protocolo más alto posible en esta versión
        f.write(str(estado))

# for i in range(1,20):
#     contador = leer_estado()
#     print(f"El contador vale {contador}")
#     # contador = (contador)/2+1/(contador)
#     # contador = 1/(4-contador)
#     # contador += ((i**2+1)**(1/2)-i)/i
#     contador = contador*(i/(i+7))
#     guardar_estado(contador)
# # else:
# #     print(2**(1/2))
contador = leer_estado()
print(f'El contador vale {contador}')
contador += 1
guardar_estado(contador)