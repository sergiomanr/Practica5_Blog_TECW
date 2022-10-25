def mostrar_productos(comprados=False, etiquetas=('caca','popo'), categorias=[]):
    # print(len(etiquetas.split()))
    match comprados,len(etiquetas),len(categorias):
        case (False,1|2,0):
            print('holis')
mostrar_productos()
