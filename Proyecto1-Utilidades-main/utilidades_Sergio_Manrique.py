EURO_BITCOIN_RATE = 44471.78

def sumar_numeros(num1, num2):
    '''Suma los dos numeros proporcionados.'''
    suma = num1 + num2
    return suma

'''Conversión euros/btc y btc/euros'''
def euros_a_bitcoins(euros):
  return float(int(euros)/44570.17)

def bitcoins_a_euros(numero: float):
  return float(numero*44570.17)
  numero.endswith
'''Contar vocales'''
def contar_vocales(texto):
  '''Devuelve el número de vocales que tiene el texto dado.'''
  vocales = 0
  if type(texto) == list:
    texto = ''.join(texto)
  for x in texto.lower():
    if x == 'a' or x== 'e' or x== 'i' or x== 'o' or x== 'u':
      vocales += 1
  return vocales

'''Palindromo'''
def es_palindromo(texto: str)-> bool:
  '''Detecta si un texto es palíndromo o no'''
  if type(texto) == list:
    texto = ''.join(texto)
  c = texto.replace(',',' ')
  b = c.replace('.',' ')
  a = list(b.lower())
  while ' ' in a:
    a.remove(' ')
  if a == a[::-1]:
    return True
  else:
    return False

'''Temperatura'''
def max_temperaturas(temperaturas, umbral):
  w = []
  for i in temperaturas:
    if int(i) >= umbral:
      w.append(i)
  return w

'''Lista de la compra'''
prod = []
def insertar(producto: str):
    '''Añade un producto a la lista'''
    prod.append(producto)

def borrar(numero):
    '''Devuelve el producto en el índice dado de lista de productos.'''
    del prod[numero]

def lista_productos():
  '''Devuelve los producto en formato lista.'''  
  return prod

def productos():
  '''Muestra la lista de productos con sus índices.'''
  if len(prod) == 0:
    print('No hay productos')
  else:
    contador = 0
    for i in prod:
      print(contador, i)
      contador += 1

def cantidad():
  '''Devuelve el número de productos.'''
  return len(prod)
  
'''Cifrado y descifrado'''
def cifrar(texto: str,desplazamiento:int)->str:
    clave = 'ABCDEFGHIJKLMÑOPQRSTUVWXYZÁÉÍÓÚ'
    letras_unir = []
    for e in texto.upper():
        if e in clave:
            s = clave.index(e) + desplazamiento
            if s >= len(clave):
                s = s - len(clave)
                letras_unir.append(clave[s])
            else:
                letras_unir.append(clave[s])
        else:
            letras_unir.append(e)
    return ''.join(letras_unir)

def descifrar(cifrado: str,desplazamiento:int)->str:
    clave = 'ABCDEFGHIJKLMÑOPQRSTUVWXYZÁÉÍÓÚ'
    letras_unir = []
    for e in cifrado.upper():
        if e in clave:
            s = clave.index(e) - desplazamiento
            if s < 0:
                s = s + len(clave)
                letras_unir.append(clave[s])
            else:
                letras_unir.append(clave[s])
        else:
            letras_unir.append(e)
    return ''.join(letras_unir)

'''Menú de selección'''
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
#intentar hacer con el match-case