'''a, b = True, False
print(a or b)           #Son lo mismo que las puertas logicas de FPRO con (and)y(or)
c = not (a and b)
print(c)
'''

#estructuras de control
'''
mascotas = ['perro', 'gato', 'hamster']
if 'pulpo' not in mascotas:
    print("No aceptamos pulpo como animal de compañía.")

'''

# num_alumnos = 2
# capacidad_max = 79
# if num_alumnos > capacidad_max:
#     print("Necesitamos un aula grande")
# else:
#     print("Hay espacio porque somos",num_alumnos,"y hay sitios libres para llegar a",capacidad_max)

# if num_alumnos <= 2:
#     print("No hay clase...Es una tutoria privada")
# elif 2 < num_alumnos <= 15:
#     print("la gente deja de venit")
# elif 15< num_alumnos <= 30:
#     print("Todo bien")
# elif num_alumnos > 30:
#     print("Hay overbooking")

'''
quiero_entrar_en = input("¿Dónde vamos? ")
edad = int(input("Escribe tu edad: "))
mayor_edad = edad > 18
discoteca = ["Cats","Pacha","Iron"]
costes_soborno = [15,30,5]
coste_soborno = costes_soborno[discoteca.index(quiero_entrar_en)]
if mayor_edad:
    print("Puedes pasar")
else:
    soborno = input("¿Quieres sobornar al portero? ")
    passwords = ["Si","Sí","si","sí","dale"]
    if soborno in passwords:
        soborno = float(input("¿Cuánto de das al portero? "))
        if soborno >= coste_soborno:
            print("Puedes entrar ")
        else:
            print("Menudo racaño.")
    else:
        print("No puedes pasar")
'''

# while True:
#     nombre = input("Dime tu nombre: ")
#     if nombre == "q":
#         break
#     else:
#         print("Hola",nombre,"buenos días")
#         break

# contador = 0
# while contador < 10:
#     contador += 1
#     print("Esta es la iteración",contador)
# else:
#     print("Ya he terminado")
'''
contador = 0
while contador < 10:
    contador += 1
    if contador %2 == 0:
        continue
    print("Esta es la iteracion",contador)
else:
    print("Terminé")
'''

# contador = 1
# while True:
#     if contador != 5 and contador % 5 == 0:
#         print(contador, "es múltiplo de 5.")
#         break
#     print(contador, "no es múltiplo de 5.")
#     contador += 1

# animals = ['dog', 'cat', 'dog', 'cat', 'rabbit', 'cat']
# while 'cat' in animals:
#     animals.remove('cat')
# print(animals)

# animals = ['perro', 'gato', 'conejo']
# for animal in animals:
#     if animal == 'gato':
#         continue
#     print('He encontrado un', animal)
# else:
#     print('Ya no hay más animales') 

# Este código no imprimiría nunca el mensaje “He encontrado,
# un gato”, ya que cuando lo encuentra, pasa al siguiente
# elemento debido a la sentencia continue

mensaje = "Repito lo que me digas hasta que digas STOP:\n"
respuesta = ""
while "STOP" not in respuesta:      #si el stop esta en la frase se termina el código
    respuesta = input(mensaje)
    print("Repito tu mensaje:", respuesta)
else:
    print('El usuario ha decidido parar la ejecución.')

# hacer una historia o un mini videojuego interactiva, intentar meter random o hacer una lista de tareas.
#  
