nombre_fichero: str = 'contactos.txt'

with open(file=nombre_fichero, mode='w',encoding='utf8') as file:
    file.write('jose luis: 1234574584')