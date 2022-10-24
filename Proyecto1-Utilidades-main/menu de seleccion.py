from utilidades_Sergio_Manrique import*
while True:
    respuesta = input("Que quieres hacer (escribe AYUDA para ver la lista de comandos)\n")
    if respuesta.startswith("convertir euros"):
        x = respuesta.split()
        print(euros_a_bitcoins(float(x[-1])))
    elif respuesta.startswith("convertir bitcoin"):
        x = respuesta.split()
        print(bitcoins_a_euros(float(x[-1])))
    elif respuesta.startswith("contar"):
        x = respuesta.split()
        print(contar_vocales(x[1:]))
    elif respuesta.startswith("palindromo"):
        x = respuesta.split()
        print(es_palindromo(x[1:]))
    elif respuesta.startswith("temperaturas"): 
        x = respuesta.split()
        y = x[1:-1]
        print(max_temperaturas(list(y),int(x[-1])))
    elif respuesta.startswith("cifrar"):
        x = respuesta.split()
        y = int(x[-1])
        z = x[1:-1]
        z1 = ' '.join(z)
        # print(z1)
        # print(z)
        
        print(cifrar(str(z1),y))
    elif respuesta.startswith("descifrar"):
        x = respuesta.split()
        y = int(x[-1])
        z = x[1:-1]
        z1 = ' '.join(z)
        # print(z1)
        # print(z)
        print(descifrar(str(z1),y))
    elif respuesta.startswith("productos"):
        productos()
    elif respuesta.startswith("producto nuevo"):
        x = respuesta.split()
        insertar(x[-1])
    elif respuesta.startswith("producto borrar"):
        x = respuesta.split()
        borrar(int(x[-1]))
    elif respuesta == 'AYUDA':
        print("""
- convertir euros bitcoins <cantidad>
- convertir bitcoins euros <cantidad>
- contar <texto>
- palindromo <texto>
- temperaturas <lista separada por comas> <umbral>
- cifrar <texto> <desplazamiento> 
- descifrar <texto> <desplazamiento> 
- productos
- producto nuevo <nombre>
- producto borrar <índice>
- Salir
    """)
    elif respuesta == 'Salir':
        print("\nAdiós\n")
        break
    else:
        print("\nIntroduce un comando correcto\n")
