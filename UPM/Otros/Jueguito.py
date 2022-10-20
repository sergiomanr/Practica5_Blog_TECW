import time
 
print("---Bienvenido a--- \n")
time.sleep(1)
print(("""
 ________________________
[                        ]
[  La senda del bosque   ]
[________________________]   
\n""").title())
time.sleep(1)
nombre = str(input("Escribe el nombre de tu personaje\n---->"))
time.sleep(0.75)
personaje = str(input("Elige personaje entre:\nSamurai \tMago\n----> "))
armas = {"Samurai":"Katana","Mago":"Bastón mágico"}
objeto_especial = {'Samurai':'Amuleto sagrado','Mago':'Barita de oro'}
time.sleep(1)
print("""Has elegido""",personaje,"""si estás preparado para la aventura presiona ENTER""")
input()
print(
    """
    Es un día nuevo, te has despertado feliz y
    te preparas para ir al poblado para
    comprar los filetes. Sales de tu casa y al
    ver la nueva señal con dirección al
    para tí nuevo poblado de Lakos decides segirla.

    Te adentras por un bosque por el cuál 
    nunca antes habías pasado, el aire es denso,
    hace frio, escuchas las ramas moverse pero no 
    es nada, o eso crees...
    """
)
time.sleep(16.5) 

print("AAAAAHHHHAHAHAHAHAHAH")
print("""
(Un macaco de metro y medio se para
enfrete de ti y te desafia a una batalla)
""")
time.sleep(3)

'''batalla 1'''
batalla_macaco = str(input("Que quieres hacer:\nAtacar \tEscapar\n----> "))
time.sleep(1.2)
#Batalla de verdad
if batalla_macaco == "Atacar" and personaje == "Samurai":
    print("Usaste tu",armas[personaje],"y por poco sales de esa batalla")
elif batalla_macaco == 'Atacar' and personaje == 'Mago':
    print("A pesar de tus debilidades al usar tu",armas[personaje],"lograste aturdir al macaco y salir corriendo.")
#Escapar
if batalla_macaco == "Escapar":
    print("Justo cuando el macaco se distrae te hechas a correr lo más rápido que puedes ")
#Consecuencia de batalla
if batalla_macaco == 'Atacar':
    time.sleep(1.5)
    print(f"""
    La batalla te ha dejado un poco debilitado 
    por lo que reposas en una caseta al final 
    de un camino divergente al caminos que recorrias    
   
    En la caseta te encuentras con Gelmir, un anciano
    que accede a ayudarte a cambio de tú dar tu {objeto_especial[personaje]}, 
    a lo que accedes sin pensar.
    
    Después de descansar un poco y comer continuas con
    tu ruta hacia el poblado de Lakos.
    """)
if batalla_macaco == 'Escapar':
    time.sleep(2)
    print("""
    Después de lo que has corrido decides parar 
    y beber agua en una fuente donde encuentras 
    a un comerciante .\n    -¿Qué te trae por aquí""",nombre,
    """esta no es zona para un""",personaje.lower(),
    """como tú- comenta el señor.    

    -Iba de camino al poblado de Lakos y decidí 
    tomar este camino y por lo que veo ha sido
    un error- respondes
    Después de recobrar tu aliento y comer un poco
    vuelves al camino en dirección al poblado.
    """)
#Lakos
time.sleep(20) 
print("""
    -------------------Lakos------------------------


    Tiempo después llegas al poblado de Lakos.
    Al entrar la ciudad te sorprende por lo
    que decides explorarla.
    """)
if personaje == 'Mago':
    time.sleep(5)
    print("""
    Entras en un restaurante solo para magos y conoces a
    Morgan, otro mago que al ver que 
    perdiste tu""", objeto_especial[personaje],"""te decide
    regalar su anillo.
    """)
    time.sleep(7)
    if batalla_macaco == 'Atacar':
        print("""
    -Menudo corte tienes ahí """,nombre.capitalize(),""", ¿qué ha pasado?- dice Morgan preocupado
        """)
        respuesta_morgan = input("Mentir/Decir la verdad:\n---->(M/DV) ")
        time.sleep(1)
        if respuesta_morgan == 'M':
            print("""
    -No es nada, me he cortado afilando mi navaja-respondes
            """)
        elif respuesta_morgan == 'DV':
            print("""
    -Me he topado con un macaco de metro y medio
    y casi muero-dices con un aire embarazoso
            """)
            print("""
    -Jajajaja que curioso porque la primera vez que
    vine a Lakos pasando por un bosque me topé 
    también con un macaco así-responde mientras enseña su herida.

    -Menudo susto me he llevado pero por suerte no es nada 
    muy difícil de curar.

    Te curas y vas al mercado
            """)
    elif batalla_macaco == 'Escapar':
        print("""
    -Muchas gracias por este anillo, me recuerda a uno 
    que tuve cuando era pequeño-comentas nostalgicamente 

    Desoués de hablar un rato sales y te diriges al mercado 
        """)
elif personaje == 'Samurai':    
    print("""
    Decides vagar por la ciudad hasta que te topas con un
    bar, entrar y hablas con el camarero.

    -¿Cuanto por un plato de comida y bebida?- preguntas

    -Uff pues depende de lo que estés dispuesto a ofrecer- dice el camarero
    """)
    regateo = True
    while regateo:
        oferta = float(input("Introduce ofeta en monedas por la comida y bebida: "))
        if oferta < 5:
            time.sleep(0.5)
            print("""
    -Pero quién te crees que soy, fuera de mi bar!!-
        """)
            continue  
        elif 5 <= oferta <= 10:
            time.sleep(0.5)
            print("""
    -Mmmmm cerca... prueba con una oferta un poco más alta-
        """) 
            continue
        elif 10 < oferta:
            time.sleep(0.5)
            print("""
    -Así sí, en un momento te sirvo tu plato    
            """)
            regateo = False
    print("""
    La comida no ha sido tan rica como esperabas por 
    lo que te vas del resturante malhumorado y te diriges al mercado
    """)
print("""
-------------------Mercado--------------
""")
print("""
    Pero a pesar de lo dicho no pasó nada
    
""")