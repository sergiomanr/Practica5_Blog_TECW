# def get_formated_name(first_name,middle_name='',last_name=''): #hacemos que el middle_name sea opcional
#     if middle_name:
#         full_name = f'{first_name.title()} {middle_name.title()} {last_name.title()}'
#     else:
#                 full_name = f'{first_name.title()} {last_name.title()}'
#     return full_name.title()
# musician = get_formated_name('jimi','hendrix')
# print(musician)
# musician = get_formated_name('john','lee','hooker')
# # musico = f'{nom}'
# nom = input("Enter your name: ")
# seminom = input("Enter your middle name: ")
# apellido = input("Enter your last name: ")
# musico = f'{nom} {seminom} {apellido}'
# print(musico)
'''
nombre = str(input("Tu nombre es: "))
print(nombre.lower())
# print("El nombre empieza por",nombre[0].lower(),"y acaba por",nombre[-1].lower())
print(f"El nombre empieza por {nombre[0].lower()} y acaba por {nombre[-1].lower()}")
'''

# numero = int(input("Dime cuántas palabras tendrá la lista: "))
# lista = []
# for palabras in range(numero):
#     palabras = input()
#     lista.append(palabras)
# print("\nLa lista creada es:", lista)


# cuadrado = [(elemento +1 )**2   for elemento in range(10)]
# print(cuadrado)

# lista = [2, 2, 5, 4, 7, 4, 8, 1, 9,2,5, 3, 5, 6, 3]
# sin_duplicados = []
# for elemento in lista:
#     sin_duplicados.append(elemento)
#     while elemento in lista: 
#         lista.remove(elemento)  
# print(sorted(sin_duplicados))
# lista = [2, 2, 5, 4, 7, 4, 8, 1, 9, 3, 5, 6, 3]
# sin_duplicados = []
# for elemento in lista:
#     if elemento not in sin_duplicados:
#         sin_duplicados.append(elemento)
#     else:
#         continue
# print(sorted(sin_duplicados))
# a = 5
# b = 1
# c = 4
# d = 8
# if a > b and c<d:
#     print("Hola")
# num = int(input("Introduzca un número entero: "))
# if num < 5:
#     print("pequeño")
# elif num == 5:
#     print("normal")
# elif num > 5:
#     print("grande")
# respuesta = input()
# interaccion = True
# while interaccion:
#     if respuesta == 'STOP':
#         print("Adiós")
#         interaccion = False
#     elif respuesta != 'STOP':
#         print("Siguiente")
#         interaccion = True




'''def multiplicacion(numeros):
    resultado = 1
    for x in numeros:
        resultado=resultado*x
    # print(resultado)
print(multiplicacion([2,2,2]))'''

# numero = int(input("Dime cuántas palabras tendrá la lista: "))
# lista = []
# for palabras in range(numero):
#     palabras = input()
#     lista.append(palabras)
# print("\nLa lista creada es:", lista)




# def reverse_string(palabra):
#     x=palabra.split()
    
#     ''.join(x.reverse())
#     print(x)
# reverse_string(input())
# x = input("Enter any string: ")
# a = x.split()
# a.reverse()
# print(' '.join(a))



# palabra = "hola"
# # papa=palabra.split()
# print(palabra)
s = 'Python' #initial string
# reversed=''.join(reversed(s)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
# print(reversed) #print the reversed string

'''def es_palindromo(palabra):
    revertido =''.join(reversed(palabra)) 
    if revertido == palabra:
        print(True)
    else:
        print(False)
print(type(reversed(s)))
print(es_palindromo("rececar"))'''
# def reverse_string(palabra):
#     revertido =''.join(reversed(palabra)) 
#     print(revertido)
# reverse_string("hola")

'''
lista = [1,2,3]
mas = [4,5,7]
lista.extend(mas)
print(lista)

'''
# x = [1, 2, 3]
# x.extend([4, 5])
# print(x)

def cifrar(texto: str, desplazamiento: int)-> str:
    dic = {}
    contador = 1
    for i in 'ABCDEFGHIJKLMÑOPQRSTUVWXYZÁÉÍÓÚ':
        dic[i] = contador
        contador += 1
    letras_unir = []    
    for e in texto:
        if e in dic.keys():
            s = dic[e] + desplazamiento
            if s >= 30:
                s = s-31
            for x,y in dic.items():
                if y == s:
                    letras_unir.append(x)  
        else:
            letras_unir.append(e)
    print(''.join(letras_unir))
cifrar('HOLA MUNDO', 20)
cifrar('hola', 20)
a