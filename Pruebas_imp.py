
nombres = ["alberto","luiS", "ana", "pablo", "julian"]


# nombres[1] = "Mónica" #sustituir un elemento
nombres.append("Julián".lower()) #meter al final un elemento
# nombres.insert(2,"Diego") #insertar en la posicion()
# del nombres[2] #eliminar un elemnto en una posición notificado por posicion  
# print(nombres.index("alberto")) #util para buscar la localizacion de un elemnto 
# nombres.remove("Ana") #eliminar un elemento notificado por como se llama
# popped_nombres = nombres.pop() #popped_... es solo un nombre. 
# En pop(x) hacemos que un valor se vaya momentaneamente con el print pero se puede recuperar con el pop()
# ultimo_conocido = nombres.pop()
# print(len(nombres))
''' 
lista = [1,2,3]
mas = [4,5,7]
lista.extend(mas)
print(lista)
'''

# nombres.sort(reverse=True) #ordenar alfabeticamente los elemntos y al reves de forma permanete. En el print es print(sorted(nombres, reverse=true))
print(nombres)
#print("""Hola chicos  para dividir el parrafo
# que tal el día""")  
# 
# print("Hola chicos\   para que continue
# que tal el día") 

# print("Hombre la verdad es que si no",
# "pero bueno yo no pienso eso ")

''' Looops
Paises=['Alemania','Japon','España','Portugal']
for pais in Paises:
     print(f"{pais.capitalize()},that was fucking nit my bro")  
     print(f"Yo {pais.capitalize()} you might want to chill broski\n") 

print("tank-u for you participation in ww2")
'''
#potencias raras
'''
potencias=[] #lista sin definir
for variables in range(1,11): #variables son los numeros que va a coger
    ''''''
    potencia = variables**2  #definimos potencia como la variable al cuadrado
    potencias.append(potencia) #hacemos que "potencia" se una a la lista de potencias
    Más rápido es
    s
    potencias.append(variables**2)
min(potencias)
max(potencias)
sum(potencias)
print(potencias) 
'''  
#lo mismo pero más rápido
'''
potencias=[variables**2 for variables in range(1,5) ] #variables son los elementos y luego con el "for" "in" creamos un loop que da los valores 
print(potencias)
'''
'''
edad=18
if edad in #lo que sea:
    print("me da que no pulga")
else:
    print("dale")   
'''
'''
if "audi" and 'bmw' not in car:
    print("nooo")
else:
    print("siii")
'''
'''

print(f"Tu precio es {precio}")

lista = ["ola", "mar", "arena", "niños", "socorristas"]
print("Te gusta de la playa: ")
if "ola" in lista:
    print("duro bro")
if "mar" in lista:
    print("meh")
if "arena" in lista:
    print("rarito")
'''
#diccionarios
'''
alien_0={'x_position':0,'y_position':25,'speed':'fast'}
alien_0['length'] = 25
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"The new position is : {alien_0['x_position']}\n")
print(alien_0['length'])
'''
'''favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
valor = favorite_languages.get('jhon', 'No existe nadie con ese nombre')
print(valor)
'''
#loopear diction
'''favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for person,language in favorite_languages.items(): #.item dice de coger las parejas #key y value son cosas que se le añaden para dar nombre a lo primero y segundo
    print(f"{person.capitalize()}'s favourite language is : {language.title()}\n")
    
friends = ['phil', 'sarah']
for name in sorted(favorite_languages.keys(), reverse=True): #tambuen se puede cambiar por la de abajo
for name in favorite_languages.keys():  #con name nos referimos al 'valor' jen,sarah,adward...
    print(f"Hi {name.title()}.")
    if name in friends:
            language = favorite_languages[name].title()
            print(f"\t{name.title()}, I see you love {language}!")
    else:
            print(f"\t{name.capitalize()} can we become friends")

print("The following languages have been mentioned")
for languages in sorted(set(favorite_languages.values())): #el set() hace que los valores sean unicoos
    print(languages.title())


'''

'''
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)        
print(len(aliens))

for name, languages in favorite_languages.items():
    if len(languages) > 1:
       print(f"\n{name.title()}'s favorite languages are:")
       for language in languages:
        print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
             print(f"\t{language.title()}")

pets = {
   'poppy': {
       'name': 'poppy',
       'length': '24cm',
       'location': 'heaven',
        },
    'max': {
           'name': 'max',
           'length': '1m',
           'location': 'paris',
           },
       }
for pet,pet_info in pets.items():
    print(f"Username: {pet}")
    name = pet_info['name']
    length = pet_info['length']
    location = pet_info['location']
    print(f"Name: {name.capitalize()}")
    print(f"Length: {length.capitalize()}")
    print(f"Location: {location.capitalize()}")
'''
'''
prompt = "\nTell mesomething, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

        current_number = 0
while current_number <10:
    current_number +=1
    if current_number %2 == 0:
        continue                #hace que vuelva al inicio del loop y break que pare
    print(current_number)


prompt = "\nEnter you pizza topping: "
prompt += "\n(Write 'quit' to exit the interface)"

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza")

prompt = "\nEnter your age to know the price: "

while True:
    age = float(input(prompt))
    if age <= 3:
        print("Your ticket is free")
    elif age <= 12:
        print("Your ticket is 10$")
    elif age >12:
        print("Your ticket is 15$")
    elif age == 'quit':
        break
'''
#while loop con lista
'''
from operator import concat


unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop() #retira a los elementos de la 1ª lsita 
    print(f"Verifying user:{current_user.title()}") #Dice cuales son
    confirmed_users.append(current_user) # los mete en la otra lista

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''
# sandwich_orders = ['pepperoni','pastrami','cheese','margaritta','pastrami','fillet','pastrami','chicken','carbonara']
# print("This fucking Deli has run of the fucking pastrami\n")
# finished_sandwiches = []
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#         sandwich_hacinendose = sandwich_orders.pop()
#         print(f"I made your {sandwich_hacinendose.capitalize()}, please pay now")
#         finished_sandwiches.append(sandwich_hacinendose)
# print(f"\nThe sandwiches made are:")
# for finished_sandwich in finished_sandwiches:
#         print(finished_sandwich.title())
'''
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ") #pregunta que hace
    response = input("Which mountain would you like to climb some day? ")    #pregunta que hace
    responses[name] = response #para añadir name como Key y response como value
    repeat = input("Would you like another person to respond? (yes/no)") #repeat es otra pregunta
    if repeat == 'no':
        polling_active = False
        print("\n---Poll results---")
    elif repeat == 'yes':
        continue
    else:
        break
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
'''
'''

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet('harry') #solo para asegurarse
describe_pet(animal_type='hamster', pet_name='rufus') #si no especificamos el animal_type pone 'dog' como default

def get_formated_name(first_name,last_name,middle_name=''): #hacemos que el middle_name sea opcional
    if middle_name:
        full_name = f'{first_name.title()} {middle_name.title()} {last_name.title()}'
    else:
                full_name = f'{first_name.title()} {last_name.title()}'
    return full_name.title()
musician = get_formated_name('jimi','hendrix')
print(musician)
musician = get_formated_name('john', 'hooker', 'lee')
print(musician)


##############################################
def get_formatted_name(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()
while True:
   print("\nPlease tell me your name:")
   print("(enter 'q' at any time to quit)")
   f_name = input("First name: ")
   if f_name == 'q':
    break
   l_name = input("Last name: ")
   if l_name == 'q':
    break

   formatted_name = get_formatted_name(f_name,l_name)
   print(f"\nHello, {formatted_name}!")

'''
# mensaje = f"Hola {nombres[1].capitalize()} y {nombres[2].capitalize()} como estais mis primo"
# print(nombres)

'''Multiplicar los elementos de una lista'''
 # def multiplicacion(numeros):
#     resultado = 1
#     for x in numeros:
#         resultado=resultado*x
#     print(resultado)
# multiplicacion([2,2,2])
'''Coger una palabra y escribirla hacia atras'''
def reverse_string(palabra):
    revertido =''.join(reversed(palabra)) 
    print(revertido)
reverse_string("hola")
########Mejor########
a = 'arroz'
print(a[::-1]) #Si la variable es un int hay que poner str() para que el comando funcione. Se puede llegar a poner un float 12.52 = 25.21

'''No recomendable'''
n = int(input ("¿Cuántos viajeros llegan al pueblo?\n"))
contagiados_dias = []
for dias in range(10):
    dia = 4 
    contagiados = 1
    if dias == 0:
        contagiados_dias.append(n)
    else:
        formula = (contagiados_dias[dias-1])*3
        contagiados_dias.append(formula)
# print ("El número de contagios durante el cuarto día, con", n, "viajeros es:",contagiados_dias[dia-1])

################
'''Comprobar si una lista es palindroma'''
lista = [1,2,1]
def lista_palindromo(lista: list):
    if  lista == lista[::-1]:
        print(True)
    else:
        print(False)
lista_palindromo(lista)

nums = [2,1,1,4,2]
def diferente(nums: list):
  sin_rep = []
  for i in nums:
    if i not in sin_rep:
      sin_rep.append(i)
    elif i in sin_rep:
      sin_rep.remove(i)
  for e in sin_rep:
    print(e)

diferente(nums)

song = "The rain in Spain..." 
wds = song.split()      #['the','rain','in','spain']
ads = song.split('rain') #['The ', ' in Spain...']
print(wds, ads)
'''
https://openbookproject.net/thinkcs/python/english3e/lists.html
'''