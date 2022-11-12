with open('./datos/nombres.txt',mode='w', encoding='utf8') as file:          #con un punto te situas en la carpeta en la que estas. '..' te situas en la carpeta padre
    lineas = file.readlines()           #crea una lista con los nombres
    for linea in file:
        # contenido = file.read()
        print('->',linea)
print(lineas)
