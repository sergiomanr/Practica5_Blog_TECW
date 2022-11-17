# with open('./datos/nombres.txt',mode='w', encoding='utf8') as file:          #con un punto te situas en la carpeta en la que estas. '..' te situas en la carpeta padre
#     lineas = file.readlines()           #crea una lista con los nombres
#     for linea in file:
#         # contenido = file.read()
#         print('->',linea)
# print(lineas)
import csv
with open('../datos/nombtos.csv', mode='r', encoding='utf8', newline='') as fichero:
    csv_writer = csv.writer(fichero, delimiter=',')
    cabeceras = ['Nombre','Apellido','Email']
    csv_writer.writerow(cabeceras)
    linea = ['Pablo','botella','yo@miweb.com']
    csv_writer.writerow(linea)
    linea = ['Enrique', None,'el@miweb.com']
    csv_writer.writerow(linea)