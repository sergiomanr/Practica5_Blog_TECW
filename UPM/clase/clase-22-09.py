'''
def imprime_saludo(nombre):
#  Esta función muestra un saludo en pantalla a una persona
 print("¡Hola " + nombre.title() + "!")
# Llamada a la función
print("Desde el programa principal te queremos saludar:")
input(imprime_saludo("Di tu nombre"))
'''

# def mi_funcion(*params):
#     for p in params:
#         # pero no es que ye pasa
#         print(p*p)
# print(mi_funcion(2,5,7,8)) 
# '''Intentar poner funciones, tipar las cosas y como hacer que sea más corto'''
# palabra = 'hola'
def reverse_string(palabra):
    print(sorted(palabra))
reverse_string(input())
print(reverse_string("hola"))