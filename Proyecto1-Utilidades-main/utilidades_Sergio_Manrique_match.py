from utilidades_Sergio_Manrique import*
while True:
    respuesta = input("Que quieres hacer (escribe Ayuda para ver la lista de comandos)\n")
    match respuesta.split():
        case ["convertir",'euros','a','bitcoin', obj]:
            print(euros_a_bitcoins(int(obj)))
        case ['convertir','bitcoin','a','euros',obj]: 
            print(bitcoins_a_euros(int(obj)))
        case ['contar',*palabras]:
            print(contar_vocales(palabras))
        case ['palindromo',*palabra]:
            print(es_palindromo(palabra))
        case ['temperaturas',*temps,umbral]:
            print(max_temperaturas(temps,umbral))
        case ['cifrar',*palabras,desplazamiento]:
            print(cifrar(palabras,desplazamiento))
        case ['descifrar',*palabras,desplazamiento]:
            print(descifrar(palabras,desplazamiento))
        case ['productos']:
            print(productos())
        case ['producto','nuevo',prod]:
            insertar(prod)
        case ['producto','borrar',produc]:
            borrar(produc)
        case ['hola']:
            productos.app
        case ['Ayuda']:
            print("""
                - convertir euros bitcoins <cantidad>\n- convertir bitcoins euros <cantidad>\n- contar <texto>
                - palindromo <texto>\n- temperaturas <lista separada por comas> <umbral>\n- cifrar <texto> <desplazamiento> 
                - descifrar <texto> <desplazamiento>\n- productos\n- producto nuevo <nombre>
                - producto borrar <índice>\n- Salir""")
        case ['Salir']:
            break
        case [_]:
            print('Introduce un comando correcto(escribe Ayuda para los comandos)')
                  
                