# import unittest
# def mi_funcion_suma(a, b):
#     return a + b
# class TestMiPrograma(unittest.TestCase):
#  def test_mi_funcion_suma(self):
#     assert mi_funcion_suma(2, 3) == 5
#     assert mi_funcion_suma(2, -3) == -1
#     resultado = mi_funcion_suma(1, 1)
#     self.assertEqual(resultado, 2)
# if __name__ == '__main__':
#  unittest.main()


# import logging, csv
# logging.basicConfig(level=logging.DEBUG, filename='programa.log')

# logger = logging.getLogger('PruebasCSV Logger')
# try:
#     with open('personas.csv', mode='r') as fichero:
#         csv_reader = csv.reader(fichero, delimiter=',')
#         logger.info('Fichero csv abierto correctamente')    
#         contador = 0
#         cabecera = None
#         for fila in csv_reader:
#             logger.debug('Leyendo la línea', contador)
#             if contador == 0:
#                 abecera = fila
#                 logger.info('Cabecera recuperada correctamente')
# except:
#     logger.critical('No puede accederse al fichero')    



