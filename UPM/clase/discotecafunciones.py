import random
discotecas = {"Cats":15,"Pacha":30,"Iron":5}
respuestas_portero = {
    'respuestas_bordes': [
        '¿Pero de que vas?',
        'Esto es una mierda',
    ],
    'respuestas_buenas' : [
        'Venga entra',
        'Dale'
    ]
}
def get_edad()-> int:
    respuesta: str=input("Dime tu edad: ")
    edad:  int= int(respuesta)
    return edad

def es_mayor_de_edad(edad: int)->bool: #El parametro es oligatorio porque no hemos definido como la edad un número
    return edad >= 18

def elegir_discoteca()-> str: 
    discoteca = input("¿Dónde vamos? ")
    while discoteca not in discotecas:
        discoteca = input("No la cononzco, di otra: ")
    print("De acuerdo. Vamos a",discoteca)
    # coste_soborno = costes_soborno[discoteca.index(quiero_entrar_en)]
    return discoteca

def intenta_soborno(nombre: str)->bool:
    soborno_al_portero = float(input("¿Cuánto de das al portero? "))
    # coste= costes_soborno[discotecas.index(nombre)]
    coste = discotecas[nombre]
    if soborno_al_portero >= coste:
        print(random.choice(respuestas_portero["respuestas_buenas"]))
        return True
    else:
        print(random.choice(respuestas_portero["respuestas_bordes"]))
        return False

def conversacion(discoteca: str,mayor_de_edad: bool = False)-> bool:
    if mayor_de_edad:
        print(random.choice(respuestas_portero['respuestas_buenas']))
        return False
    else:
        soborno = input("¿Quieres sobornar al portero? ")
        passwords = ["Si","Sí","si","sí","dale"]
        if soborno in passwords:
            soborno_exitoso = intenta_soborno(discoteca)
            return soborno_exitoso
        else:
            print(random.choice(respuestas_portero["respuestas_bordes"]))
            return False
