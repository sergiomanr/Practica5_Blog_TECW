# discotecas = ["Cats","Pacha","Iron"]
# costes_soborno = [15,30,5]

# def get_edad()-> int:
#     respuesta: str=input("Dime tu edad: ")
#     edad:  int= int(respuesta)
#     return edad

# def es_mayor_de_edad(edad: int)->bool: #El parametro es oligatorio porque no hemos definido como la edad un número
#     return edad >= 18

# def elegir_discoteca()-> str:
#     discoteca = input("¿Dónde vamos? ")
#     while discoteca not in discotecas:
#         discoteca = input("No la cononzco, di otra: ")
#     print("De acuerdo. Vamos a",discoteca)
#     # coste_soborno = costes_soborno[discoteca.index(quiero_entrar_en)]
#     return discoteca

# def intenta_soborno(nombre: str)->bool:
#     soborno_al_portero = float(input("¿Cuánto de das al portero? "))
#     coste= costes_soborno[discotecas.index(nombre)]
#     if soborno_al_portero >= coste:
#         print("Venga entra")
#         return True
#     else:
#         print("Pero que dice, prueba otra vez--> ")
#         return False

# def conversacion(discoteca: str,mayor_de_edad: bool = False)-> bool:
#     if mayor_de_edad:
#         print("Puedes entrar")
#         return False
#     else:
#         # soborno_exitoso = intenta_soborno(discoteca)
#         # return soborno_exitoso
#         soborno = input("¿Quieres sobornar al portero? ")
#         passwords = ["Si","Sí","si","sí","dale"]
#         if soborno in passwords:
#             soborno_exitoso = intenta_soborno(discoteca)
#             return soborno_exitoso
#         else:
#             print("No puedes pasar")
#             return False

# edad: int = get_edad()
# mayor_de_edad: bool = es_mayor_de_edad(edad)
# disco = elegir_discoteca()
# has_entrado = conversacion(discoteca=disco, mayor_de_edad=mayor_de_edad)


# módulosç 
# import math as m
# x = int(m.sqrt(25))
# y = int(m.factorial(6))
# print(x,y)

# from math import * #saca todo para no tener que poner el math.___ 
# u = factorial(9)
# k = cos(3.14)
# print(k,u)
# __doc__ devuelve los comentarios en los ''' ''' de la variable o funcion 

#####
# random.choice es para que eliga en algo sin necesidad de poner que vaya desde 0 a lo que sea

from discotecafunciones import *
if __name__ == '__main__':
    edad: int = get_edad() 
    mayor_de_edad: bool = es_mayor_de_edad(edad)
    disco = elegir_discoteca()
    has_entrado = conversacion(discoteca=disco, mayor_de_edad=mayor_de_edad)
else:
    print("Este no es el modulo principal ")
